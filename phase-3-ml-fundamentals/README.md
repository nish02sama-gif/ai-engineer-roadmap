# Phase 3: Machine Learning Fundamentals (Weeks 5-6)

**Goal:** understand what "training a model" means, and evaluate one honestly. This is the foundation under NLP, embeddings, and LLM evaluation.

## Topics

| Days | Topic | Practice |
|---|---|---|
| 1-2 | What ML is: features, labels, training vs inference, supervised vs unsupervised | Describe three real problems as ML tasks |
| 3-4 | Train/test split, overfitting, underfitting, cross-validation | `first_model.py`, then change the split and watch scores move |
| 5-6 | Regression: linear regression, MAE/RMSE | Predict a numeric value |
| 7-9 | Classification: logistic regression, decision trees, random forests; accuracy, precision, recall, F1, confusion matrix | Compare three models on the same data |
| 10 | Pipelines, preprocessing, categorical encoding, scaling | Build one `Pipeline` |
| 11 | Basic math intuition: vectors, dot product, averages, probability, gradient descent idea | Explain gradient descent in your own words |
| 12-14 | Project (below), cleanup, push | Ticket classifier |

You don't need heavy math to start. You do need the intuition: a model is a function with adjustable numbers, and training adjusts them to reduce error.

## Start here

```bash
python phase-3-ml-fundamentals/first_model.py
```

Read the output. Then change one thing at a time (the model, `test_size`, `random_state`) and note what happens in `docs/progress-log.md`.

## Project: ticket category classifier

Use the ticket dataset idea from Phase 2, or any labelled dataset (Kaggle has many). Build a model that predicts a category or whether a ticket will breach its target resolution time.

Requirements:

1. A held-out test set you do not touch until the end.
2. A simple **baseline** first (always predict the most common class). Your model must beat it.
3. At least two real models compared with cross-validation.
4. Report precision, recall, and F1 per class, plus a confusion matrix.
5. A short section in the README: where does the model fail, and why? What would you collect to improve it?

Honest evaluation is worth more than a high score. A model with 95% accuracy on a dataset that's 95% one class has learned nothing.

## Done when

- [ ] You can explain overfitting with an example and show it in code
- [ ] You can explain precision vs recall and pick which matters for a given problem
- [ ] You've built and evaluated a classifier with a baseline and a confusion matrix
- [ ] You know why the test set is only used once
- [ ] The project README states its limitations

## GitHub skill this phase

Part 4 of `docs/github-guide.md`: keep secrets out of the repo, and use `git restore` and `git revert` when an experiment goes wrong. Try an experiment on a branch, throw it away, and notice that nothing was lost.
