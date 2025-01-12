import os

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, \
    QFileDialog

from image_processor import ImageProcessor

app = QApplication([])
win = QWidget()
win.setWindowTitle("Easy Editor")
win.resize(700, 500)

label_image = QLabel("Тут буде картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Дзеркало")
btn_bw = QPushButton("Ч/Б")

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
row_tools = QHBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_bw)

col2.addWidget(label_image)
col2.addLayout(row_tools)
row.addLayout(col1, stretch=1)
row.addLayout(col2, stretch=3)

win.setLayout(row)
win.show()

work_dir = ""

def filter(files, extensions):
    result = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                result.append(file)
    return result

def chooseWorkDir():
    global work_dir
    work_dir = QFileDialog.getExistingDirectory()

def showFilenameList():
    extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    chooseWorkDir()
    filenames = filter(os.listdir(work_dir), extensions)
    lw_files.clear()
    lw_files.addItems(filenames)

def showChosenImage():
   if lw_files.currentRow() >= 0:
      filename = lw_files.currentItem().text()
      workimage.loadImage(work_dir, filename)
      image_path = os.path.join(workimage.dir, workimage.filename)
      workimage.showImage(image_path, label_image)

workimage = ImageProcessor()

lw_files.currentRowChanged.connect(showChosenImage)
btn_dir.clicked.connect(showFilenameList)

btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_flip.clicked.connect(workimage.do_flip)

win.setStyleSheet("""
   QWidget {
      background-color: grey;
      font-size: 32px;
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

app.exec_()
