# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EFT-UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 803)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Tab_main = QtWidgets.QTabWidget(self.centralwidget)
        self.Tab_main.setGeometry(QtCore.QRect(10, 10, 1091, 721))
        self.Tab_main.setObjectName("Tab_main")
        self.QA_tab = QtWidgets.QWidget()
        self.QA_tab.setObjectName("QA_tab")
        self.Tab_main.addTab(self.QA_tab, "")
        self.InputData_tab = QtWidgets.QWidget()
        self.InputData_tab.setObjectName("InputData_tab")
        self.Breakdown_by_vehicle_checkbox = QtWidgets.QCheckBox(self.InputData_tab)
        self.Breakdown_by_vehicle_checkbox.setGeometry(QtCore.QRect(360, 30, 121, 17))
        self.Breakdown_by_vehicle_checkbox.setObjectName("Breakdown_by_vehicle_checkbox")
        self.Source_apportionment_checkbox = QtWidgets.QCheckBox(self.InputData_tab)
        self.Source_apportionment_checkbox.setGeometry(QtCore.QRect(360, 60, 141, 17))
        self.Source_apportionment_checkbox.setObjectName("Source_apportionment_checkbox")
        self.PM_by_source_checkbox = QtWidgets.QCheckBox(self.InputData_tab)
        self.PM_by_source_checkbox.setGeometry(QtCore.QRect(360, 90, 111, 17))
        self.PM_by_source_checkbox.setObjectName("PM_by_source_checkbox")
        self.NOx_checkbox = QtWidgets.QCheckBox(self.InputData_tab)
        self.NOx_checkbox.setGeometry(QtCore.QRect(30, 30, 70, 17))
        self.NOx_checkbox.setObjectName("NOx_checkbox")
        self.Emission_rates_checkbox = QtWidgets.QCheckBox(self.InputData_tab)
        self.Emission_rates_checkbox.setGeometry(QtCore.QRect(220, 60, 121, 17))
        self.Emission_rates_checkbox.setObjectName("Emission_rates_checkbox")
        self.PM25_checkbox = QtWidgets.QCheckBox(self.InputData_tab)
        self.PM25_checkbox.setGeometry(QtCore.QRect(120, 60, 70, 17))
        self.PM25_checkbox.setObjectName("PM25_checkbox")
        self.Year_dropdown = QtWidgets.QComboBox(self.InputData_tab)
        self.Year_dropdown.setGeometry(QtCore.QRect(100, 150, 69, 22))
        self.Year_dropdown.setObjectName("Year_dropdown")
        self.CO2_checkbox = QtWidgets.QCheckBox(self.InputData_tab)
        self.CO2_checkbox.setGeometry(QtCore.QRect(120, 30, 70, 17))
        self.CO2_checkbox.setObjectName("CO2_checkbox")
        self.PM10_checkbox = QtWidgets.QCheckBox(self.InputData_tab)
        self.PM10_checkbox.setGeometry(QtCore.QRect(30, 60, 70, 17))
        self.PM10_checkbox.setObjectName("PM10_checkbox")
        self.Traffic_format_dropdown = QtWidgets.QComboBox(self.InputData_tab)
        self.Traffic_format_dropdown.setGeometry(QtCore.QRect(100, 190, 69, 22))
        self.Traffic_format_dropdown.setObjectName("Traffic_format_dropdown")
        self.Area_dropdown = QtWidgets.QComboBox(self.InputData_tab)
        self.Area_dropdown.setGeometry(QtCore.QRect(100, 110, 69, 22))
        self.Area_dropdown.setObjectName("Area_dropdown")
        self.Annual_link_emissions_checkbox = QtWidgets.QCheckBox(self.InputData_tab)
        self.Annual_link_emissions_checkbox.setGeometry(QtCore.QRect(220, 90, 121, 17))
        self.Annual_link_emissions_checkbox.setObjectName("Annual_link_emissions_checkbox")
        self.AQ_modelling_checkbox = QtWidgets.QCheckBox(self.InputData_tab)
        self.AQ_modelling_checkbox.setGeometry(QtCore.QRect(220, 30, 131, 17))
        self.AQ_modelling_checkbox.setObjectName("AQ_modelling_checkbox")
        self.label = QtWidgets.QLabel(self.InputData_tab)
        self.label.setGeometry(QtCore.QRect(30, 110, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.InputData_tab)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 21, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.InputData_tab)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 81, 21))
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.InputData_tab)
        self.groupBox.setGeometry(QtCore.QRect(210, 10, 141, 231))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.InputData_tab)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 10, 391, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.NOX_annual_split_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.NOX_annual_split_checkbox.setGeometry(QtCore.QRect(190, 30, 181, 21))
        self.NOX_annual_split_checkbox.setObjectName("NOX_annual_split_checkbox")
        self.Output_percent_contributuons_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.Output_percent_contributuons_checkbox.setGeometry(QtCore.QRect(10, 90, 171, 16))
        self.Output_percent_contributuons_checkbox.setObjectName("Output_percent_contributuons_checkbox")
        self.Fleet_projection_tool_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.Fleet_projection_tool_checkbox.setGeometry(QtCore.QRect(190, 120, 151, 17))
        self.Fleet_projection_tool_checkbox.setObjectName("Fleet_projection_tool_checkbox")
        self.PM10_annual_split_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.PM10_annual_split_checkbox.setGeometry(QtCore.QRect(190, 60, 191, 21))
        self.PM10_annual_split_checkbox.setObjectName("PM10_annual_split_checkbox")
        self.Simple_euro_compositions_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.Simple_euro_compositions_checkbox.setGeometry(QtCore.QRect(10, 60, 181, 16))
        self.Simple_euro_compositions_checkbox.setObjectName("Simple_euro_compositions_checkbox")
        self.PM25_annual_split_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.PM25_annual_split_checkbox.setGeometry(QtCore.QRect(190, 90, 191, 17))
        self.PM25_annual_split_checkbox.setObjectName("PM25_annual_split_checkbox")
        self.Euro_compositions_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.Euro_compositions_checkbox.setGeometry(QtCore.QRect(10, 30, 131, 17))
        self.Euro_compositions_checkbox.setObjectName("Euro_compositions_checkbox")
        self.Primary_no2_fraction_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.Primary_no2_fraction_checkbox.setGeometry(QtCore.QRect(10, 120, 131, 17))
        self.Primary_no2_fraction_checkbox.setObjectName("Primary_no2_fraction_checkbox")
        self.Clear_button = QtWidgets.QPushButton(self.groupBox_2)
        self.Clear_button.setGeometry(QtCore.QRect(210, 180, 75, 23))
        self.Clear_button.setObjectName("Clear_button")
        self.Run_button = QtWidgets.QPushButton(self.groupBox_2)
        self.Run_button.setGeometry(QtCore.QRect(110, 180, 75, 23))
        self.Run_button.setObjectName("Run_button")
        self.groupBox_3 = QtWidgets.QGroupBox(self.InputData_tab)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 10, 211, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.Input_table_table = QtWidgets.QTableWidget(self.InputData_tab)
        self.Input_table_table.setGeometry(QtCore.QRect(20, 260, 1011, 421))
        self.Input_table_table.setRowCount(50)
        self.Input_table_table.setColumnCount(11)
        self.Input_table_table.setObjectName("Input_table_table")
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Input_table_table.setItem(0, 0, item)
        self.groupBox_4 = QtWidgets.QGroupBox(self.InputData_tab)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 10, 161, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.Breakdown_by_vehicle_checkbox.raise_()
        self.Source_apportionment_checkbox.raise_()
        self.PM_by_source_checkbox.raise_()
        self.NOx_checkbox.raise_()
        self.Emission_rates_checkbox.raise_()
        self.PM25_checkbox.raise_()
        self.Year_dropdown.raise_()
        self.CO2_checkbox.raise_()
        self.PM10_checkbox.raise_()
        self.Traffic_format_dropdown.raise_()
        self.Area_dropdown.raise_()
        self.Annual_link_emissions_checkbox.raise_()
        self.AQ_modelling_checkbox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.Input_table_table.raise_()
        self.Tab_main.addTab(self.InputData_tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Tab_main.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.Output_table = QtWidgets.QTableWidget(self.tab_4)
        self.Output_table.setGeometry(QtCore.QRect(50, 70, 651, 451))
        self.Output_table.setRowCount(10)
        self.Output_table.setColumnCount(4)
        self.Output_table.setObjectName("Output_table")
        item = QtWidgets.QTableWidgetItem()
        self.Output_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Output_table.setHorizontalHeaderItem(1, item)
        self.Tab_main.addTab(self.tab_4, "")
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
        self.actionNew_File = QtWidgets.QAction(MainWindow)
        self.actionNew_File.setObjectName("actionNew_File")
        self.menuFile.addAction(self.actionNew_File)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.Tab_main.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emission Factor Toolkit"))
        self.Tab_main.setTabText(self.Tab_main.indexOf(self.QA_tab), _translate("MainWindow", "QA"))
        self.Breakdown_by_vehicle_checkbox.setText(_translate("MainWindow", "Breakdown by Vehicle"))
        self.Source_apportionment_checkbox.setText(_translate("MainWindow", "Source Apportionment"))
        self.PM_by_source_checkbox.setText(_translate("MainWindow", "PM by Source"))
        self.NOx_checkbox.setText(_translate("MainWindow", "NOx"))
        self.Emission_rates_checkbox.setText(_translate("MainWindow", "Emission Rates"))
        self.PM25_checkbox.setText(_translate("MainWindow", "PM2.5"))
        self.CO2_checkbox.setText(_translate("MainWindow", "CO2"))
        self.PM10_checkbox.setText(_translate("MainWindow", "PM10"))
        self.Annual_link_emissions_checkbox.setText(_translate("MainWindow", "Annual Link Emissions"))
        self.AQ_modelling_checkbox.setText(_translate("MainWindow", "Air Quality Modelling"))
        self.label.setText(_translate("MainWindow", "Area"))
        self.label_2.setText(_translate("MainWindow", "Year"))
        self.label_3.setText(_translate("MainWindow", "Traffic Format"))
        self.groupBox.setTitle(_translate("MainWindow", "Select Outputs"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Advanced Options"))
        self.NOX_annual_split_checkbox.setText(_translate("MainWindow", "NOx Annual Emissions Euro Split"))
        self.Output_percent_contributuons_checkbox.setText(_translate("MainWindow", "Output % contributions from euro classes"))
        self.Fleet_projection_tool_checkbox.setText(_translate("MainWindow", "Fleet Projection Tool"))
        self.PM10_annual_split_checkbox.setText(_translate("MainWindow", "PM10 Annual Emissions Euro Split"))
        self.Simple_euro_compositions_checkbox.setText(_translate("MainWindow", "Simple Entry Euro Compositions"))
        self.PM25_annual_split_checkbox.setText(_translate("MainWindow", "PM2.5 Annual Emissions Euro Split"))
        self.Euro_compositions_checkbox.setText(_translate("MainWindow", "Euro Compositions"))
        self.Primary_no2_fraction_checkbox.setText(_translate("MainWindow", "Primary NO2 Fraction"))
        self.Clear_button.setText(_translate("MainWindow", "Clear"))
        self.Run_button.setText(_translate("MainWindow", "Run EFT"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Select Pollutants"))
        item = self.Input_table_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Source ID"))
        item = self.Input_table_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Road Type"))
        item = self.Input_table_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Traffic Flow"))
        item = self.Input_table_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "%HDV"))
        item = self.Input_table_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Speed (kph)"))
        item = self.Input_table_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "No of Hours"))
        item = self.Input_table_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Link Length (km)"))
        item = self.Input_table_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "% Gradient"))
        item = self.Input_table_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Flow Direction"))
        item = self.Input_table_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Load (%)"))
        __sortingEnabled = self.Input_table_table.isSortingEnabled()
        self.Input_table_table.setSortingEnabled(False)
        self.Input_table_table.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("MainWindow", "Additional Outputs"))
        self.Tab_main.setTabText(self.Tab_main.indexOf(self.InputData_tab), _translate("MainWindow", "Input Data"))
        self.Tab_main.setTabText(self.Tab_main.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        item = self.Output_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.Output_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ouput EF"))
        self.Tab_main.setTabText(self.Tab_main.indexOf(self.tab_4), _translate("MainWindow", "Output"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
