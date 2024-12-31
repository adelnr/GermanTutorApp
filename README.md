# German-English Vocabulary Quiz App

This is a Flask-based web application designed to help users practice translating German words into English. The app loads vocabulary from an Excel file, quizzes the user with random words, and provides feedback on their answers.

## Features

- **Vocabulary Loading**: Loads German-English word pairs from an Excel file.
- **Random Quiz**: Asks the user to translate a randomly selected German word into English.
- **Voice Feedback**: Uses text-to-speech (gTTS) to provide audio feedback for correct and incorrect answers.
- **Score Tracking**: Keeps track of the user's score as they answer questions.
- **File Upload**: Allows users to upload their own Excel files with vocabulary.

## Technologies Used

- **Python**: The backend logic is written in Python.
- **Flask**: A lightweight web framework for handling HTTP requests and rendering templates.
- **gTTS**: Google Text-to-Speech for generating audio feedback.
- **Pandas**: For reading and processing Excel files.
- **SpeechRecognition**: For speech-to-text functionality (not fully implemented in this version).
- **PyGame**: For playing audio files.

## Setup Instructions

### Prerequisites

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Pip**: Python's package manager.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Create a virtual environment (optional but recommended):

bash
Copy
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy
pip install -r requirements.txt
Run the application:

bash
Copy
python app.py
Access the app:
Open your browser and go to http://127.0.0.1:5000.

File Format
The app expects an Excel file (xlsx) with two columns:

German: The German word or phrase.

English: The corresponding English translation.

Example:

German	English
Hallo	Hello
Apfel	Apple
Buch	Book
How to Use
Upload a Vocabulary File:

On the homepage, click "Choose File" and select your Excel file.

Click "Upload" to load the vocabulary.

Start the Quiz:

Click "Next Question" to get a random German word to translate.

Submit Your Answer:

Type your answer in the input field and click "Submit".

The app will provide feedback (both text and audio) on whether your answer was correct.

Track Your Score:

Your score is displayed and updated after each question.

Code Structure
app.py: The main Flask application with routes and logic.

templates/: Contains HTML templates for the web interface.

index.html: The main page for uploading files and starting the quiz.

static/: Stores temporary audio files generated by gTTS.

uploads/: Stores uploaded Excel files.

Future Improvements
Speech Recognition: Allow users to speak their answers instead of typing.

Multiple Choice: Add a multiple-choice quiz mode.

User Accounts: Allow users to save their progress and scores.

Mobile Support: Optimize the app for mobile devices.

Contributing
Contributions are welcome! If you'd like to improve this project, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
