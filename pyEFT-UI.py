# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EFT-UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 803)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1051, 721))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.InputData = QtWidgets.QWidget()
        self.InputData.setObjectName("InputData")
        self.checkBox_5 = QtWidgets.QCheckBox(self.InputData)
        self.checkBox_5.setGeometry(QtCore.QRect(360, 30, 121, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_7 = QtWidgets.QCheckBox(self.InputData)
        self.checkBox_7.setGeometry(QtCore.QRect(360, 60, 111, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_10 = QtWidgets.QCheckBox(self.InputData)
        self.checkBox_10.setGeometry(QtCore.QRect(360, 90, 111, 17))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox = QtWidgets.QCheckBox(self.InputData)
        self.checkBox.setGeometry(QtCore.QRect(30, 30, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_6 = QtWidgets.QCheckBox(self.InputData)
        self.checkBox_6.setGeometry(QtCore.QRect(220, 60, 121, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_4 = QtWidgets.QCheckBox(self.InputData)
        self.checkBox_4.setGeometry(QtCore.QRect(120, 60, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.InputData)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 150, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.InputData)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 30, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.InputData)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 60, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.InputData)
        self.comboBox_3.setGeometry(QtCore.QRect(100, 190, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox = QtWidgets.QComboBox(self.InputData)
        self.comboBox.setGeometry(QtCore.QRect(100, 110, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.checkBox_9 = QtWidgets.QCheckBox(self.InputData)
        self.checkBox_9.setGeometry(QtCore.QRect(220, 90, 121, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_8 = QtWidgets.QCheckBox(self.InputData)
        self.checkBox_8.setGeometry(QtCore.QRect(220, 30, 131, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.label = QtWidgets.QLabel(self.InputData)
        self.label.setGeometry(QtCore.QRect(30, 110, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.InputData)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 21, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.InputData)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 81, 21))
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.InputData)
        self.groupBox.setGeometry(QtCore.QRect(210, 10, 281, 231))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(130, 0, 151, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.InputData)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 10, 391, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_16 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_16.setGeometry(QtCore.QRect(190, 30, 181, 21))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_11.setGeometry(QtCore.QRect(10, 90, 171, 16))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_17 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_17.setGeometry(QtCore.QRect(190, 120, 151, 17))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_13.setGeometry(QtCore.QRect(190, 60, 191, 21))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_12.setGeometry(QtCore.QRect(10, 60, 181, 16))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_14.setGeometry(QtCore.QRect(190, 90, 191, 17))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_15.setGeometry(QtCore.QRect(10, 30, 131, 17))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_18 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_18.setGeometry(QtCore.QRect(10, 120, 131, 17))
        self.checkBox_18.setObjectName("checkBox_18")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 180, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(110, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.InputData)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 10, 211, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableWidget = QtWidgets.QTableWidget(self.InputData)
        self.tableWidget.setGeometry(QtCore.QRect(20, 260, 1011, 421))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.checkBox_5.raise_()
        self.checkBox_7.raise_()
        self.checkBox_10.raise_()
        self.checkBox.raise_()
        self.checkBox_6.raise_()
        self.checkBox_4.raise_()
        self.comboBox_2.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.comboBox_3.raise_()
        self.comboBox.raise_()
        self.checkBox_9.raise_()
        self.checkBox_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.tableWidget.raise_()
        self.tabWidget.addTab(self.InputData, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emission Factor Toolkit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.checkBox_5.setText(_translate("MainWindow", "Breakdown by Vehicle"))
        self.checkBox_7.setText(_translate("MainWindow", "Source Apportionment"))
        self.checkBox_10.setText(_translate("MainWindow", "PM by Source"))
        self.checkBox.setText(_translate("MainWindow", "NOx"))
        self.checkBox_6.setText(_translate("MainWindow", "Emission Rates"))
        self.checkBox_4.setText(_translate("MainWindow", "PM2.5"))
        self.checkBox_2.setText(_translate("MainWindow", "CO2"))
        self.checkBox_3.setText(_translate("MainWindow", "PM10"))
        self.checkBox_9.setText(_translate("MainWindow", "Annual Link Emissions"))
        self.checkBox_8.setText(_translate("MainWindow", "Air Quality Modelling"))
        self.label.setText(_translate("MainWindow", "Area"))
        self.label_2.setText(_translate("MainWindow", "Year"))
        self.label_3.setText(_translate("MainWindow", "Traffic Format"))
        self.groupBox.setTitle(_translate("MainWindow", "Select Outputs"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Additional Outputs"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Advanced Options"))
        self.checkBox_16.setText(_translate("MainWindow", "NOx Annual Emissions Euro Split"))
        self.checkBox_11.setText(_translate("MainWindow", "Output % contributions from euro classes"))
        self.checkBox_17.setText(_translate("MainWindow", "Fleet Projection Tool"))
        self.checkBox_13.setText(_translate("MainWindow", "PM10 Annual Emissions Euro Split"))
        self.checkBox_12.setText(_translate("MainWindow", "Simple Entry Euro Compositions"))
        self.checkBox_14.setText(_translate("MainWindow", "PM2.5 Annual Emissions Euro Split"))
        self.checkBox_15.setText(_translate("MainWindow", "Euro Compositions"))
        self.checkBox_18.setText(_translate("MainWindow", "Primary NO2 Fraction"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton.setText(_translate("MainWindow", "Run EFT"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Select Pollutants"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Source ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Road Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Traffic Flow"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "%HDV"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Speed (kph)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "No of Hours"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Link Length (km)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "% Gradient"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Flow Direction"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Load (%)"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InputData), _translate("MainWindow", "Input Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

