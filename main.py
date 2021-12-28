import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtGui

class Appdemo(QWidget):
    def __init__(self):
        super(Appdemo, self).__init__()
        uic.loadUi('app.ui',self)
        self.setWindowIcon(QtGui.QIcon('calc.png'))
        self.setWindowTitle("Calculator")
        self.pushButton_eql.clicked.connect(self.pressedeql)
        self.pushButton_00.clicked.connect(self.pressed0)
        self.pushButton_01.clicked.connect(self.pressed1)
        self.pushButton_02.clicked.connect(self.pressed2)
        self.pushButton_03.clicked.connect(self.pressed3)
        self.pushButton_04.clicked.connect(self.pressed4)
        self.pushButton_05.clicked.connect(self.pressed5)
        self.pushButton_06.clicked.connect(self.pressed6)
        self.pushButton_07.clicked.connect(self.pressed7)
        self.pushButton_08.clicked.connect(self.pressed8)
        self.pushButton_09.clicked.connect(self.pressed9)
        self.pushButton_dot.clicked.connect(self.presseddot)
        self.pushButton_clr.clicked.connect(self.pressedclr)
        self.pushButton_div.clicked.connect(self.presseddiv)
        self.pushButton_mul.clicked.connect(self.pressedmul)
        self.pushButton_sub.clicked.connect(self.pressedsub)
        self.pushButton_add.clicked.connect(self.pressedadd)
        self.pushButton_del.clicked.connect(self.presseddel)

    def presseddiv(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "/")

    def pressedmul(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "*")

    def pressedsub(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "-")

    def pressedadd(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "+")

    def pressedeql(self):
        equation = self.lineEdit.text()
        try:
            ans = eval(equation)
            self.lineEdit.setText(str(ans))
        except:
            self.lineEdit.setText("Please Enter Valid Expression !")

    def presseddot(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + ".")

    def pressed0(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "0")

    def pressed1(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "1")

    def pressed2(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "2")

    def pressed3(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "3")

    def pressed4(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "4")

    def pressed5(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "5")

    def pressed6(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "6")

    def pressed7(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "7")

    def pressed8(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "8")

    def pressed9(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a + "9")

    def presseddel(self):
        a = self.lineEdit.text()
        a = a[:-1]
        self.lineEdit.setText(a)

    def pressedclr(self):
        self.lineEdit.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Appdemo()
    demo.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')