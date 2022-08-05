from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PIL import Image
import threading

app = QApplication(sys.argv)

def selectPath(p):
    file, check = QFileDialog.getOpenFileName(None, caption='Select image.', directory='',
                                              filter='PNG Files (*.png);;JPG Files (*.jpg);;JPEG Files (*.jpeg)')

    if check:
        p.setText(file)

def selectOutputPath(p):
    folder = QFileDialog.getExistingDirectory(None, caption='Select the output path.', directory='')

    if folder:
        p.setText(folder)

def convert(path, output, width, height):
    if not path or not output or not width or not height:
        QMessageBox.warning(w, 'Warning', 'All fields must be filled in!')
        return

    try: int(width)
    except:
        QMessageBox.warning(w, 'Warning', 'Width must be a number!')
        return

    try: int(height)
    except:
        QMessageBox.warning(w, 'Warning', 'Height must be a number!')
        return

    image_list = path.split("/")[-1].split(".")

    i = Image.open(path)
    i_r = i.resize((int(width), int(height)), Image.Resampling.LANCZOS)
    i_r.save(f'{output}/{image_list[0]}CONVERTED.{image_list[1]}')

    QMessageBox.about(w, 'Finished', 'Converted')

w = QWidget()
lyt = QGridLayout()
lyt.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

title = QLabel(parent=w, text='Resize Image by Niklas')
title.setFont(QFont('Montserrat', 30))

path_note = QLabel(parent=w, text='Image: ')
path = QLineEdit(parent=w)

selectpath = QPushButton(parent=w, text='...')
selectpath.clicked.connect(lambda: selectPath(path))
selectpath.setFixedWidth(30)

output_note = QLabel(parent=w, text='Output folder: ')
output = QLineEdit(parent=w)

selectoutput = QPushButton(parent=w, text='...')
selectoutput.clicked.connect(lambda: selectOutputPath(output))
selectoutput.setFixedWidth(30)

w_note = QLabel(parent=w, text='New Width: ')
width = QLineEdit(parent=w)

h_note = QLabel(parent=w, text='New Height: ')
height = QLineEdit(parent=w)

convert_b = QPushButton(parent=w, text='Convert')
convert_b.clicked.connect(lambda: convert(path.text(), output.text(), width.text(), height.text()))

lyt.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

lyt.addWidget(path_note, 3, 0, Qt.AlignLeft)
lyt.addWidget(path, 3, 1, Qt.AlignRight)
lyt.addWidget(selectpath, 3, 1, Qt.AlignRight)

lyt.addWidget(output_note, 4, 0, Qt.AlignLeft)
lyt.addWidget(output, 4, 1, Qt.AlignRight)
lyt.addWidget(selectoutput, 4, 1, Qt.AlignRight)

lyt.addWidget(w_note, 5, 0, Qt.AlignLeft)
lyt.addWidget(width, 5, 1, Qt.AlignRight)

lyt.addWidget(h_note, 6, 0, Qt.AlignLeft)
lyt.addWidget(height, 6, 1, Qt.AlignRight)

lyt.addWidget(convert_b, 7, 0, 1, 0, Qt.AlignCenter)

w.setLayout(lyt)
w.setGeometry(0, 0, 600, 600)
w.setWindowTitle('Resize Image')
w.show()

sys.exit(app.exec_())