from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import calModel

class side1(QtWidgets.QMainWindow):
    def __init__(self):
        super(side1,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 510)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 40, 381, 91))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(460, 90, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 40, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(50, 170, 531, 271))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.plainTextEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def search(self):
        name = ''
        try:
            name = self.plainTextEdit.toPlainText()
        except:
            pass
        finally:
            output = calModel.search_by_steelgrade(name)
            self.textBrowser.setText(output)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plainTextEdit.setPlaceholderText(_translate("Form", "请输入钢种代号"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "重新输入"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = side1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
