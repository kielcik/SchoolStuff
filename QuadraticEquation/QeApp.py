from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QInputDialog, QDialog
from QeAppDesign import *
import math
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.input_window)

    def input_window(self):
        values = [0, 0, 0]
        equation = QInputDialog().getText(
            self, "Podaj dane", "Wpisz A, B i C oddzielając wartości przecinkami: ")

        try:
            values = equation[0].split(',')
            for i in range(0, len(values)):
                if values[i] == "": values[i] = 0
                values[i] = float(values[i])
            if len(values) != 3:
                raise ValueError

        except ValueError:
            self.show_warning()
            self.ui.pushButton_2.setDisabled(True)

        if equation[1]:
            if values[0] != 0 and len(values) == 3:
                if values[1] > 0 and values[2] > 0:
                    self.ui.equation.setText(f"f(x) = {values[0]}x²+{values[1]}x+{values[2]}")
                elif values[1] < 0 < values[2]:
                    self.ui.equation.setText(f"f(x) = {values[0]}x²{values[1]}x+{values[2]}")
                elif values[2] < 0 < values[1]:
                    self.ui.equation.setText(f"f(x) = {values[0]}x²+{values[1]}x{values[2]}")
                elif values[1] < 0 and values[2] < 0:
                    self.ui.equation.setText(f"f(x) = {values[0]}x²{values[1]}x{values[2]}")
                self.ui.pushButton_2.setEnabled(True)
                self.ui.pushButton_2.clicked.connect(lambda: self.root_calc(values))

            elif values[0] == 0 and len(values) == 3:
                self.ui.equation.setText("")
                self.ui.delta.setText("")
                self.show_info()

    def root_calc(self, values):
        delta = math.pow(values[1], 2) - (4 * values[0] * values[2])
        self.ui.delta.setText(str(delta))
        if delta > 0:
            root1 = str(round(((values[1] * -1) - math.sqrt(delta)) / 2 * values[0], 2))
            root2 = str(round(((values[1] * -1) + math.sqrt(delta)) / 2 * values[0], 2))
            self.ui.roots.setText(f"x₁ = {root1}   x₂ = {root2}")
            if values[0] > 0:
                self.ui.photo.setPixmap(QtGui.QPixmap("photos/up_2.png"))
            elif values[0] < 0:
                self.ui.photo.setPixmap(QtGui.QPixmap("photos/down_2.png"))
        elif delta == 0:
            root1 = str(round(-1 * (values[1] / 2 * values[0])))
            self.ui.roots.setText(f"x₁ = x₂ = {root1}")
            if values[0] > 0:
                self.ui.photo.setPixmap(QtGui.QPixmap("photos/up_1.png"))
            elif values[0] < 0:
                self.ui.photo.setPixmap(QtGui.QPixmap("photos/down_1.png"))
        else:
            self.ui.roots.setText("Brak miejsc zerowych")
            if values[0] > 0:
                self.ui.photo.setPixmap(QtGui.QPixmap("photos/up_0.png"))
            elif values[0] < 0:
                self.ui.photo.setPixmap(QtGui.QPixmap("photos/down_0.png"))

    def show_warning(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Należy wprowadzić trzy liczby oddzielone przecinkami")
        msgBox.setWindowTitle("Informacja")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def show_info(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("To nie będzie funkcja kwadratowa")
        msgBox.setWindowTitle("Informacja")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Window()
    okno.show()
    app.exec_()
