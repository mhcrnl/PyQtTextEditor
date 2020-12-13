# This Python file uses the following encoding: utf-8
# File: text_editor.py created with Qt Creator
# Run: python3 text_editor.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QMainWindow, QMessageBox
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtWidgets import QAction

class text_editor(QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Window ----------------------------------------
        self.setWindowTitle("PyQtTextEditor")
        self.isMaximized()
        self.setFixedSize(850, 500)
        self.setWindowIcon(QIcon("images/color.ico"))
        self.show()
        # Adding QTextEdit widget -------------------------
        text = QTextEdit(self)
        text.setTabStopWidth(20000)
        self.setCentralWidget(text)
        # File menu New -------------------------------------
        new = QAction(QIcon("images/color.ico"), "New", self)
        new.setStatusTip("Creaza un nou document.")
        new.triggered.connect(self.New)
        # File menu Open ------------------------------------
        open = QAction(QIcon("images/color.ico"), "Open File", self)
        open.setStatusTip("Deschide un document.")
        open.triggered.connect(self.Open)
        # File menu Save ---------------------------------------------
        save = QAction(QIcon("images/color.ico"), "Save", self)
        save.setStatusTip("Salveaza un document.")
        save.triggered.connect(self.Save)
        # File menu Exit ---------------------------------------------
        exit = QAction(QIcon("images/color.ico"), "Exit", self)
        exit.setStatusTip("Exit application.")
        exit.triggered.connect(self.Exit)

        menubar = self.menuBar()
        file = menubar.addMenu("File")

        file.addAction(new)
        file.addAction(open)
        file.addAction(save)
        file.addAction(exit)

    def Exit(self):
        f = QMessageBox.question(self, "PyQtTextEditor", "Doriti sa inchideti aplicatia?",
            QMessageBox.Save | QMessageBox.Yes | QMessageBox.No, QMessageBox.Save)
        if f == QMessageBox.Save:
            text_editor.Save(self)
        elif f == QMessageBox.Yes:
            QMainWindow.close(self)
        elif f == QMessage.Box.No:
            QMainWindow.destroy(self, destroyWindow=False)


    def New(self):
        self.New = text_editor()
        self.New.show()

    def Open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",
".", "(*.*)All Files")[0]
        if filename == '':
            text_editor()
        else:
            f = open(filename, "r")
            file = f.read()
            self.text.setText(file)
            f.close()

    def Save(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save File",
".", "(*.*)All Files")[0]
        if filename == '':
            text_editor()
        else:
            f = open(filename, "w")
            # file = f.read()
            file = self.text.toPlainText()
            f.write(file)
            f.close()


if __name__ == "__main__":
    app = QApplication([])
    window = text_editor()
    window.show()
    sys.exit(app.exec_())
