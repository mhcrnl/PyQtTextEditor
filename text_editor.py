# This Python file uses the following encoding: utf-8
# File: text_editor.py created with Qt Creator
# Run: python3 text_editor.py

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QMainWindow, QMessageBox, QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QAction
from PyQt5.QtCore import QDir
from PyQt5.QtGui import *

class text_editor(QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.prog_name = "PyQtTextEditor"
        self.version = "0.01"
        self.author = "mhcrnl@gmail.com"

        # Window ----------------------------------------
        self.setWindowTitle(self.prog_name)
        self.isMaximized()
        self.setFixedSize(850, 500)
        self.setWindowIcon(QtGui.QIcon("PyQtTextEditor/images/home1.png"))
        self.statusBar()
        self.show()
        # Adding PyQt ToolBar -------------------------------------------
        self.toolbar = self.addToolBar("Exit")
        #self.toolbar.addAction(exit)

        # Adding QTextEdit widget -------------------------
        self.text = QTextEdit(self)
        self.text.setTabStopWidth(20000)
        self.setCentralWidget(self.text)
        # File menu New -------------------------------------
        new = QAction(QIcon("icons/new.png"), "New", self)
        new.setShortcut("Ctrl+N")
        new.setStatusTip("Creaza un nou document.")
        new.triggered.connect(self.New)
        # File menu Open ------------------------------------
        open = QAction(QIcon("images/color.ico"), "Open File", self)
        open.setStatusTip("Deschide un document.")
        open.triggered.connect(self.Open1)
        # File menu Save ---------------------------------------------
        save = QAction(QIcon("images/color.ico"), "Save", self)
        save.setStatusTip("<h2>Salveaza un document.</h2>")
        save.triggered.connect(self.Save)
        # File menu Exit ---------------------------------------------
        exit = QAction(QIcon("images/color.ico"), "Exit", self)
        exit.setStatusTip("Exit application.")
        exit.triggered.connect(self.Exit)
        #Cut --------------------------------------------------------
        cut = QAction(QIcon("images/color.ico"), "Cut", self)
        cut.setStatusTip("Delete and copy text to clipboard.")
        cut.triggered.connect(self.Cut)
        # Copy ---------------------------------------------------
        copy = QAction(QIcon("images/color.ico"), "Copy", self)
        copy.setStatusTip("Copy text to clipboard.")
        copy.triggered.connect(self.Copy)
        # Paste --------------------------------------------------
        paste = QAction(QIcon("images/color.ico"), "Paste", self)
        paste.setStatusTip("Paste text from clipboard")
        paste.triggered.connect(self.Paste)
        # Undo ---------------------------------------------------
        undo = QAction(QIcon("images/color.ico"), "Undo", self)
        undo.setStatusTip("Undo last action.")
        undo.triggered.connect(self.Undo)
        # Redo ---------------------------------------------------
        redo = QAction(QIcon("images/color.ico"), "Redo", self)
        redo.setStatusTip("Redo last undone thing.")
        redo.triggered.connect(self.Redo)
        # Info --------------------------------------------------
        info = QAction(QIcon("images/color.ico"), "Info", self)
        info.setStatusTip("Information by developer.")
        info.triggered.connect(self.Info)

        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        help = menubar.addMenu("Help")

        file.addAction(new)
        file.addAction(open)
        file.addAction(save)
        file.addAction(exit)

        edit.addAction(cut)
        edit.addAction(copy)
        edit.addAction(paste)
        edit.addAction(undo)
        edit.addAction(redo)

        help.addAction(info)

        self.toolbar.addAction(exit)

    def Info(self):
        f = QMessageBox.about(self, "About", "PyQtTextEditor\n\n Version 0.01 \n\n A simple text editor in python3 and PyQt5")

    def Redo(self):
        self.text.redo()

    def Undo(self):
        self.text.undo()

    def Paste(self):
        self.text.paste()

    def Copy(self):
        self.text.copy()

    def Cut(self):
        self.text.cut()

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

    def Open1(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilters(["Text files (*.txt)"])
        #filenames = QString()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open (filenames[0], "r")
            with f:
                data = f.read()
                self.text.setText(data)


    def Open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",
"~/", "(*.txt *.md)All Files")[0]
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
