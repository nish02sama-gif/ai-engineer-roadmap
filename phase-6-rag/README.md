# Phase 6: Retrieval-Augmented Generation (Weeks 11-12)

**Goal:** build a question-answering system that answers from *your* documents, cites its sources, and says "I don't know" when the documents don't contain the answer.

## Why RAG

An LLM only knows what it was trained on, and it can invent plausible-sounding answers. RAG fixes both problems: find the relevant passages first, then give them to the model and tell it to answer only from them.

```
question -> embed -> search vector index -> top-k chunks -> prompt (chunks + question) -> LLM -> answer + citations
```

## Topics

| Days | Topic | Practice |
|---|---|---|
| 1-2 | Pipeline overview, run and read `mini_rag.py` line by line | Break it on purpose, see what fails |
| 3-4 | Chunking: size, overlap, splitting on headings or paragraphs | Compare 3 chunk sizes on 15 questions |
| 5 | Embedding models, normalization, cosine similarity | Swap the embedding model, compare |
| 6 | Vector stores: in-memory NumPy first, then a library such as Chroma or FAISS | Move `mini_rag.py` to a real vector store |
| 7 | Retrieval quality: top-k, metadata filters, hybrid search (keyword + semantic), reranking | Add a keyword score and compare |
| 8 | Prompting for grounded answers, citations, refusing when context is missing | Write the "answer only from context" prompt |
| 9 | Failure modes: wrong chunk retrieved, answer split across chunks, outdated docs, prompt injection in documents | Make a list of 5 failures you can reproduce |
| 10 | **Evaluation:** retrieval hit rate, answer correctness, faithfulness | Build a 40-question test set |
| 11-14 | Project 2 (below), README, tests, push | Docs Q&A with citations |

## Start here

```bash
pip install -r requirements-llm.txt
python phase-6-rag/mini_rag.py "How long do refunds take?" --no-llm     # retrieval only, no API key needed
python phase-6-rag/mini_rag.py "How long do refunds take?"             # full RAG, needs ANTHROPIC_API_KEY
```

`mini_rag.py` is deliberately small and uses only NumPy for the vector search, so nothing is hidden. Understand it fully before you reach for a framework like LangChain or LlamaIndex. If you later use one, you'll know what it's doing for you.

## Project 2: Docs Q&A with citations

Full spec in `projects/README.md`. Use a real document set you can legally share (open-source project docs, a public handbook, your own notes). Build a test set of at least 40 questions, including 8 that the documents **cannot** answer. Report retrieval hit rate and answer accuracy, and show at least three failures with your diagnosis.

## Done when

- [ ] You can draw the RAG pipeline from memory and explain each step
- [ ] You've tested at least three chunking settings with numbers
- [ ] Your system cites sources and refuses when the answer isn't in the documents
- [ ] You have an evaluation set and a results table in the README
- [ ] You can name three ways RAG fails and how you'd detect each
- [ ] Project 2 is pushed, runnable in five commands

## GitHub skill this phase

Part 6 of `docs/github-guide.md`: fork a small open-source project and submit one documentation fix or small issue fix as a pull request. It's a good habit, and it builds your reading-other-people's-code skill.
