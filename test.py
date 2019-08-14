import sys,MainWin

from PyQt5 import QtWidgets

app=QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QWidget()
ui=MainWin.Ui_Form()
ui.setupUi(widget)
widget.show()
sys.exit(app.exec_())