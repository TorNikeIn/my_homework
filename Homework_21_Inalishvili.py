# T&T (Time & Territory) - თამაში ვიქტორინა ორისთვის. თამაში შედგება ორი ნაწილისგან, დროითი და გეოგრაფიული რაუნდებისგან,
# სადაც 12 კითხვაზე პასუხის გაცემის შემდეგ, დაგროვებული ქულების მიხედვით, იმარჯვებს მოთამაშე. თამაშის შესაქმნელად
# გამოყენებულია PyQt5 ბიბლიოთეკა და Python-ის რამდენიმე მოდული(sys, random, ...). კითხვების შესანახად გამოყენებულია
# ცალკე JSON ფაილი, საიდანაც ჩამოიტვირთება შესაბამისი რაუნდის კითხვები და პასუხები.

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import random


# თამაშის პირველი რაუნდის კითხვების და ვიზუალის შესაქმნელი კლასი
class TimeGame:
    pass


# თამაშის მეორე რაუნდის კითხვების და ვიზუალის შესაქმნელი კლასი
class TerritoryGame:
    pass


# თამაშის მსვლელობის და ინტერფეისის შესაქმნელი კლასი
class MainGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.currentQuestion = 0
        self.player1Score = 0
        self.player2Score = 0
        self.questions = self.loadQuestions()

    def initUI(self):
        self.setGeometry(900, 900, 400, 300)
        self.setWindowTitle('Time & Territory')

        self.layout = QVBoxLayout()

        self.questionLabel = QLabel("Question will appear here")
        self.layout.addWidget(self.questionLabel)

        self.player1Answer = QLineEdit(self)
        self.player2Answer = QLineEdit(self)

        self.answerLayout = QHBoxLayout()
        self.answerLayout.addWidget(self.player1Answer)
        self.answerLayout.addWidget(self.player2Answer)
        self.layout.addLayout(self.answerLayout)

        self.submitButton = QPushButton("Submit Answers", self)
        self.submitButton.clicked.connect(self.checkAnswers)
        self.layout.addWidget(self.submitButton)

        self.setLayout(self.layout)

    def loadQuestions(self):
        return []

    def displayQuestion(self):
        pass

    def checkAnswers(self):
        pass

    def showResult(self):
        pass

    def calculateScore(self, playerAnswer, correctAnswer):
        return abs(correctAnswer - playerAnswer)

def main():
    app = QApplication(sys.argv)
    quiz = MainGame()
    quiz.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()