#!/usr/bin/python
#-*-encoding:utf8-*-
from PyQt4.QtGui import *
import commands as c
import sys
import serial

class Ventana(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("RECONOCIENDO PUERTOS SERIALES")
        self.setWindowIcon(QIcon("/home/meza/workspace/qt4/dragon.jpg"))
        
        self.btn1=QPushButton("Actualizar",self)
        self.btn1.clicked.connect(self.actualizarSerial)
        self.btn2=QPushButton("Enviar")
        self.btn2.clicked.connect(self.enviar)
        self.btn2.setEnabled(False)        
        
        self.btn3=QPushButton("Conectar",self)
        self.btn3.setFixedHeight(80)
        self.btn3.setFixedWidth(120)
        self.btn3.clicked.connect(self.conectarSerial)
        
        self.btn3.setIcon(QIcon('/home/meza/workspace/qt4/on.png'))
        
        self.puerto="ls /dev/ttyS*"
        self.combo=QComboBox(self)  
        self.combo.setFixedWidth(140)
        self.combo.currentIndexChanged.connect(self.conectarSerial2)
        self.habilitarPuerto=False
        
        self.check1=QCheckBox("ACM",self)
        self.check1.clicked.connect(self.elegirSerial)
        self.check2=QCheckBox("USB",self)
        self.check2.clicked.connect(self.elegirSerial)
        self.check3=QCheckBox("rfcomm",self)
        self.check3.clicked.connect(self.elegirSerial)
        
        self.lineaEdit=QLineEdit(self)
        self.lineaEdit.setEnabled(False)
        
        self.lH=QHBoxLayout(self)
        self.setLayout(self.lH)
        
        self.lV1=QVBoxLayout(self)
        self.lV1.addWidget(self.check1)
        self.lV1.addWidget(self.check2)
        self.lV1.addWidget(self.check3)
        self.lH.addLayout(self.lV1)
        
        self.lV2=QVBoxLayout(self)       
        self.lH.addLayout(self.lV2)
        
        self.lH2=QHBoxLayout(self)
        self.lH2.addWidget(self.btn1)
        self.lH2.addWidget(self.combo)
        self.lV2.addLayout(self.lH2)
        
        self.lH3=QHBoxLayout(self)
        self.lH3.addWidget(self.lineaEdit)
        self.lH3.addWidget(self.btn2)
        self.lV2.addLayout(self.lH3)
        
        self.lH.addWidget(self.btn3)
        
    def actualizarSerial(self):
        self.combo.clear()
        
        l=c.getoutput(self.puerto)
        self.lN=l.split('\n')    #creamos una lista

        if "ls: no se puede acceder" not in self.lN[0]:
            #para que no encuentre si no hay
            self.primerItem = "---Detectados "+str(len(self.lN))+'---'
            self.lN=[self.primerItem]+self.lN
            for i in self.lN:
                self.combo.addItem(i)
        else:
            self.btn2.setEnabled(False)
            self.lineaEdit.setEnabled(False) 
            self.habilitarPuerto=False
              
    def conectarSerial2(self):
        self.habilitarPuerto=True
    
    def conectarSerial(self): 
        if self.btn3.text() == "Conectar" and str(self.combo.currentText())!=self.primerItem and self.habilitarPuerto==True:
            #print "conectado",self.btn3.text()
            self.btn2.setEnabled(True)
            self.lineaEdit.setEnabled(True)
            self.btn3.setText("Desconectar")
            self.habilitarPuerto=False
            namePuerto = str(self.combo.currentText())
            self.ser=serial.Serial(namePuerto)
            self.btn3.setIcon(QIcon('/home/meza/workspace/qt4/off.png'))
            
        elif self.btn3.text()=="Desconectar":
            #print "desconectado",self.btn3.text()
            self.btn2.setEnabled(False)
            self.lineaEdit.setEnabled(False)
            self.btn3.setText("Conectar")
            self.ser.close()
            self.actualizarSerial()
            self.btn3.setIcon(QIcon('/home/meza/workspace/qt4/on.png'))

    def enviar(self):    
        self.ser.write(str(self.lineaEdit.text()))
        #pass
    
    def elegirSerial(self):
        if self.check1.isChecked():
            #self.check2.setChecked(False)
            self.check2.setEnabled(False)
            #self.check3.setChecked(False)
            self.check3.setEnabled(False)
            #print self.check1.text()
            self.puerto="ls /dev/ttyACM*"
        elif self.check2.isChecked():
            self.check1.setEnabled(False)
            self.check3.setEnabled(False)
            self.puerto="ls /dev/ttyUSB*" 
        elif self.check3.isChecked():
            self.check1.setEnabled(False)
            self.check2.setEnabled(False)
            self.puerto="ls /dev/rfcomm*"
        else:
            self.check1.setEnabled(True)
            self.check2.setEnabled(True)
            self.check3.setEnabled(True)
            self.puerto="ls /dev/ttyS*"

app = QApplication(sys.argv)
        
v=Ventana()
v.show()

sys.exit(app.exec_())
