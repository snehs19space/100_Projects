const startScreen = document.getElementById('startScreen');
const quizScreen = document.getElementById('quizScreen');
const questionText = document.getElementById('QuestionText');
const choiceTexts = Array.from(document.getElementsByClassName('ChoiceText'));
const progressText = document.getElementById('progressText');
const scoreDisplay = document.getElementById('scorenumber');
const progressBarFull = document.getElementById('progressBarFull');

let currentQuestion = {};
let score = 0;
let questionCounter = 0;
let acceptingAnswers = false;
let userName = "";

let questions = [
  {
    question: "What is the capital of France?",
    choices: ["Paris", "London", "Rome"],
    answer: 1
  },
  {
    question: "Which planet is known as the Red Planet?",
    choices: ["Earth", "Mars", "Jupiter"],
    answer: 2
  },
  {
    question: "What is 5 x 6?",
    choices: ["30", "11", "56"],
    answer: 1
  },
  {
    question: "Which language runs in a web browser?",
    choices: ["Java", "C", "JavaScript"],
    answer: 3
  },
  {
    question: "Which ocean is the largest?",
    choices: ["Atlantic", "Pacific", "Indian"],
    answer: 2
  }
];

let availableQuestions = [];

function startQuiz() {
  const inputName = document.getElementById('username').value.trim();
  if (!inputName) {
    alert("Please enter your name.");
    return;
  }

  userName = inputName;

  startScreen.style.display = 'none';
  quizScreen.style.display = 'block';

  questionCounter = 0;
  score = 0;
  availableQuestions = [...questions];
  getNewQuestion();
}

function getNewQuestion() {
  if (availableQuestions.length === 0 || questionCounter >= 5) {
    saveTopAchiever(userName, score);
    alert(`Quiz Over!\n${userName}, your score is ${score}`);
    window.location.href = "achievers.html";
    return;
  }

  questionCounter++;
  progressText.innerText = `Question ${questionCounter} of 5`;
  progressBarFull.style.width = `${(questionCounter / 5) * 100}%`;

  const questionIndex = Math.floor(Math.random() * availableQuestions.length);
  currentQuestion = availableQuestions[questionIndex];
  questionText.innerText = currentQuestion.question;

  choiceTexts.forEach((choice, index) => {
    choice.innerText = currentQuestion.choices[index];
    choice.dataset.number = index + 1;
  });

  availableQuestions.splice(questionIndex, 1);
  acceptingAnswers = true;
}

choiceTexts.forEach(choice => {
  choice.addEventListener('click', e => {
    if (!acceptingAnswers) return;

    acceptingAnswers = false;
    const selected = e.target;
    const selectedAnswer = parseInt(selected.dataset.number);

    if (selectedAnswer === currentQuestion.answer) {
      score += 10;
    }

    scoreDisplay.innerText = score;

    setTimeout(() => {
      getNewQuestion();
    }, 500);
  });
});

function saveTopAchiever(name, score) {
  const achievers = JSON.parse(localStorage.getItem('topAchievers')) || [];
  achievers.push({ name, score });
  localStorage.setItem('topAchievers', JSON.stringify(achievers));
}
