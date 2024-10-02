import sys
from PyQt5.QtWidgets import QApplication
from pronunciation_assessment import PronunciationAssessment

def main():
    app = QApplication(sys.argv)
    window = PronunciationAssessment()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
