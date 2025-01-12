import os

from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from image_proceessor import ImageProcessor

app = QApplication([])
win = QWidget()
win.setWindowTitle("Easy Editor")
win.resize(700, 500)

lb_image = QLabel("Image")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Дзеркало")
btn_bw = QPushButton("Ч/Б")
btn_filter_red = QPushButton("Червоний фільтр")
btn_3d = QPushButton("- Яркість")


row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)


col_tools = QVBoxLayout()
row_tools1 = QHBoxLayout()

row_tools1.addWidget(btn_left)
row_tools1.addWidget(btn_right)
row_tools1.addWidget(btn_filter_red)

row_tools2 = QHBoxLayout()
row_tools2.addWidget(btn_flip)
row_tools2.addWidget(btn_bw)
row_tools2.addWidget(btn_3d)

row_tools.addLayout(row_tools1)
row_tools.addLayout(row_tools2)

col2.addLayout(row_tools)
col2.addWidget(lb_image, 95)

row.addLayout(col2, stretch=3)
row.addLayout(col1, stretch=1)
win.setLayout(row)

work_dir = ""

def filter(files, extensions):
   result = []
   for filename in files:
      for ext in extensions:
         if filename.endswith(ext):
            result.append(filename)
   return result

def chooseWorkDir():
   global work_dir
   work_dir = QFileDialog.getExistingDirectory()

def showFilenamesList():
   extensions = [".jpg", ".png", ".jpeg", ".gif", ".bmp"]
   chooseWorkDir()
   filenames = filter(os.listdir(work_dir), extensions)
   lw_files.clear()
   lw_files.addItems(filenames)


def showChosenImage():
   if lw_files.currentRow() >= 0:
      filename = lw_files.currentItem().text()
      workimage.loadImage(work_dir, filename)
      image_path = os.path.join(workimage.dir, workimage.filename)
      workimage.showImage(image_path, lb_image)

workimage = ImageProcessor()
lw_files.currentRowChanged.connect(showChosenImage)


btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_flip.clicked.connect(workimage.do_flip)



btn_filter_red.clicked.connect(workimage.do_red)
btn_3d.clicked.connect(workimage.do_brightness)

win.setStyleSheet("""
   QWidget {
      background-color: grey;
      font-size: 28px;
   }

   QPushButton {
      background-color: black;
      color: white;
      border-radius: 5px;
      padding: 5px;
      font-size: 14px;

   }
   QPushButton:hover {
      background-color: #333230;
      color: white;
   }

   QListWidget {
      background-color: white;
      border: 2px solid black;
      border-radius: 5px;
   }
""")

btn_dir.clicked.connect(showFilenamesList)
win.show()

app.exec_()
