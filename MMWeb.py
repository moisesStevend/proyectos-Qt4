import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import QWebView

class MMWeb(QWidget):
    def __init__(self):
        QWidget.__init__(self) 
        vbox=QVBoxLayout(self)    
        
        self.btnBack=QPushButton(self.style().standardIcon(QStyle.SP_ArrowBack),'') #ponemos el texto en bacio
        self.btnForward=QPushButton(self.style().standardIcon(QStyle.SP_ArrowForward),'')
        self.btnReload=QPushButton(self.style().standardIcon(QStyle.SP_BrowserReload),'')
        self.btnStop=QPushButton(self.style().standardIcon(QStyle.SP_BrowserStop),'')
        self.lineUrl=QLineEdit()
        self.btnOk=QPushButton(self.style().standardIcon(QStyle.SP_DialogOkButton),'')
        
        hbox=QHBoxLayout(self)
        hbox.addWidget(self.btnBack)
        hbox.addWidget(self.btnForward)
        hbox.addWidget(self.btnReload)
        hbox.addWidget(self.btnStop) 
        hbox.addWidget(self.lineUrl)
        hbox.addWidget(self.btnOk)
        
        vbox.addLayout(hbox)  
        
        self.web=QWebView(self)
        self.web.load(QUrl('http://google.com'))
        vbox.addWidget(self.web)  
        
        self.status=QStatusBar(self)
        self.status.addWidget(QLabel('Loading ...'))

        self.prog=QProgressBar(self)
        self.status.addWidget(self.prog) 
        vbox.addWidget(self.status)  
        
        self.connect(self.btnBack, SIGNAL('clicked()'),self.web.back)
        self.connect(self.btnForward, SIGNAL('clicked()'),self.web.forward) 
        self.connect(self.btnReload, SIGNAL('clicked()'),self.web.reload) 
        self.connect(self.btnStop, SIGNAL('clicked()'),self.web.stop)  
        self.connect(self.web, SIGNAL("loadStarted()"),self.status.show)
        self.connect(self.web,SIGNAL("loadProgress(int)"),self.prog.setValue)

app = QApplication(sys.argv)
        
v=MMWeb()
v.show()

sys.exit(app.exec_())