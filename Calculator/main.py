from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from decimal import *
class Calculator(QMainWindow):
    def __init__(self):
            super().__init__()
            loader = QUiLoader()
            self.ui = loader.load('calc.ui',None)
            self.ui.show()

            self.old_operator = ""
            self.old_val = 0
            self.append_mode = False

            self.ui.btn_0.clicked.connect(lambda: self.append(self.ui.btn_0.text()))
            self.ui.btn_1.clicked.connect(lambda: self.append(self.ui.btn_1.text()))
            self.ui.btn_2.clicked.connect(lambda: self.append(self.ui.btn_2.text()))
            self.ui.btn_3.clicked.connect(lambda: self.append(self.ui.btn_3.text()))
            self.ui.btn_4.clicked.connect(lambda: self.append(self.ui.btn_4.text()))
            self.ui.btn_5.clicked.connect(lambda: self.append(self.ui.btn_5.text()))
            self.ui.btn_6.clicked.connect(lambda: self.append(self.ui.btn_6.text()))
            self.ui.btn_7.clicked.connect(lambda: self.append(self.ui.btn_7.text()))
            self.ui.btn_8.clicked.connect(lambda: self.append(self.ui.btn_8.text()))
            self.ui.btn_9.clicked.connect(lambda: self.append(self.ui.btn_9.text()))

            self.ui.btn_plus.clicked.connect(lambda: self.operate(self.ui.btn_plus.text()))
            self.ui.btn_minus.clicked.connect(lambda: self.operate(self.ui.btn_minus.text()))
            self.ui.btn_mul.clicked.connect(lambda: self.operate(self.ui.btn_mul.text()))
            self.ui.btn_div.clicked.connect(lambda: self.operate(self.ui.btn_div.text()))

            self.ui.btn_dot.clicked.connect(self.add_dot)

            self.ui.btn_ce.clicked.connect(lambda: self.ce())
            self.ui.btn_c.clicked.connect(lambda: self.reset())
            self.ui.btn_back.clicked.connect(lambda: self.back())

            self.ui.btn_equal.clicked.connect(lambda: self.equal())

            self.ui.btn_sign.clicked.connect(self.toggle_sign)
    
    def append(self,txt):
        current_text = self.ui.txt_result.text()
        if(current_text == '0' or not self.append_mode):
            if(current_text == '0' and txt == '.'):
                self.ui.txt_result.setText("0.")
            else:
                self.ui.txt_result.setText(txt)
        else:
            self.ui.txt_result.setText(current_text + txt)
        self.append_mode = True
    def add_dot(self):
        if('.' in self.ui.txt_result.text()):
            return
        self.append('.')

    def ce(self):
        self.ui.txt_result.setText('0')

    def reset(self):
        self.old_operator = ""
        self.old_val = 0
        self.append_mode = True
        self.ui.txt_result.setText('0')

    def back(self):
        current_text = self.ui.txt_result.text()
        if(len(current_text) == 1):
            if(current_text != '0'):
                self.ui.txt_result.setText('0')
        else:
            txt = current_text[:len(current_text)-1]
            self.ui.txt_result.setText(txt)

    def toggle_sign(self):
        current_text = Decimal(self.ui.txt_result.text())
        current_text *= -1
        self.ui.txt_result.setText(str(current_text))

    def operate(self, operator):
        if(self.old_operator == ""):
            self.old_operator = operator
            self.old_val = Decimal(self.ui.txt_result.text()) 
        else:
            new_val = Decimal(self.ui.txt_result.text())
            if(self.old_operator == "+"):
                result = self.old_val + new_val
            elif(self.old_operator == "-"):
                result = self.old_val - new_val
            elif(self.old_operator == "×"):
                result = self.old_val * new_val
            elif(self.old_operator == "÷"):
                if(new_val == 0):
                    result = 'Infinity'
                    self.ui.txt_result.setText(result)
                    self.old_operator = ""
                    self.old_val = 0
                    self.append_mode = False
                else:
                    result = self.old_val / new_val
            self.ui.txt_result.setText(str(result))
            self.old_val = Decimal(str(result))
            self.old_operator = operator
        self.append_mode = False

    def equal(self):
        self.operate('')
        self.old_operator = ""
        self.old_val = 0
        self.append_mode = False

app = QApplication([])
window = Calculator()
app.exec()