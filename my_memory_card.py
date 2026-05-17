from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox 
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
text = QLabel('Какой национальности не существует?')

RadioGroupBox = QGroupBox('Варианты ответа')

rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')


# RadioGroupBox.hide()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(answers)

def ask(q: Question):
    shuffle(answers)
    answers[0].text = q.right_answer
    answers[1].text = q.wrong1
    answers[2].text = q.wrong2
    answers[3].text = q.wrong3
    text.setText(q.question)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout() 



layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

button = QPushButton('Ответить')

AnserGroupBox = QGroupBox('Варианты ответа')


layout_main = QVBoxLayout()
text = QLabel('Какой национальности не существует?')
layout_main.addWidget(text)
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(AnserGroupBox)
AnserGroupBox.hide()
layout_main.addWidget(button)

####################################################################
def show_question(q: Question):
        RadioGroupBox.show()
        AnserGroupBox.hide()

def show_result():
        RadioGroupBox.hide()
        AnserGroupBox.show()

def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()


button.clicked.connect(start_test)



l = list()




#####################################################################################

ask(Question('Какой национальности не существует?' , 1 , 2 , 3 , 4))

def test():
    if button.text() == 'Ответить':
        RadioGroupBox.hide()
        AnserGroupBox.show()
    else:
        print('asww')


button.clicked.connect(test)

rbtn_5 = QLabel('1')

layout_ans4 = QHBoxLayout()
layout_ans4.addWidget(rbtn_5)

RadioGroupBox.setLayout(layout_ans4)


main_win.setLayout(layout_main)

main_win.show()
app.exec_()



























#RadioGroupBox = QRadioBox("")



#создай приложение для запоминания информации 