# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import calModel

# css样式
class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class side2(QtWidgets.QMainWindow):
    def __init__(self):
        super(side2, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 775)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 0, 461, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 81, 51))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 90, 111, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 100, 72, 15))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 90, 81, 51))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(250, 90, 111, 41))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(420, 80, 81, 51))
        self.label_5.setObjectName("label_5")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(450, 90, 111, 41))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(430, 120, 72, 15))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(70, 160, 111, 41))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 160, 72, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(220, 160, 81, 51))
        self.label_9.setObjectName("label_9")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(250, 160, 111, 41))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(220, 170, 72, 15))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(420, 160, 81, 51))
        self.label_11.setObjectName("label_11")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(450, 160, 111, 41))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(420, 170, 72, 15))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(40, 230, 81, 51))
        self.label_13.setObjectName("label_13")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(70, 230, 111, 41))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(40, 240, 72, 15))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(220, 230, 81, 51))
        self.label_15.setObjectName("label_15")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(250, 230, 111, 41))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(220, 224, 72, 31))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(420, 230, 81, 51))
        self.label_17.setObjectName("label_17")
        self.plainTextEdit_9 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_9.setGeometry(QtCore.QRect(450, 230, 111, 41))
        self.plainTextEdit_9.setObjectName("plainTextEdit_9")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(420, 240, 72, 15))
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(40, 300, 81, 51))
        self.label_19.setObjectName("label_19")
        self.plainTextEdit_10 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_10.setGeometry(QtCore.QRect(70, 300, 111, 41))
        self.plainTextEdit_10.setObjectName("plainTextEdit_10")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(40, 310, 72, 15))
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(230, 300, 81, 51))
        self.label_21.setObjectName("label_21")
        self.plainTextEdit_11 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_11.setGeometry(QtCore.QRect(260, 300, 111, 41))
        self.plainTextEdit_11.setObjectName("plainTextEdit_11")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(230, 310, 72, 15))
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(420, 300, 81, 51))
        self.label_23.setObjectName("label_23")
        self.plainTextEdit_12 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_12.setGeometry(QtCore.QRect(450, 300, 111, 41))
        self.plainTextEdit_12.setObjectName("plainTextEdit_12")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(420, 310, 72, 15))
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(40, 380, 81, 51))
        self.label_25.setObjectName("label_25")
        self.plainTextEdit_13 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_13.setGeometry(QtCore.QRect(70, 380, 111, 41))
        self.plainTextEdit_13.setObjectName("plainTextEdit_13")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(40, 390, 72, 15))
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(230, 370, 81, 51))
        self.label_27.setObjectName("label_27")
        self.plainTextEdit_14 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_14.setGeometry(QtCore.QRect(260, 370, 111, 41))
        self.plainTextEdit_14.setObjectName("plainTextEdit_14")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(230, 380, 72, 15))
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(620, 140, 111, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 250, 111, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.qTable = QtWidgets.QTableView(Form)
        self.qTable.setGeometry(QtCore.QRect(40, 450, 681, 261))
        self.qTable.setObjectName("qTable")

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(440, 350, 371, 81))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.plainTextEdit.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_2.clear)
        self.pushButton_2.clicked['bool'].connect(self.plainTextEdit_3.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_4.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_5.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_6.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_7.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_8.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_9.clear)
        self.pushButton_2.clicked['bool'].connect(self.plainTextEdit_10.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_11.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_12.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_13.clear)
        self.pushButton_2.clicked['bool'].connect(self.plainTextEdit_14.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def search(self):
        c = 0; si = 0; mn = 0; p = 0; s = 0; cu = 0; ass = 0; sn = 0
        nb = 0; v = 0; al = 0; b = 0; ni = 0; cr = 0
        
        c = self.plainTextEdit.toPlainText()
        if c=='':
            c = 0
        else:
            c= float(c)
        si = self.plainTextEdit_2.toPlainText()
        if si=='':
            si = 0
        else:
            si = float(si)
        mn = self.plainTextEdit_3.toPlainText()
        if mn =='':
            mn = 0
        else:
            mn = float(mn)
        p = self.plainTextEdit_4.toPlainText()
        if p =='':
            p = 0
        else:
            p= float(p)
        s = self.plainTextEdit_5.toPlainText()
        if s=='':
            s = 0
        else:
            s= float(s)
        cu = self.plainTextEdit_6.toPlainText()
        if cu =='':
            cu = 0
        else:
            cu = float(cu)
        ass = self.plainTextEdit_7.toPlainText()
        if ass=='':
            ass = 0
        else:
            ass = float(ass)
        sn = self.plainTextEdit_8.toPlainText()
        if sn =='':
            sn = 0
        else:
            sn = float(sn)
        nb = self.plainTextEdit_9.toPlainText()
        if nb =='':
            nb = 0
        else:
            nb = float(nb)
        v = self.plainTextEdit_10.toPlainText()
        if v =='':
            v = 0
        else:
            v= float(v)
        al = self.plainTextEdit_11.toPlainText()
        if al=='':
            al = 0
        else:
            al= float(al)
        b = self.plainTextEdit_12.toPlainText()
        if b=='':
            b = 0
        else:
            b= float(b)
        ni = self.plainTextEdit_13.toPlainText()
        if ni=='':
            ni = 0
        else:
            ni= float(ni)
        cr = self.plainTextEdit_14.toPlainText()
        if cr=='':
            cr = 0
        else:
            cr= float(cr)
        element_name = ['c','si','mn','p','s','cu','ass','sn','nb','v','al','b','ni','cr']
        element_judge = []
        for element in element_name:
            if eval(element) !=0:
                element_judge.append(element)
        df = pd.read_excel(r'data4.xls')
        st_name = []
        class_name_1 = []
        class_name_2 = []
        for n in range(len(df)):
            sum =0
            for element in element_judge:

                element_min = df.iloc[n][element+"_min"]
                element_max = df.iloc[n][element+"_max"]
                if (eval(element) >=element_min) and (eval(element) <= element_max):
                    sum += 1
                        
                if sum == len(element_judge):
                    st_name.append(df.iloc[n]['st_no'])
                    class_name_1.append(df.iloc[n]['tag'])
                    class_name_2.append(df.iloc[n]['2nd_tag'])
        result_dict={}
        result_dict["符合要求的钢种代码"]= st_name
        result_dict["对应的钢种代号01"] = class_name_1
        result_dict["对应的钢种代号02"] = class_name_2
        output = pd.DataFrame(result_dict)

        try:
            model = pandasModel(output)
            self.qTable.setModel(model)
        except:
            print("未找到匹配钢种")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">请输入钢种成分（将百分比转化为小数点）</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">C</span></p></body></html>"))
        self.label_4.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Si</span></p></body></html>"))
        self.label_5.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Mn</span></p></body></html>"))
        self.label_8.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">P</span></p></body></html>"))
        self.label_9.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">S</span></p></body></html>"))
        self.label_11.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Cu</span></p></body></html>"))
        self.label_13.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">As</span></p></body></html>"))
        self.label_15.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Sn</span></p></body></html>"))
        self.label_17.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Nb</span></p></body></html>"))
        self.label_19.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">V</span></p></body></html>"))
        self.label_21.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Al</span></p></body></html>"))
        self.label_23.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">B</span></p></body></html>"))
        self.label_25.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Ni</span></p></body></html>"))
        self.label_27.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Cr</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "一键清空"))
        self.label_7.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">若某一元素值为0，请手动输入0</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = side2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
