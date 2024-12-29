import os

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, \
    QFileDialog

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
#col2.addLayout(row_tools)
row_tools.addLayout(col2)
row.addLayout(col1, stretch=1)
row.addLayout(row_tools, stretch=3)

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

btn_dir.clicked.connect(showFilenameList)

app.exec_()
