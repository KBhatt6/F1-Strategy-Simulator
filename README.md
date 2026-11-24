# F1 Strategy Simulator

> **Status: in progress.** This is an early version that runs from the terminal. The finished project will be a website with a chatbot powered by the Gemini API.

A Python tool for testing Formula 1 race strategies. It answers the question a fan asks while watching a race: *"Would pitting earlier have been faster?"*

The comparison is based on race time only.

## Goal

1. You enter a strategy for a track: your tyre compounds and the laps you pit on.
2. The simulator runs the race many times with random events such as safety cars (Monte Carlo simulation) and reports your average race time.
3. It compares your strategy against the most common strategies real teams used at that race, using real data from FastF1.

## Final vision

A website with a chatbot front end. You describe your strategy in plain English, for example "start on mediums and pit on lap 20". The chatbot passes it to the Python simulator and returns the result. The chatbot will use the Gemini API.

## Progress

- [x] Lap-by-lap race time calculator with pit stops, tyre compounds, and multiple stops
- [ ] Real race data from FastF1 (in progress)
- [ ] Monte Carlo simulation for safety cars and other unexpected events
- [ ] Compare a user strategy with the most common real team strategies
- [ ] Website with a Gemini-powered chatbot

## Tech

- Python
- [FastF1](https://docs.fastf1.dev/) for real F1 data
- Gemini API (planned, for the chatbot)

## Getting started

```bash
pip install fastf1
python Simulate.py
```

## Notes

- Results come from a simplified model. They are estimates for comparing strategies, not predictions of real race outcomes.
