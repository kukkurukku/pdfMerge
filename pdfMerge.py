import sys, os, io
if hasattr(sys, 'frozen'): #making_a_standAlone_installer
    os.environ['PATH'] = sys._MEIPASS + ';' + os.environ['PATH'] 

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout,\
                            QGridLayout, QDial, QDialog, QFileDialog, QMessageBox, QAbstractItemView  #check_the_comma

