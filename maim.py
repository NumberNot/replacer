import sys 
import os, shutil
import design

from pathlib import Path
from PyQt5 import QtWidgets

class ReplaceApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnSelectFolder.clicked.connect(self.browse_folder)
        self.btnSelectFile.clicked.connect(self.browse_file)
        self.btnStart.clicked.connect(self.find_file)
        self.btnChange.clicked.connect(self.change_file)

    def browse_folder(self):
        global directory
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose folder")
        if directory:
#            print(os.getcwd())
            self.lineFolder.setText(os.path.abspath(directory))
            
    def browse_file(self):
        global pick_file
        pick_file = QtWidgets.QFileDialog.getOpenFileName(self, "Choose file")
        if pick_file:
            self.lineFile.setText(Path(pick_file[0]).name)
#            self.lineFile.setText(pick_file[0])        # Uncomment if you need full path to the file
#            tail = os.path.split(pick_file[0])         # Uncomment if you need get  part of path
#            self.lineFile.setText(tail[1])             # 
            sfile__ = self.lineFile.text()

    def find_file(self):
        self.listWidget.clear()
        sfile__ = self.lineFile.text()
        i = 0
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if(file.endswith(sfile__)):
                        self.listWidget.addItem(os.path.join(root,file))
                        i+=1
        except Exception as identifier:
            self.browse_folder()
        self.labelFound.setText("Total: " + str(int(i)))

    def change_file(self):
        self.listErrors.clear()
        items = []
        i = 0
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index))
        for item in items:
            try:
                shutil.copy2(pick_file[0], item.text())
                i+=1
            except Exception as identifier:
                self.listErrors.addItem(str(identifier))
        self.labelChanged.setText("Changed: " + str(int(i)))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ReplaceApp() 
    window.show()
    app.exec_() 

if __name__ == '__main__': 
    main()