import sys,MainWin2

from PyQt5 import QtWidgets

app=QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QWidget()
ui=MainWin2.Ui_Form()
ui.setupUi(widget)
widget.show()
sys.exit(app.exec_())