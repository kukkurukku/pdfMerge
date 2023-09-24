import sys, os, io
import typing
from PyQt5 import QtCore, QtGui
if hasattr(sys, 'frozen'): #making_a_standAlone_installer
    os.environ['PATH'] = sys._MEIPASS + ';' + os.environ['PATH'] 

#import necessary libraries

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout,\
                            QGridLayout, QDial, QDialog, QFileDialog, QMessageBox, QAbstractItemView  #check_the_comma

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyPDF2 import PdfFileMerger #need to install PyPDF "pip3 install PyPDF2"

def resource_path(relative_path):
    """
    This function, resource_path, is a common utility function that developers use 
    when working with PyInstaller to bundle a Python application into a standalone 
    executable, especially when the application has external resource files (like 
    images, data files, etc.). It's often used with GUI frameworks like PyQt5, which 
    may require paths to these resources.
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

#creatingClasses


#dragAndDropFeature
class ListWidget(QListWidget):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setStyleSheet('font-size: 25px;')
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            return super().dragEnterEvent()
    
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            return super().dragMoveEvent(event)
    
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            pdfFiles = []

            for url in evnet.mimeData().urls():
                if url.isLocalFile():
                    if url.toString().endswith('.pdf'):
                                               pdfFiles.append(str(url.toLocalFile()))
        else:    
            return super().dropEvent(event)

class PDFApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PDF Bundler')  #appTitle
        #self.setWindowIcon(QIcon(resource_path('DesignAIconInIllustrator')))  #AppIcon #need to add an icon
        self.resize(960, 540) #windowSize

app = QApplication(sys.argv)
app.setStyle('fusion') #iwilleditthislater

pdfApp = PDFApp()
pdfApp.show()

sys.exit(app.exec_())

#donewithshell