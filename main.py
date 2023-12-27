
from PyQt5 import QtWidgets, uic
from main_window_logic import MainWindowLogic
import sys

from main_window import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
logic = MainWindowLogic()
sys.exit(app.exec_())