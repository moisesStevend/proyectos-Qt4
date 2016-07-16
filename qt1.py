from PyQt4.QtGui import *  #importamos los widgets
import sys #libreria del sistema


app=QApplication(sys.argv)

ventana=QWidget()
ventana.show()

sys.exit(app.exec_())   #ventana main loop