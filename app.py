# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assignment.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import csv
import os
import sys
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 532)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ScatterButton = QPushButton(self.centralwidget)
        self.ScatterButton.setGeometry(QtCore.QRect(20, 10, 141, 32))
        self.ScatterButton.setObjectName("ScatterButton")
        self.SmoothLinesButton = QPushButton(self.centralwidget)
        self.SmoothLinesButton.setGeometry(QtCore.QRect(180, 10, 251, 32))
        self.SmoothLinesButton.setObjectName("SmoothLinesButton")
        self.PlotLinesButton = QPushButton(self.centralwidget)
        self.PlotLinesButton.setGeometry(QtCore.QRect(470, 10, 113, 32))
        self.PlotLinesButton.setObjectName("PlotLinesButton")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 601, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(-5, 1, 601, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
       # self.tab_2 = QWidget()
       # self.tab_2.setObjectName("tab_2")
       # self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdd_Data = QMenu(self.menuFile)
        self.menuAdd_Data.setObjectName("menuAdd_Data")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as_png = QAction(MainWindow)
        self.actionSave_as_png.setObjectName("actionSave_as_png")
        self.actionAdd_Row = QAction(MainWindow)
        self.actionAdd_Row.setObjectName("actionAdd_Row")
        self.actionAdd_Column = QAction(MainWindow)
        self.actionAdd_Column.setObjectName("actionAdd_Column")
        
        self.actionEdit_Data = QAction(MainWindow)
        self.actionEdit_Data.setObjectName("actionEdit_Data")
        self.menuAdd_Data.addAction(self.actionAdd_Row)
        self.menuAdd_Data.addAction(self.actionAdd_Column)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as_png)
        self.menuFile.addAction(self.menuAdd_Data.menuAction())
        self.menuEdit.addAction(self.actionEdit_Data)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        count = [1]

        self.actionLoad.triggered.connect(lambda: self.load_clicked())
        self.actionSave.triggered.connect(lambda: self.save_sheet())
        self.actionAdd_Row.triggered.connect(lambda: self.add_row())
        self.actionAdd_Column.triggered.connect(lambda: self.add_column())

        self.actionSave_as_png.triggered.connect(lambda: self.save_plot(count))
        self.ScatterButton.clicked.connect(lambda: self.scatter_plot())
        self.SmoothLinesButton.clicked.connect(lambda: self.smooth_plot())
        self.PlotLinesButton.clicked.connect(lambda: self.line_plot())
        self.actionEdit_Data.triggered.connect(lambda: self.edit_data())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ScatterButton.setText(_translate("MainWindow", "Plot Scatter points"))
        self.SmoothLinesButton.setText(_translate("MainWindow", "Plot Scatter points with smooth lines"))
        self.PlotLinesButton.setText(_translate("MainWindow", "Plot Lines"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
       # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAdd_Data.setTitle(_translate("MainWindow", "Add Data"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as_png.setText(_translate("MainWindow", "Save as .png"))
        self.actionAdd_Row.setText(_translate("MainWindow", "Add Row"))
        self.actionAdd_Column.setText(_translate("MainWindow", "Add Column"))
        self.actionAdd_Row.setText(_translate("MainWindow", "Add Row"))
        self.actionAdd_Column.setText(_translate("MainWindow", "Add Column"))
        self.actionEdit_Data.setText(_translate("MainWindow", "Edit Data"))

    def load_clicked(self):
        self.tableWidget.check_change = False
        path = QFileDialog.getOpenFileName(self.tableWidget, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')

        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                #print(path[0])
                csv_reader = csv.reader(csv_file, dialect='excel')
                #print(list(csv_reader))
               # self.tableWidget.setRowCount(len(list(csv_reader)))
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(2)
               # my_file = csv.reader(csv_file, dialect='excel')
                #print(csv_reader)
                for row_data in csv_reader:
                    #print(row_data)
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    if len(row_data) > 2:
                        self.tableWidget.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.tableWidget.setItem(row, column, item)
               # print(list(csv_reader))        `
        self.tableWidget.check_change = True 
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) 

    def edit_data(self):
        self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

    def save_sheet(self):
        path = QFileDialog.getSaveFileName(self.tableWidget, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.tableWidget.rowCount()):
                    row_data = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)    

    def add_row(self):
        #self.tableWidget.check_change = False
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
       # self.tableWidget.check_change = True

    def add_column(self):
       # self.tableWidget.check_change = False
        row = self.tableWidget.columnCount()
        self.tableWidget.insertColumn(row)
        #self.tableWidget.check_change = True  

    def scatter_plot(self):
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection) 
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        item = self.tableWidget.selectedIndexes()

        
        rows = []
        columns = []

        for element in list(item):
            #print(element.row())
            rows.append(element.row())
            columns.append(element.column())

        columns.sort()    

        data1 = []
        data2 = []
        xLabel = ''
        yLabel = ''

        k=0

        for itr in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(itr,columns[0])
            if k==0:
                k+=1
                xLabel += str(item.text())
                continue
            
            if item is not None:
                data1.append(int(item.text()))

        k=0        
                
        for itr in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(itr,columns[len(columns)-1])
            if k==0:
                k+=1
                yLabel += str(item.text())
                continue
            
            if item is not None:
                data2.append(int(item.text()))      
                

        self.tab_2 = QWidget()
        self.tab_2.setObjectName("Scatter_Plot")
        self.tabWidget.addTab(self.tab_2,"Scatter Plot")
        self.tab_2.layout = QVBoxLayout(self.tabWidget)
        self.canvas = PlotCanvas(self.tabWidget, width=5, height=4)

        ax = self.canvas.figure.add_subplot(111)
        #data = [random.random() for i in range(25)]
        ax.scatter(data1,data2)
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel)
        ax.set_title("Scatter Plot")
        self.canvas.draw()
        
        self.tab_2.layout.addWidget(self.canvas)
        self.tab_2.setLayout(self.tab_2.layout)    
        #print(columns[0],columns[len(columns)-1])  

    def smooth_plot(self):
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection) 
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        item = self.tableWidget.selectedIndexes()

        
        rows = []
        columns = []

        for element in list(item):
            #print(element.row())
            rows.append(element.row())
            columns.append(element.column())

        columns.sort()    

        data1 = []
        data2 = []
        xLabel = ''
        yLabel = ''

        k=0

        for itr in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(itr,columns[0])
            if k==0:
                k+=1
                xLabel += str(item.text())
                continue
            
            if item is not None:
                data1.append(int(item.text()))

        k=0        
                
        for itr in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(itr,columns[len(columns)-1])
            if k==0:
                k+=1
                yLabel += str(item.text())
                continue
            
            if item is not None:
                data2.append(int(item.text()))      
                

        self.tab_2 = QWidget()
        self.tab_2.setObjectName("Smooth_Plot")
        self.tabWidget.addTab(self.tab_2,"Smooth Plot")
        self.tab_2.layout = QVBoxLayout(self.tabWidget)
        self.canvas = PlotCanvas(self.tabWidget, width=5, height=4)

        ax = self.canvas.figure.add_subplot(111)
        #data = [random.random() for i in range(25)]
        ax.plot(data1,data2,linestyle='dashed',marker='o')
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel)
        ax.set_title("Scatter Plot with smooth lines")
        self.canvas.draw()
        
        self.tab_2.layout.addWidget(self.canvas)
        self.tab_2.setLayout(self.tab_2.layout)

    def line_plot(self):
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection) 
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        item = self.tableWidget.selectedIndexes()

        
        rows = []
        columns = []

        for element in list(item):
            #print(element.row())
            rows.append(element.row())
            columns.append(element.column())

        columns.sort()    

        data1 = []
        data2 = []
        xLabel = ''
        yLabel = ''

        k=0

        for itr in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(itr,columns[0])
            if k==0:
                k+=1
                xLabel += str(item.text())
                continue
            
            if item is not None:
                data1.append(int(item.text()))

        k=0        
                
        for itr in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(itr,columns[len(columns)-1])
            if k==0:
                k+=1
                yLabel += str(item.text())
                continue
            
            if item is not None:
                data2.append(int(item.text()))        
                

        self.tab_2 = QWidget()
        self.tab_2.setObjectName("Line_Plot")
        self.tabWidget.addTab(self.tab_2,"Line Plot")
        self.tab_2.layout = QVBoxLayout(self.tabWidget)
        self.canvas = PlotCanvas(self.tabWidget, width=5, height=4)

        ax = self.canvas.figure.add_subplot(111)
        #data = [random.random() for i in range(25)]
        ax.plot(data1,data2)
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel)
        ax.set_title("Line Plot")
        #ax.figure.savefig('plot.png')
        self.canvas.draw()
        
        self.tab_2.layout.addWidget(self.canvas)
        self.tab_2.setLayout(self.tab_2.layout)
        #self.setLayout(self.layout)
    

    def save_plot(self,count):
        num = self.tabWidget.currentIndex()
        wid = self.tabWidget.widget(num)
        #lay = wid.layout()
        pix = QtGui.QPixmap(wid.size())
        wid.render(pix)
        present = count[len(count)-1]
        pix.save("plot"+str(present)+".png")
        count.append(present+1)

        #print(self.tabWidget.findChildren(wid))


        

if __name__ == "__main__":
    import sys
    count = 1
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
