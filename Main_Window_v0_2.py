# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow0.2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(434, 150)
        MainWindow.setMinimumSize(QtCore.QSize(434, 150))
        MainWindow.setMaximumSize(QtCore.QSize(800, 400))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self.label_lineDesc = QtWidgets.QLabel(self.centralwidget)
        self.label_lineDesc.setObjectName("label_lineDesc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_lineDesc)
        self.line_toneInput = QtWidgets.QLineEdit(self.centralwidget)
        self.line_toneInput.setMaxLength(12)
        self.line_toneInput.setObjectName("line_toneInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_toneInput)
        self.StatDisplay = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.StatDisplay.setFont(font)
        self.StatDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.StatDisplay.setObjectName("StatDisplay")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.StatDisplay)
        self.PB_transmit = QtWidgets.QPushButton(self.centralwidget)
        self.PB_transmit.setEnabled(False)
        self.PB_transmit.setObjectName("PB_transmit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.PB_transmit)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.actionVer_0_0_0 = QtWidgets.QAction(MainWindow)
        self.actionVer_0_0_0.setObjectName("actionVer_0_0_0")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Base Station Kendali"))
        self.label_lineDesc.setText(_translate("MainWindow", "String Perintah :"))
        self.StatDisplay.setText(_translate("MainWindow", "Stand By"))
        self.PB_transmit.setText(_translate("MainWindow", "Kirim Perintah"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.actionVer_0_0_0.setText(_translate("MainWindow", "Ver 0.0.0"))
