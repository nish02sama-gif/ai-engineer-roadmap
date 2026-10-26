"""Phase 6 starter: a minimal RAG pipeline with no framework.

    chunk -> embed -> retrieve (cosine similarity) -> generate with citations

Run:
    python phase-6-rag/mini_rag.py "How long do refunds take?" --no-llm   # no API key needed
    python phase-6-rag/mini_rag.py "How long do refunds take?"           # needs ANTHROPIC_API_KEY
"""

import argparse
import os
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

DOCS_DIR = Path(__file__).parent / "sample_docs"
EMBED_MODEL = "all-MiniLM-L6-v2"
CHUNK_SIZE = 400      # characters per chunk. Experiment with this.
CHUNK_OVERLAP = 80    # characters shared between neighbouring chunks
TOP_K = 3


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping character windows."""
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start : start + size].strip())
        start += size - overlap
    return [c for c in chunks if c]


def load_chunks(folder: Path) -> list[dict]:
    """Read every .txt file and return chunks tagged with their source file."""
    chunks = []
    for path in sorted(folder.glob("*.txt")):
        for i, piece in enumerate(chunk_text(path.read_text(encoding="utf-8"))):
            chunks.append({"source": f"{path.name}#{i}", "text": piece})
    return chunks


def retrieve(query: str, chunks: list[dict], vectors: np.ndarray, model, k: int = TOP_K):
    """Return the k chunks most similar to the query, with their scores."""
    q = model.encode([query], normalize_embeddings=True)[0]
    scores = vectors @ q  # cosine similarity, since vectors are normalized
    best = np.argsort(scores)[::-1][:k]
    return [(float(scores[i]), chunks[i]) for i in best]


def build_prompt(question: str, hits: list[tuple[float, dict]]) -> str:
    context = "\n\n".join(f"[{c['source']}]\n{c['text']}" for _, c in hits)
    return (
        "Answer the question using ONLY the context below. Cite the source tags, "
        "like [refunds.txt#0], after each claim. If the context does not contain the "
        'answer, reply exactly: "I don\'t know based on the documents."\n\n'
        f"<context>\n{context}\n</context>\n\n"
        f"<question>{question}</question>"
    )


def generate(prompt: str) -> str:
    import anthropic  # imported here so --no-llm works without the package configured

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5"),
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    parser.add_argument("--no-llm", action="store_true", help="show retrieved chunks only")
    args = parser.parse_args()

    chunks = load_chunks(DOCS_DIR)
    model = SentenceTransformer(EMBED_MODEL)
    vectors = model.encode([c["text"] for c in chunks], normalize_embeddings=True)

    hits = retrieve(args.question, chunks, vectors, model)
    print("Retrieved chunks:")
    for score, chunk in hits:
        print(f"  {score:.2f}  {chunk['source']}: {chunk['text'][:80]!r}")

    if args.no_llm:
        return
    print("\nAnswer:")
    print(generate(build_prompt(args.question, hits)))

    # ------------------------------------------------------------------
    # YOUR TURN:
    # 1. Ask five questions. For each, is the right chunk in the top 3?
    # 2. Change CHUNK_SIZE to 150, then 1000. How does retrieval change?
    # 3. Ask something the documents do NOT answer. Does it say "I don't know"?
    # 4. Write 20 question/expected-source pairs in a JSON file and compute the
    #    retrieval hit rate automatically. This is your first evaluation set.
    # 5. Cache the vectors to disk (np.save) so you don't re-embed every run.
    # ------------------------------------------------------------------


if __name__ == "__main__":
    main()
