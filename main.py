import sys
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from db.models import *
from db.queries import query3


class MainWindow(QMainWindow):
    def __init__(self):
        self.sightValue = None
        self.ageValue = None

        resorts = [x for x in Resort.select()]
        resort_names = [x.name for x in resorts]

        super().__init__()

        self.resize(800, 800)
        self.setWindowTitle("Турагенство?")

        self.sight_label = QLabel(self)
        self.sight_label.move(300, 50)
        self.sight_label.setFixedSize(200, 30)
        self.setSightLabel()

        self.sight_input = QPushButton('Введите название', self)
        self.sight_input.move(10, 50)
        self.sight_input.setFixedSize(200, 30)
        self.sight_input.clicked.connect(self.getSightName)

        self.label1 = QLabel(self)
        self.label1.move(10, 100)
        self.label1.setFixedSize(200, 30)
        self.label1.setText('Выберите курорт')
        
        self.combo = QComboBox(self)
        self.combo.move(300, 100)
        self.combo.addItems(resort_names)
        self.combo.setFixedSize(150, 30)

        self.btn = QPushButton('Добавить достопримечательность', self)
        self.btn.move(10, 150)
        self.btn.setFixedSize(250, 30)
        self.btn.clicked.connect(self.addSight)

        self.age_label = QLabel(self)
        self.age_label.move(300, 200)
        self.age_label.setFixedSize(200, 30)
        self.setAgeLabel()

        self.age_input = QPushButton('Введите возраст', self)
        self.age_input.move(10, 200)
        self.age_input.setFixedSize(200, 30)
        self.age_input.clicked.connect(self.getAge)

        self.label2 = QLabel(self)
        self.label2.move(10, 250)
        self.label2.setFixedSize(200, 30)
        self.label2.setText('Выберите продолжительность')

        self.duration = QSpinBox(self)
        self.duration.setRange(1, 100)
        self.duration.move(300, 250)
        self.duration.setFixedSize(200, 30)

        self.search_btn = QPushButton('Найти достопримечательности', self)
        self.search_btn.move(10, 300)
        self.search_btn.setFixedSize(250, 30)
        self.search_btn.clicked.connect(self.selectData)

        self.qtree = QTreeView(self)
        
        self.initModel()
        self.qtree.move(50, 400)
        self.qtree.setFixedSize(550, 250)

    def setSightLabel(self, value=''):
        self.sightValue = value
        label_text = value if value else 'Вы ничего не ввели'
        self.sight_label.setText(label_text)

    def setAgeLabel(self, value=None):
        self.ageValue = value
        label_text = f'Возраст для поиска: {value}' if value else 'Вы ничего не ввели'
        self.age_label.setText(label_text)

    def getSightName(self):
        text, ok = QInputDialog.getText(self, 'Евровидение отменили', 'Введите название вашей достопримечательности:')

        if ok:
            self.setSightLabel(text)

    def getAge(self):
        text, ok = QInputDialog.getInt(self, 'Сыр с плесенью', 'Введите возраст:')

        if ok:
            self.setAgeLabel(text)

    def addSight(self):
        resort = Resort.get(Resort.name == str(self.combo.currentText()))
        name = self.sightValue
        if not name:
            QErrorMessage(self).showMessage("Как же вы хотите добавить достопримечательность, не введя её название?")
        else:
            Sight.create(
                name=name,
                resort=resort,
            )
        
        self.setSightLabel()

    def selectData(self):
        age = self.ageValue
        duration = int(self.duration.text())

        if not age:
            QErrorMessage(self).showMessage("Возможно, не стоит скрывать возраст?")
        else:
            query = query3(age=int(age), duration=duration)
            self.initModel(query.namedtuples())

        self.setAgeLabel()
                
    def initModel(self, data=[]):
        self.model = QStandardItemModel(0, 2, self.qtree)
        self.model.setHeaderData(0, Qt.Horizontal, u"Название")
        self.model.setHeaderData(1, Qt.Horizontal, u"Координаты")

        self.qtree.setModel(self.model)
        self.qtree.setColumnWidth(0, 275)

        for item in data:
            self.addSightModel(item)

    def addSightModel(self, sight):
        self.model.insertRow(0)
        self.model.setData(self.model.index(0, 0), sight.name)
        self.model.setData(self.model.index(0, 1), sight.coordinate)


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
