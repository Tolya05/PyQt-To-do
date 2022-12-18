import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QRadioButton,
    QMessageBox, 
    QListWidget
)
from PyQt6.QtGui import QIcon
from qt_material import apply_stylesheet
import json

class MainWindow(QWidget):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('To-Do')
        self.setGeometry(100, 200, 400, 400)
        icon = QIcon('to-do.png')
        self.setWindowIcon(icon)
        apply_stylesheet(self, theme='dark_purple.xml')
        self.toDoList = []

        #Create the list
        self.toDoListWidget = QListWidget(self)

        #Create a to do item
        self.addItemLabel = QLabel('Add Item:')
        self.addItemEntry = QLineEdit()
        self.addItemEntry.setPlaceholderText('Add an Item...')
        self.addItemEntry.returnPressed.connect(self.addItemMethod)
        self.addItemButton = QPushButton('Add Item')
        self.addItemButton.setChecked(True)
        self.addItemButton.clicked.connect(self.addItemMethod)

        #Removes Items
        self.removeItemButton = QPushButton('Remove Item')
        self.removeItemButton.setChecked(True)
        self.removeItemButton.clicked.connect(self.removeItemMethod)

        #Save/Load Button
        self.loadButton = QPushButton('Load')
        self.loadButton.setChecked(True)
        self.loadButton.clicked.connect(self.loadMethod)

        self.saveButton = QPushButton('Save')
        self.saveButton.setChecked(True)
        self.saveButton.clicked.connect(self.saveMethod)

        self.saveLoadFrame = QWidget(self)
        saveLoadLayout = QHBoxLayout()
        saveLoadLayout.addWidget(self.saveButton)
        saveLoadLayout.addWidget(self.loadButton)
        self.saveLoadFrame.setLayout(saveLoadLayout)

        #Credits Button to the author of app icon
        creditsButton = QPushButton('Credits')
        creditsButton.setChecked(True)
        creditsButton.clicked.connect(self.creditsButton)
        
        mainLayout = QGridLayout()
        self.setLayout(mainLayout)
        mainLayout.addWidget(self.toDoListWidget, 0, 0, 4, 3)
        mainLayout.addWidget(self.addItemLabel, 5, 0)
        mainLayout.addWidget(self.addItemEntry, 5, 1)
        mainLayout.addWidget(self.addItemButton, 5, 2)
        mainLayout.addWidget(self.removeItemButton, 6, 2)
        mainLayout.addWidget(self.saveLoadFrame, 6, 1)
        mainLayout.addWidget(creditsButton, 6, 0)

        self.show()
    
    def addItemMethod(self):
        itemEntry = self.addItemEntry
        self.toDoList.append(itemEntry.text())
        self.toDoListWidget.clear()
        self.toDoListWidget.addItems(self.toDoList)
        itemEntry.setText('')

    def removeItemMethod(self):
        item = self.toDoListWidget.currentIndex()
        itemValue = item.row()
        self.toDoList.pop(itemValue)
        self.toDoListWidget.clear()
        self.toDoListWidget.addItems(self.toDoList)

    def saveMethod(self):
        with open('todo.json', 'w') as file:
            json.dump(self.toDoList, file, indent=4)
        QMessageBox.information(
            self,
            'Saved',
            'Your To-Do List was saved'
        )

    def loadMethod(self):
        self.toDoListWidget.clear()
        with open('todo.json', 'r') as file:
            data = json.load(file)
            self.toDoList.clear()
            for items in data:
                self.toDoList.append(items)
        self.toDoListWidget.addItems(self.toDoList)
        QMessageBox.information(
            self,
            'Loaded',
            'Your To-Do List was loaded'
        )

    def creditsButton(self):
        QMessageBox.information(
            self, 
            'Credits',
            'App made by Anatoliy K.\nResults icons created by Icongeek26 '
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())