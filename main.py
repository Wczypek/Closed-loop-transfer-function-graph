from gui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from taylor import *
import sys


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.A = 0
        self.B = 0
        self.M = 0
        self.K = 0
        self.y = []
        self.u = []
        self.t = []
        self.y_visible = True
        self.u_visible = True

        self.ui.sine.clicked.connect(self.set_sine)
        self.ui.rectangular.clicked.connect(self.set_rectangular)
        self.ui.step.clicked.connect(self.set_step)

        self.ui.u_box.stateChanged.connect(self.u_changed)
        self.ui.y_box.stateChanged.connect(self.y_changed)

    def u_changed(self, state):
        if state == Qt.Checked:
            self.u_visible = True
            self.update_axes()
        else:
            self.u_visible = False
            self.update_axes()

    def y_changed(self, state):
        if state == Qt.Checked:
            self.y_visible = True
            self.update_axes()
        else:
            self.y_visible = False
            self.update_axes()

    def take_variables(self):
        self.A = float(self.ui.A_value.text())
        self.B = float(self.ui.B_value.text())
        self.M = float(self.ui.M_value.text())
        self.K = float(self.ui.K_value.text())
        self.t = time_function()

    def set_sine(self):
        self.take_variables()
        self.u = sin_func(1, self.t)
        self.y = integration(1, self.A, self.B, self.K, self.M, self.u)
        self.update_axes()

    def set_rectangular(self):
        self.take_variables()
        self.u = rectangular_func(1, self.t)
        self.y = integration(1, self.A, self.B, self.K, self.M, self.u)
        self.update_axes()

    def set_step(self):
        self.take_variables()
        self.u = step_func(1, self.t)
        self.y = integration(1, self.A, self.B, self.K, self.M, self.u)
        self.update_axes()

    def update_axes(self):
        self.ui.u_y_plot.canvas.axes.clear()
        if self.y_visible:
            self.ui.u_y_plot.canvas.axes.plot(self.t, self.y)
        if self.u_visible:
            self.ui.u_y_plot.canvas.axes.plot(self.t, self.u)
        self.ui.u_y_plot.canvas.draw()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
