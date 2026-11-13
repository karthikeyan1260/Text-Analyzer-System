import json
import os
import re
from collections import defaultdict
from dataclasses import dataclass, field

STOP_WORDS = {"a", "an", "the", "is", "are", "was", "of", "to", "in", "and", "or", "it"}


# --------------------------------------------------------------------------
# 1. TextProcessor: turns raw text into clean words
# --------------------------------------------------------------------------
class TextProcessor:
    _WORD = re.compile(r"[a-z0-9]+(?:'[a-z]+)?")

    def __init__(self, stop_words=None):
        self._stop_words = set(stop_words or [])

    def tokenize(self, text):
        words = self._WORD.findall(text.lower())
        return [w for w in words if w not in self._stop_words]


# --------------------------------------------------------------------------
# 2. Document: one text file on disk (file handling lives here)
# --------------------------------------------------------------------------
class Document:
    def __init__(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError(f"File not found: {path}")
        self.path = path
        self.name = os.path.basename(path)

    def scan(self):
        """Yield (line_no, offset, text). offset comes from file.tell()."""
        with open(self.path, "r", encoding="utf-8") as f:
            line_no = 0
            while True:
                offset = f.tell()          # where this line starts
                line = f.readline()
                if not line:
                    break
                line_no += 1
                yield line_no, offset, line.rstrip("\n")

    def read_line_at(self, offset):
        """Jump straight to a saved offset using seek() and read that line."""
        with open(self.path, "r", encoding="utf-8") as f:
            f.seek(offset)
            return f.readline().rstrip("\n")


# --------------------------------------------------------------------------
# 3. InvertedIndex: word -> where it appears
# --------------------------------------------------------------------------
class InvertedIndex:
    def __init__(self):
        self._data = defaultdict(lambda: defaultdict(list))

    def add(self, word, doc_name, line_no, offset):
        self._data[word][doc_name].append((line_no, offset))

    def lookup(self, word):
        return self._data.get(word, {})

    def remove_document(self, doc_name):
        """Delete every entry that belongs to one document."""
        for word in list(self._data):
            if doc_name in self._data[word]:
                del self._data[word][doc_name]
                if not self._data[word]:
                    del self._data[word]

    def word_count(self):
        return len(self._data)

    def top_words(self, n=5):
        totals = {w: sum(len(p) for p in docs.values()) for w, docs in self._data.items()}
        return sorted(totals.items(), key=lambda x: -x[1])[:n]

    def to_dict(self):
        return {w: dict(docs) for w, docs in self._data.items()}

    @classmethod
    def from_dict(cls, data):
        index = cls()
        for word, docs in data.items():
            for doc_name, positions in docs.items():
                for line_no, offset in positions:
                    index.add(word, doc_name, line_no, offset)
        return index


# --------------------------------------------------------------------------
# 4. SearchEngine: ties everything together
# --------------------------------------------------------------------------
@dataclass
class SearchResult:
    document: str
    score: int
    lines: list = field(default_factory=list)   # [(line_no, text), ...]


class SearchEngine:
    def __init__(self, index_file="search_index.json"):
        self.index_file = index_file
        self.processor = TextProcessor(STOP_WORDS)
        self.index = InvertedIndex()
        self.documents = {}
        self.left = "["     # marker placed before a matched word
        self.right = "]"    # marker placed after a matched word

    # ---- building the index ----
    def add_document(self, path):
        doc = Document(path)
        self.index.remove_document(doc.name)   # no duplicates when a file is re-added
        self.documents[doc.name] = doc
        for line_no, offset, text in doc.scan():
            for word in self.processor.tokenize(text):
                self.index.add(word, doc.name, line_no, offset)
        return doc

    def add_folder(self, folder):
        added = 0
        for name in sorted(os.listdir(folder)):
            if name.lower().endswith(".txt"):
                self.add_document(os.path.join(folder, name))
                added += 1
        return added

    # ---- searching ----
    def search(self, query, match_all=False):
        words = self.processor.tokenize(query)
        if not words:
            return []

        hits = [self.index.lookup(w) for w in words]
        if match_all:
            names = set(hits[0]).intersection(*hits[1:])
        else:
            names = set().union(*hits)

        results = []
        for name in names:
            score = sum(len(h.get(name, [])) for h in hits)
            line_offsets = {}
            for h in hits:
                for line_no, offset in h.get(name, []):
                    line_offsets[line_no] = offset
            lines = [
                (ln, self._highlight(self.documents[name].read_line_at(off), words))
                for ln, off in sorted(line_offsets.items())
            ]
            results.append(SearchResult(name, score, lines))

        return sorted(results, key=lambda r: (-r.score, r.document))

    def _highlight(self, text, words):
        for w in words:
            text = re.sub(rf"\b({re.escape(w)})\b",
                          rf"{self.left}\1{self.right}",
                          text, flags=re.IGNORECASE)
        return text

    # ---- saving / loading the index (file handling) ----
    def save_index(self):
        data = {
            "documents": {n: d.path for n, d in self.documents.items()},
            "index": self.index.to_dict(),
        }
        with open(self.index_file, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def load_index(self):
        if not os.path.exists(self.index_file):
            return False
        with open(self.index_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.index = InvertedIndex.from_dict(data["index"])
        self.documents = {}
        for name, path in data["documents"].items():
            if os.path.isfile(path):
                self.documents[name] = Document(path)
            else:
                self.index.remove_document(name)   # file moved or deleted
        return True


# --------------------------------------------------------------------------
# Console menu
# --------------------------------------------------------------------------
def print_results(results):
    if not results:
        print("No matches found.")
        return
    for r in results:
        print(f"\n{r.document}  (score: {r.score})")
        for line_no, text in r.lines:
            print(f"  line {line_no}: {text}")


def main():
    engine = SearchEngine()
    if engine.load_index():
        print(f"Loaded saved index: {len(engine.documents)} file(s).")

    menu = """
=== Word Search Engine ===
1. Add a text file
2. Add a folder of .txt files
3. Search (any word matches)
4. Search (all words must match)
5. Show statistics
6. Save index
7. Exit
"""
    while True:
        print(menu)
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                doc = engine.add_document(input("File path: ").strip())
                print(f"Indexed {doc.name}.")
            elif choice == "2":
                count = engine.add_folder(input("Folder path: ").strip())
                print(f"Indexed {count} file(s).")
            elif choice in ("3", "4"):
                query = input("Search for: ")
                print_results(engine.search(query, match_all=(choice == "4")))
            elif choice == "5":
                print(f"Documents: {len(engine.documents)}")
                print(f"Unique words: {engine.index.word_count()}")
                print("Top words:", engine.index.top_words())
            elif choice == "6":
                engine.save_index()
                print(f"Index saved to {engine.index_file}.")
            elif choice == "7":
                engine.save_index()
                print("Index saved. Goodbye!")
                break
            else:
                print("Invalid choice.")
        except (FileNotFoundError, NotADirectoryError) as e:
            print("Error:", e)


if __name__ == "__main__":
    main()