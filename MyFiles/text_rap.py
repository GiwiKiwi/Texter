import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QDesktopWidget, QLabel, QLineEdit, QTextEdit, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont



class NextTrainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(750, 450)
        self.center()
        self.setWindowTitle('Упражнение вставочного типа')
        self.setWindowIcon(QIcon('EnglishTest.jpg'))

        Task1Label = QLabel('1. Use the vebs in brackets to complete the sentences. Pay attention: some of them are questions.', self)
        Task1Label.resize(650, 75)
        Task1Label.move(50, 20)
        Task1Label.setFont(QFont('SansSerif', 11))

        Task1Line = QTextEdit(self)
        Task1Line.resize(650, 100)
        Task1Line.move(50, 80)
        Task1Line.setFont(QFont('SansSerif', 12))
        
        AnswerLabel = QLabel('Wrong! Правильный ответ: is she studding', self)
        AnswerLabel.resize(500, 50)
        AnswerLabel.move(50, 190)
        AnswerLabel.setFont(QFont('SansSerif', 11))

        AnswerLine = QTextEdit(self)
        AnswerLine.resize(650, 100)
        AnswerLine.move(50, 250)
        AnswerLine.setFont(QFont('SansSerif', 12))
        
        NextTrainNextButton = QPushButton('Далее', self)
        NextTrainNextButton.resize(100, 50)
        NextTrainNextButton.move(500, 360)
        NextTrainNextButton.setFont(QFont('SansSerif', 16))

        NextTrainExitButton = QPushButton('Exit', self)
        NextTrainExitButton.resize(100, 50)
        NextTrainExitButton.move(620, 360)
        NextTrainExitButton.setFont(QFont('SansSerif', 16))
        NextTrainExitButton.clicked.connect(self.close)

        self.show()

    def center(self):

        Geometry = self.frameGeometry()
        CenterOfDesktop = QDesktopWidget().availableGeometry().center()
        Geometry.moveCenter(CenterOfDesktop)
        self.move(Geometry.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выход из приложения',
            "Вы уверены, что хотите выйти?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            

class TrainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(750, 450)
        self.center()
        self.setWindowTitle('Формы глагола')
        self.setWindowIcon(QIcon('EnglishTest.jpg'))

        TaskLabel = QLabel('Введите три формы глагола. Для продолжения нажмите Enter.', self)
        TaskLabel.resize(650, 75)
        TaskLabel.move(50, 20)
        TaskLabel.setFont(QFont('SansSerif', 16))

        InfinitiveLabel = QLabel('Infinitive', self)
        InfinitiveLabel.resize(150, 75)
        InfinitiveLabel.move(110, 70)
        InfinitiveLabel.setFont(QFont('SansSerif', 14))

        SimpleLabel = QLabel('Past Simple', self)
        SimpleLabel.resize(150, 75)
        SimpleLabel.move(310, 70)
        SimpleLabel.setFont(QFont('SansSerif', 14))

        ParticipleLabel = QLabel('Past Participle', self)
        ParticipleLabel.resize(150, 75)
        ParticipleLabel.move(510, 70)
        ParticipleLabel.setFont(QFont('SansSerif', 14))

        InfinitiveLine = QLineEdit(self)
        InfinitiveLine.resize(180, 30)
        InfinitiveLine.move(60, 130)
        InfinitiveLine.setFont(QFont('SansSerif', 14))

        SimpleLine = QLineEdit(self)
        SimpleLine.resize(180, 30)
        SimpleLine.move(275, 130)
        SimpleLine.setFont(QFont('SansSerif', 14))

        ParticipleLine = QLineEdit(self)
        ParticipleLine.resize(180, 30)
        ParticipleLine.move(480, 130)
        ParticipleLine.setFont(QFont('SansSerif', 14))
        
        TrainNextButton = QPushButton('Далее', self)
        TrainNextButton.resize(100, 50)
        TrainNextButton.move(500, 360)
        TrainNextButton.setFont(QFont('SansSerif', 16))
        TrainNextButton.clicked.connect(self.OpenNextTrainWindow)

        TrainExitButton = QPushButton('Exit', self)
        TrainExitButton.resize(100, 50)
        TrainExitButton.move(620, 360)
        TrainExitButton.setFont(QFont('SansSerif', 16))
        TrainExitButton.clicked.connect(self.close)

        self.show()

    def center(self):

        Geometry = self.frameGeometry()
        CenterOfDesktop = QDesktopWidget().availableGeometry().center()
        Geometry.moveCenter(CenterOfDesktop)
        self.move(Geometry.topLeft())

    def OpenNextTrainWindow(self):

        self.OpenWindow = NextTrainWindow()
        self.OpenWindow.show()
        self.destroy()
        
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выход из приложения',
            "Вы уверены, что хотите выйти?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

            
        
class StartWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(550, 450)
        self.center()
        self.setWindowTitle('Обучение')
        self.setWindowIcon(QIcon('EnglishTest.jpg'))

        TrainButton = QPushButton('Приступить к обучению', self)
        TrainButton.resize(300, 75)
        TrainButton.move(130, 70)
        TrainButton.setFont(QFont('SansSerif', 16))
        TrainButton.clicked.connect(self.OpenTrainWindow)

        TestButton = QPushButton('Приступить к тестированию', self)
        TestButton.resize(300, 75)
        TestButton.move(130, 170)
        TestButton.setFont(QFont('SansSerif', 16))
        
        ExitButton = QPushButton('Закончить сеанс', self)
        ExitButton.resize(300, 75)
        ExitButton.move(130, 270)
        ExitButton.setFont(QFont('SansSerif', 16))
        ExitButton.clicked.connect(self.close)

        self.show()

    def center(self):

        Geometry = self.frameGeometry()
        CenterOfDesktop = QDesktopWidget().availableGeometry().center()
        Geometry.moveCenter(CenterOfDesktop)
        self.move(Geometry.topLeft())

    def OpenTrainWindow(self):

        self.OpenWindow = TrainWindow()
        self.OpenWindow.show()
        self.destroy()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выход из приложения',
            "Вы уверены, что хотите выйти?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        

class EnterWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(550, 250)
        self.center()
        self.setWindowTitle('Вход в тестирование')
        self.setWindowIcon(QIcon('EnglishTest.jpg'))

        NumberLabel = QLabel('Введите номер:', self)
        NumberLabel.resize(250, 75)
        NumberLabel.move(150, 20)
        NumberLabel.setFont(QFont('SansSerif', 16))

        NumberLine = QLineEdit(self)
        NumberLine.resize(250, 40)
        NumberLine.move(150, 80)
        NumberLine.setFont(QFont('SansSerif', 16))
        
        Enter = QPushButton('Войти', self)
        Enter.resize(250, 75)
        Enter.move(150, 140)
        Enter.setFont(QFont('SansSerif', 16))
        Enter.clicked.connect(self.OpenStartWindow)

        self.show()

    def center(self):

        Geometry = self.frameGeometry()
        CenterOfDesktop = QDesktopWidget().availableGeometry().center()
        Geometry.moveCenter(CenterOfDesktop)
        self.move(Geometry.topLeft())

    def OpenStartWindow(self):

        self.OpenWindow = StartWindow()
        self.OpenWindow.show()
        self.destroy()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выход из приложения',
            "Вы уверены, что хотите выйти?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



class RegisterWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(550, 450)
        self.center()
        self.setWindowTitle('Регистрация')
        self.setWindowIcon(QIcon('EnglishTest.jpg'))

        FamilyLabel = QLabel('Введите Фамилию:', self)
        FamilyLabel.resize(250, 75)
        FamilyLabel.move(150, 20)
        FamilyLabel.setFont(QFont('SansSerif', 16))

        FamilyLine = QLineEdit(self)
        FamilyLine.resize(250, 40)
        FamilyLine.move(150, 80)
        FamilyLine.setFont(QFont('SansSerif', 16))

        
        NameLabel = QLabel('Введите Имя:', self)
        NameLabel.resize(250, 75)
        NameLabel.move(150, 120)
        NameLabel.setFont(QFont('SansSerif', 16))

        NameLine = QLineEdit(self)
        NameLine.resize(250, 40)
        NameLine.move(150, 180)
        NameLine.setFont(QFont('SansSerif', 16))
        
        Register = QPushButton('Зарегистрироваться', self)
        Register.resize(250, 75)
        Register.move(150, 300)
        Register.setFont(QFont('SansSerif', 16))

        self.show()

    def center(self):

        Geometry = self.frameGeometry()
        CenterOfDesktop = QDesktopWidget().availableGeometry().center()
        Geometry.moveCenter(CenterOfDesktop)
        self.move(Geometry.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выход из приложения',
            "Вы уверены, что хотите выйти?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.resize(550, 450)
        self.center()
        self.setWindowTitle('Главная')
        self.setWindowIcon(QIcon('EnglishTest.jpg'))

        MainEnter = QPushButton('ВХОД', self)
        MainEnter.resize(250, 75)
        MainEnter.move(150, 120)
        MainEnter.setFont(QFont('SansSerif', 16))
        MainEnter.clicked.connect(self.OpenEnterWindow)

        MainRegister = QPushButton('Регистрация', self)
        MainRegister.resize(250, 75)
        MainRegister.move(150, 220)
        MainRegister.setFont(QFont('SansSerif', 16))
        MainRegister.clicked.connect(self.OpenRegisterWindow)

        self.show()

    def center(self):

        Geometry = self.frameGeometry()
        CenterOfDesktop = QDesktopWidget().availableGeometry().center()
        Geometry.moveCenter(CenterOfDesktop)
        self.move(Geometry.topLeft())

    def OpenRegisterWindow(self):

        self.OpenWindow = RegisterWindow()
        self.OpenWindow.show()

    def OpenEnterWindow(self):
        
        self.OpenWindow = EnterWindow()
        self.OpenWindow.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выход из приложения',
            "Вы уверены, что хотите выйти?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
 


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()

    sys.exit(app.exec_())
