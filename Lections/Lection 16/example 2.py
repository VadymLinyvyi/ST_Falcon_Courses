from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot

@Slot()
def onClick():
    label.setText("You clicked the button")


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

button = QPushButton("I'm just a button man")
label = QLabel('=)')
button.clicked.connect(onClick)
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()