## Pop Quiz Game

Pop Quiz Game is a Python terminal game that tests your knowledge with a series of fun and challenging trivia questions. It runs in the Code Institute mock terminal on Heroku.

The objective is simple: answer as many questions correctly as you can! The game keeps score and gives feedback after each answer, making it both educational and enteratining.

[Here is the live link to my project](https://enigmatic-woodland-20099-e4fbc2133d43.herokuapp.com/)

## How to Play

* The game presents a series of general knowledge questions, one at a time.
* Players type their answers into the terminal.
* Answers are case-insensitive, and the game continues until all questions are answered.
* Players receive feedback after each response: "Correct!" or "Wrong!", along with the correct answer.
* After the final question, the total score is displayed.
* The game asks whether you'd like to play again, allowing for endless fun and learning.

## Features

### Question and Answer Game Loop
* A list of predefined trivia questions from topics like geography, pop culture, and politics.

### Case-Insensitive Validation
* User answers are converted to lowercase before comparison, making the game more forgiving and user-friendly.

### Score Tracking
* The game keeps track of correct answers and shows the final score at the end of each round.

### Replay Option
* After each quiz round, the player can choose to play again or exit the game.

### Input Validation
* Prevents empty inputs by asking the player to enter a valid response.

## Data Model

The quiz is built using a simple data model:
* Question List: A list of dictionaries containing question and answer pairs.
* The quiz uses basic string comparison for answer checking after stripping and converting input to lowercase.

## Testing

The game has been manually tested to ensure:
* All questions display and accept input correctly.
Score calculation is accurate.
* Replay loop works as intended.
* Empty inputs are rejected and re-prompted.
* The game runs successfully on local terminals and the Code Institute Heroku terminal.

## Bugs

Solved Bugs
* Replay logic improvement: Added lowercasing and whitespace stripping to handle various user inputs like " Yes " or "Y".

Remaining Bugs
* No known bugs at the time of writing

## Validator Testing
* Code passed through a Python linter (PEP8) with no major issues.
* Input handling has been manually tested with edge cases like whitespace and different casings.

## Deployment 

This game can be deployed using Code Institute’s mock terminal for Heroku or run locally.

To Deploy:
1. Fork or clone this repository
2. Create a new Heroku app
3. Set the buildbacks to Python and NodeJS in that order
4. Link the Heroku app to the repository
5. Click on Deploy

## Credits 
* Code Institute for the deployment terminal

