#!/usr/bin/python
#-*-encoding:utf8-*-
from PyQt4.QtGui import *
import sys

class Ventana(QWidget):
    def __init__(self):
        self.a=0b00000000
        self.b=0b00000000
        self.c=0b00000000
        self.d=0b00000000
        self.e=0b00000000
        self.f=0b00000000
        self.g=0b00000000
        
        self.sum=0
        self.n='0' #str(self.label.toPlainText())
        QWidget.__init__(self)
        self.setWindowTitle("DISPLAY")
        self.setWindowIcon(QIcon("/home/meza/7seg_pinouts.png"))
        
        self.btn1=QPushButton("adquirir",self)   
        self.btn1.setFixedSize(80, 30)    
        self.btn1.clicked.connect(self.adquirir)
        
        self.btn2=QPushButton("borrar")
        self.btn2.setFixedSize(80, 30)    
        self.btn2.clicked.connect(self.borrar)
        
        self.btn3=QPushButton("setear")
        self.btn3.setFixedSize(80, 30)    
        self.btn3.clicked.connect(self.setear)
        
        self.lv0=QVBoxLayout(self)
        #self.lv0.setSpacing(0)
        self.setLayout(self.lv0)

        #self.container=QFrame(self)
        #self.container.setFixedSize(300,200)
        #self.container.setObjectName("myWidget")
        #self.container.setStyleSheet("#myWidget {background-color:red;}")
        
        self.lh1=QHBoxLayout(self)
        #self.container.setLayout(self.lh1)
        self.lv0.addLayout(self.lh1)
#####################################################        
        
        self.la = QPushButton('a', self)
        self.la.setFixedSize(40, 20)
        self.la.setCheckable(True)       
        self.la.clicked[bool].connect(self.set_a)
        
        self.lb = QPushButton('b', self)
        self.lb.setFixedSize(20, 40)#x,y
        self.lb.setCheckable(True)       
        self.lb.clicked[bool].connect(self.set_b)
        
        self.lc = QPushButton('c', self)
        self.lc.setFixedSize(20, 40)
        self.lc.setCheckable(True)       
        self.lc.clicked[bool].connect(self.set_c)
        
        self.ld = QPushButton('d', self)
        self.ld.setFixedSize(40, 20)
        self.ld.setCheckable(True)       
        self.ld.clicked[bool].connect(self.set_d)
        
        self.le= QPushButton('e', self)
        self.le.setFixedSize(20, 40)
        self.le.setCheckable(True)       
        self.le.clicked[bool].connect(self.set_e)
        
        self.lf = QPushButton('f', self)
        self.lf.setFixedSize(20, 40)
        self.lf.setCheckable(True)       
        self.lf.clicked[bool].connect(self.set_f)
        
        self.lg = QPushButton('g', self)
        self.lg.setFixedSize(40, 20)
        self.lg.setCheckable(True)       
        self.lg.clicked[bool].connect(self.set_g)
        
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        #self.gridLayout.setRowStretch(0,10)
        self.gridLayout.addWidget(self.la,0,1)
        self.gridLayout.addWidget(self.lb,1,2)
        self.gridLayout.addWidget(self.lc,3,2)
        self.gridLayout.addWidget(self.ld,4,1)
        self.gridLayout.addWidget(self.le,3,0)
        self.gridLayout.addWidget(self.lf,1,0)
        self.gridLayout.addWidget(self.lg,2,1)
        
#         self.container=QFrame(self)
#         self.container.setFixedSize(200,100)
#         self.container.setObjectName("myWidget")
#         self.container.setStyleSheet("#myWidget {background-color:red;}")
#         self.container.setLayout(self.gridLayout)
        
        self.lh1.addLayout(self.gridLayout)
######################################################

        self.lv1=QVBoxLayout(self)
#         
#         self.container=QFrame(self)
#         self.container.setFixedSize(200,100)
#         self.container.setObjectName("myWidget")
#         self.container.setStyleSheet("#myWidget {background-color:red;}")
#         self.container.setLayout(self.lv1)
        
        self.lv1.addWidget(self.btn1)
        self.lv1.addWidget(self.btn2)
        self.lv1.addWidget(self.btn3)
        self.lh1.addLayout(self.lv1)   #poner segundo
####################################################
        #self.label=QLabel(self)
        self.label=QTextEdit(self)
        self.label.textChanged.connect(self.cambio)
        self.label.setFixedSize(200,40)
#         self.container=QFrame(self)
#         self.container.setFixedSize(200,200)
#         self.container.setObjectName("myWidget")
#         self.container.setStyleSheet("#myWidget {background-color:blue;}")
#         self.container.setLayout(self.lv0)
#         
        self.label.setText("0b00000000")
        self.label.setFont(QFont('SansSerif', 16))
        self.label.setObjectName("myWidget")
        self.label.setStyleSheet("#myWidget {background-color:white;}")
        self.lv0.addWidget(self.label)    
    
    def adquirir(self):
        self.sum=0b10000000|self.a|self.b|self.c|self.d|self.e|self.f|self.g
        self.sum=str(bin(self.sum))
        self.m=self.sum.replace('1', '0',1)
        print self.sum,type(self.sum),self.m,type(self.m)
        self.label.setText(self.m)
    
    def borrar(self):
        self.sum=0b10000000
        self.la.setChecked(False)
        self.lb.setChecked(False)
        self.lc.setChecked(False)
        self.ld.setChecked(False)
        self.le.setChecked(False)
        self.lf.setChecked(False)
        self.lg.setChecked(False)
        self.label.setText("0b00000000")

        self.a=0
        self.b=0
        self.c=0
        self.d=0
        self.e=0
        self.f=0
        self.g=0
        
    def set_a(self,pressed):
        pres=0
        if pressed:
            pres=1
            print "presionado"
        else:
            pres=0
            print "nou"
        self.a=pres<<0
        
    def set_b(self,pressed):
        pres=0
        if pressed:
            pres=1
            print "presionado"
        else:
            pres=0
            print "nou"
        self.b=pres<<1
    
    def set_c(self,pressed):
        pres=0
        if pressed:
            pres=1
            print "presionado"
        else:
            pres=0
            print "nou"
        self.c=pres<<2
    
    def set_d(self,pressed):
        pres=0
        if pressed:
            pres=1
            print "presionado"
        else:
            pres=0
            print "nou"
        self.d=pres<<3 
    
    def set_e(self,pressed):
        pres=0
        if pressed:
            pres=1
            print "presionado"
        else:
            pres=0
            print "nou"
        self.e=pres<<4 
    
    def set_f(self,pressed):
        pres=0
        if pressed:
            pres=1
            print "presionado"
        else:
            pres=0
            print "nou"
        self.f=pres<<5
    def set_g(self,pressed):
        pres=0
        if pressed:
            pres=1
            print "presionado"
        else:
            pres=0
            print "nou"
        self.g=pres<<6   
    
    def setear(self):
        self.la.setChecked(False)
        self.lb.setChecked(False)
        self.lc.setChecked(False)
        self.ld.setChecked(False)
        self.le.setChecked(False)
        self.lf.setChecked(False)
        self.lg.setChecked(False)
        
        print self.label.toPlainText(),type(self.label.toPlainText())
        self.n=str(self.label.toPlainText())
        
        self.la.setChecked(int(self.n[-1]))
        self.lb.setChecked(int(self.n[-2]))
        self.lc.setChecked(int(self.n[-3]))
        self.ld.setChecked(int(self.n[-4]))
        self.le.setChecked(int(self.n[-5]))
        self.lf.setChecked(int(self.n[-6]))
        self.lg.setChecked(int(self.n[-7]))
        
    def cambio(self):
        print "cambio",len(str(self.label.toPlainText()))
        print str(self.label.toPlainText())

        if(len(str(self.label.toPlainText()))>10):
            print str(self.label.toPlainText())
            print self.label.setText(str(self.label.toPlainText())[:-1])
            self.label.setTextCursor(10)
        elif(len(str(self.label.toPlainText()))<2):
            self.label.setText(str("0b"))
            
               
         
app = QApplication(sys.argv)
        
v=Ventana()
v.show()

sys.exit(app.exec_())