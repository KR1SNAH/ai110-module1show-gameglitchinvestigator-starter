# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Sample game on **Normal** difficulty (range 1–100, 8 attempts allowed):

1. App loads. The info bar shows "Attempts left: 8". Developer Debug Info checkbox is unchecked by default.
2. User opens the Developer Debug Info panel — secret number is revealed as **54** (for demo purposes).
3. User types **40** and clicks Submit Guess. Game returns "📉 Go HIGHER!" and score drops by 5 (score: -5).
4. User types **70** and clicks Submit Guess. Game returns "📉 Go LOWER!" and score drops by 5 again (score: -10). Attempts left updates to 6.
5. User types **110** and clicks Submit Guess. Game shows an error: "Please enter a number between 1 and 100." No attempt is counted, history is unchanged.
6. User types **abc** and clicks Submit Guess. Game shows "That is not a number." No attempt counted, nothing added to history.
7. User types **54** and clicks Submit Guess. Game returns "🎉 Correct!" with balloons. Win bonus is added to score (100 - 10 × 3 = 70, final score: 60).
8. Game status locks to "won". Submit is blocked and the success message reads: "You won! The secret was 54. Final score: 60."
9. User clicks New Game. Attempts reset to 0, score resets to 0, history clears, and a fresh secret number is chosen within the selected difficulty range.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
