# ✍️ Quiz Web App

This is a responsive quiz application built using HTML, CSS, and JavaScript. It allows users to enter their name, take a quiz of 5 questions, and view their rank in the leaderboard based on their score.

## 🔗 Live Website
Visit the live site here:  [![quiz](https://img.shields.io/badge/-Vercel-000f10?style=flat&logo=vercel&logoColor=white)](https://quiz-app-xi-mocha.vercel.app/)


## Features
- Enter name to start quiz
- Answer 5 multiple-choice questions
- Score tracking and progress bar
- Leaderboard with top 5 achievers
- Data stored using localStorage
- Responsive UI with green theme


## Project Structure
```
Multi Page App/
├── index.html
├── play.html
├── achievers.html
├── style.css
├── play.js
└── README.md
```

## How It Works
1. Open `index.html` to see the home page.
2. Click **Play** to go to `play.html`.
3. Enter your name and start the quiz.
4. After completing 5 questions, your score is stored with your name.
5. You are redirected to `achievers.html` where the top 5 scorers are shown.
6. Use the **Go Home** button to return to the main page.


## Data Storage
- User data is stored in `localStorage` under the key: `topAchievers`.
- It persists across page reloads but is specific to your browser.


## Technologies Used
- HTML5
- CSS3
- JavaScript (ES6)
- Web Storage API


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/snehs19space/100_Projects/blob/main/LICENSE) file for details.
