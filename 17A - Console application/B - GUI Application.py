from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

app = QApplication(sys.argv)
main_window = QWidget()
main_window.setGeometry(100, 100, 500, 500)
main_window.setWindowTitle("GUI Application")

label = QLabel(main_window)
label.setText("Programing GIU Find")

button = QPushButton(main_window)
button.setGeometry(200, 200, 100, 50)
button.setText("Click me")

main_window.show()
app.exec()

#event( sự kiện)
#event handler /handle
#signal (event) & slot(event handler)