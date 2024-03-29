import time
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, QObject


class DoSomething(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        time.sleep(3)
        self.emit(SIGNAL('some_signal'))


def signalHandler():
    # We got signal!
    print 'Got signal!'
    sys.exit(0)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # Create new thread object.
    d = DoSomething()

    # Connect signalHandler function with some_signal which 
    # will be emited by d thread object.
    QObject.connect(d, SIGNAL('some_signal'), signalHandler, QtCore.Qt.QueuedConnection)

    # Start new thread.
    d.start()
    i=10
    for j in range(10):
        print "hola"
        time.sleep(2)
    app.exec_()
