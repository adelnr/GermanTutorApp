import time
from flask import Flask, request, render_template, jsonify, send_from_directory
import os
import random
from gtts import gTTS
from pygame import mixer
import pandas as pd
import speech_recognition as sr

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

# Ensure the upload and static folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('static', exist_ok=True)

# Initialize the mixer for playing audio
mixer.init()

# Global variables
vocabulary = {}
user_score = 0

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def load_vocabulary(file_path):
    try:
        df = pd.read_excel(file_path)
        print("Vocabulary loaded successfully:", df.to_dict())  # Debugging line
        return dict(zip(df['German'], df['English']))
    except Exception as e:
        print(f"Error loading vocabulary: {e}")  # Debugging line
        return {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        global vocabulary
        vocabulary = load_vocabulary(file_path)
        if not vocabulary:
            return jsonify({"error": "Failed to load vocabulary. Check the file format."}), 400
        return jsonify({"message": "File uploaded successfully"}), 200
    return jsonify({"error": "File type not allowed"}), 400

@app.route('/next_question')
def next_question():
    if not vocabulary:
        return jsonify({"error": "No vocabulary found"}), 404
    try:
        word = random.choice(list(vocabulary.keys()))
        question_text = f"Was ist die englische Übersetzung von '{word}'?"
        tts = gTTS(text=question_text, lang='de')
        timestamp = int(time.time())  # Add a timestamp to the filename
        audio_filename = f"static/temp_{timestamp}.mp3"
        tts.save(audio_filename)
        print(f"Generated question: {question_text}")  # Debugging line
        return jsonify({"question": question_text, "word": word, "audio": audio_filename})
    except Exception as e:
        print(f"Error in /next_question: {e}")  # Debugging line
        return jsonify({"error": str(e)}), 500

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data.get('answer', '').strip().lower()
    word = data.get('word', '')
    if not user_answer or not word:
        return jsonify({"error": "Invalid input"}), 400

    correct_answer = vocabulary.get(word, '').lower()
    global user_score

    if user_answer == correct_answer:
        feedback = "Correct! Great job!"
        correct = True
        user_score += 1  # Increment score
    else:
        feedback = f"Incorrect. The correct answer is '{vocabulary[word]}'."
        correct = False

    # Debugging: Print the feedback and correctness
    print(f"Feedback: {feedback}, Correct: {correct}")

    # Generate audio feedback
    try:
        tts = gTTS(text=feedback, lang='en')
        timestamp = int(time.time())  # Add a timestamp to the filename
        audio_filename = f"static/feedback_{timestamp}.mp3"
        tts.save(audio_filename)
        print(f"Generated feedback audio: {audio_filename}")  # Debugging line
    except Exception as e:
        print(f"Error generating feedback audio: {e}")  # Debugging line
        return jsonify({"error": "Failed to generate feedback audio"}), 500

    return jsonify({
        "feedback": feedback,
        "correct": correct,
        "audio": audio_filename,
        "score": user_score
    })
@app.route('/static/<filename>')
def serve_static(filename):
    response = send_from_directory('static', filename)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True)