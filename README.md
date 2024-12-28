# Vector Space Model

The Vector Space Model is a mathematical model used for representing text documents as vectors of terms. In this model, each document is represented as a vector in a multi-dimensional space, where each dimension corresponds to a unique word in the corpus. The value in each dimension represents the frequency (or weight) of that word in the document.

- [documentation](#documentation)
- [setup](#setup)
- [usage](#usage)

## Documentation
- `concordance(self, document)` -> generates a term frequency dictionary (concordance) for a document. It *return* a dictionary where keys are words and values are their frequencies in the document.
    ```py
    document = "hello world hello"
    concordance = vector_compare.concordance(document)
    # Output: {'hello': 2, 'world': 1}
    ```

- `magnitude(self, concordance)` -> [calculates](https://en.wikipedia.org/wiki/Euclidean_distance) the magnitude of a document vector based on its concordance. It *return* a float value representing the magnitude.
    $$magnitude = \sqrt{\sum(count\ of\ words)^2}$$
    ```py
    concordance = {'hello': 2, 'world': 1}
    magnitude = vector_compare.magnitude(concordance)
    # Output: 2.236
    ```

- `relation(self, concordance1, concordance2)` -> Computes the cosine similarity between two document vectors based on their concordances. It *return* a float value representing the cosine similarity between the two document vectors (ranging from 0 to 1).

## Setup
1. Create a Virtual Environment (optional):
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install Dependencies:
```bash
pip install -r requirements.txt
```

## Usage
`file`: Path to the file to process. Supported extensions: .json (array of strings) and .txt (plain text).
- `-c`: Flag to enable a custom algorithm (optional).
- `-q`: Search term for querying (optional).
