# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

1. The updates to history in the Developer's Debug Info were stale.
2. The logic for checking the guess were reversed, guess > secret, it says GO HIGHER and guess < secret it says GO LOWER. It should be the other way around.
3. New game doesn't reset the attempts and doesn't refresh the history in the Info tab.
4. Attempts for each mode in the Info tab are not displayes correctly.
5. Range for 1 to 100 is not being validated.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 40 |"Too high" hint |"Too low" hint shown | None|  |
| guess of 101 | "Error number should be between 1 and 100" | "Go HIGHER" | None |
| | | | |

No range validation
Stale updates to history
Broken hints
New game doesn't refresh the history and doesn't reset the attempts
Attempts in the developer view are not correct when refreshed


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used Claude Code to find the bugs in the code and made changes to the code based on the suggestions. 

- When the user enters a guess, the developer info does not show the latest guess but only appears in the next iteration. Claude identified the issue that since the Developer Info widgets were being rendered before the game logic, the data was stale. It suggested me to move the developer info part to be rendered after the game logic or add a st.rerun() after the game logic to force the update to the developer info.

- An example where the Claude's suggestion was correct is the logic switch when the guess was too high or too low. Another one was the suggestion to fix the stale history was a partial win. When I tried the fix to add a rerun, it would erase the hint and if I used the fix to move the widget after the game logic, the dropdown would collapse. 


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I first understood what needs to happen when an operation is performed. If the outcome is as expected and is logically correct, I knew that it was fixed.

- I ran pytest on tests/test_game_logic.py after refactoring the logic into logic_utils.py. The first run failed with ModuleNotFoundError because pytest could not find logic_utils from the tests/ subfolder. Adding a conftest.py at the project root fixed the import, and the tests then passed. This showed me that test infrastructure issues can look like code bugs at first glance, and that the project structure matters as much as the test logic itself.

- Yes, Claude Code helped design the tests. I asked it to write complete tests with edge cases for all four functions in logic_utils.py. It caught that the existing three tests were already broken because they compared check_guess's result to a plain string like "Win" when the function actually returns a tuple like ("Win", "🎉 Correct!"). It also added edge cases I would not have thought of, like passing None, a float string, and a number outside the difficulty range to parse_guess.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you interact with a Streamlit app — clicking a button, typing in a box — Streamlit reruns the entire Python script from top to bottom. It does not remember any regular variables from the previous run; they reset to their initial values. Session state is a special dictionary (st.session_state) that survives across those reruns, so anything you want to persist — like the secret number, the score, or the guess history — has to live there. I learned this the hard way when the debug panel showed stale history: the panel rendered at the top of the script before the submit logic ran at the bottom, so in the same rerun the panel always saw the old state. Moving the panel below the submit block fixed it because by then the session state had already been updated in that same pass.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


- I always used to give a prompt to AI and use the code directly without verifying it. I would like to ask AI to write tests and verify.

- Instead of letting the AI do all the fixes and hoping it fixed the issue, I learned to actually test and verify that the changes were made as per instructions and guide the AI properly to avoid introducing new unwanted bugs.

- I now know that AI can be a blessing and a curse. Sometimes it shows us bugs that we missed and fixes them. In the process it might introduce new bugs. So I learned that when working with code, always and always verify yourself and be familiar with what is happening in the code.