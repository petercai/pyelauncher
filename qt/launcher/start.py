# This Python file uses the following encoding: utf-8
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication


class main(QDialog):
    def __init__(self):
        super(main, self).__init__()
        uic.loadUi("dialog.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = main()
    widget.show()
    sys.exit(app.exec_())
