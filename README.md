# moderator-evals (Week 1 starter, synthetic data only)

40 made-up live-panel moments for the "should the AI moderator speak?" eval. No client data, no real names.
`data/snippets.jsonl` was written by `make_snippets.py`; edit or add cases freely.

1. Look at the data first. Run `python3 label.py` and hand-label every snippet with a one-line reason (about 30 minutes).
2. Write your own "should I speak?" prompt and run it over the snippets (Simon's `llm` CLI works well for this).
3. Add an LLM-as-judge pass and compare it to your labels. The agreement % is the weekend post's number.

Week 1 sources: https://hamel.dev/blog/posts/evals/ and https://hamel.dev/blog/posts/llm-judge/
