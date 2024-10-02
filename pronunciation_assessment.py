import difflib
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from speech_recognition_module import speech_to_text
from styles import Styles

# Function to compare pronunciation
def pronunciation_comparison(correct_text, user_text):
    """Compares user's spoken word or sentence against the correct version."""
    if correct_text == user_text:
        return True

    sequence_matcher = difflib.SequenceMatcher(None, correct_text, user_text)
    ratio = sequence_matcher.quick_ratio()
    return ratio >= 0.8

# Pronunciation Assessment class
class PronunciationAssessment(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pronunciation Assessment")
        self.setGeometry(200, 200, 500, 600)
        self.setStyleSheet("background-color: #282a36;")  # Dark background color

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Title label
        self.title_label = QLabel("Pronunciation Practice")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ff79c6; margin: 20px;")  # Soft pink color
        self.layout.addWidget(self.title_label)

        # Input field for the correct pronunciation
        self.correct_text_label = QLabel("Enter Correct Pronunciation:")
        self.correct_text_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #8be9fd;")  # Light blue color
        self.correct_text_input = QLineEdit()
        self.correct_text_input.setStyleSheet(Styles.input_style)

        self.layout.addWidget(self.correct_text_label)
        self.layout.addWidget(self.correct_text_input)

        # Speak button
        self.speak_button = QPushButton("Speak")
        self.speak_button.setStyleSheet(Styles.button_style)
        self.speak_button.clicked.connect(self.handle_speak_button)
        self.layout.addWidget(self.speak_button)

        # Feedback label
        self.feedback_label = QLabel("")
        self.feedback_label.setAlignment(Qt.AlignCenter)
        self.feedback_label.setStyleSheet("font-size: 18px; color: #f1fa8c; margin-top: 20px;")  # Soft yellow color
        self.layout.addWidget(self.feedback_label)

    def handle_speak_button(self):
        """Handles the logic for the 'Speak' button."""
        correct_text = self.correct_text_input.text().strip().lower()
        if not correct_text:
            self.feedback_label.setText("Please enter a correct pronunciation.")
            return

        user_text = speech_to_text()
        if user_text is not None:
            # Display recognized text
            self.feedback_label.setText(f"Recognized text: {user_text}")
            
            # Compare pronunciation
            is_correct = pronunciation_comparison(correct_text, user_text)
            if is_correct:
                self.feedback_label.setText("Correct Pronunciation!")
            else:
                self.feedback_label.setText(f"Incorrect Pronunciation. Practice: {correct_text}")
        else:
            self.feedback_label.setText("Could not recognize speech. Try again.")
