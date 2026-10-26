# Phase 4: NLP and Deep Learning Basics (Weeks 7-8)

**Goal:** understand how text becomes numbers, and how modern language models and embeddings work, well enough to use them confidently in Phases 5-7.

## Topics

| Days | Topic | Practice |
|---|---|---|
| 1-2 | Text preprocessing: lowercasing, tokenization, stop words, regex | Clean a set of support messages |
| 3-4 | Bag of words, TF-IDF, cosine similarity | `tfidf_search.py` and its tasks |
| 5 | Text classification with TF-IDF + logistic regression | Classify tickets by category |
| 6-7 | Neural networks intuition: layers, weights, loss, backpropagation, gradient descent | 3Blue1Brown series; then a tiny PyTorch model |
| 8-9 | PyTorch basics: tensors, `nn.Module`, training loop | Train a small network on a toy dataset |
| 10-11 | Embeddings and semantic similarity with `sentence-transformers` | Compare TF-IDF search to embedding search |
| 12 | Transformers and attention (conceptual), tokens vs words, context windows | Explain it in your own words, out loud |
| 13-14 | Hugging Face `transformers`: pipelines for sentiment and summarization; project (below) | Semantic FAQ search |

You are not expected to build a transformer from scratch. You are expected to explain what a token is, what an embedding is, what attention does conceptually, and why context length limits matter.

## Setup

This phase needs heavier packages:

```bash
pip install -r requirements-llm.txt
```

## Start here

```bash
python phase-4-nlp-deep-learning/tfidf_search.py
```

Then finish the **Your turn** tasks in that file. The key lesson: TF-IDF matches *words*, embeddings match *meaning*. You'll feel the difference when you search with a question that shares no words with the answer.

## Project: semantic FAQ search

Build a small search tool over 30 to 50 FAQ entries (write your own about a product you know, or use a public FAQ).

1. Baseline with TF-IDF.
2. Version two using `sentence-transformers` embeddings.
3. 15 test queries with the expected FAQ for each, and a score (how often is the right answer in the top 3?) for both methods.
4. A short write-up with examples where each method wins and loses.

This project is the seed of RAG. In Phase 6 you'll put an LLM on the end of it.

## Done when

- [ ] You can explain TF-IDF in two sentences
- [ ] You can explain what an embedding is and why cosine similarity compares them
- [ ] You've trained a small PyTorch model, even a toy one
- [ ] You've compared keyword search and semantic search on the same data with numbers
- [ ] You can describe tokens, context windows, and attention at a high level

## GitHub skill this phase

Notebooks and Git don't mix well (large diffs). If you use notebooks, clear outputs before committing. Tag a milestone: `git tag phase-4-complete && git push --tags`.
