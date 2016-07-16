from PyQt4.QtGui import *
import sys

class Ventana(QWidget):
    def __init__(self):
        #super(Ventana,self).__init__()
        QWidget.__init__(self)
        
        #cambia el titulo de la ventana
        self.setWindowTitle("mi primera UI")
        
        #redimensionar la ventana
        #self.resize(800,600)
        
        #mover la ventana
        self.move(200,100)
        
        #cambiar icono
        self.setWindowIcon(QIcon("dragon.jpg"))
        
        #botones
        boton1=QPushButton("boton 1",self)
        boton1.setGeometry(0,0,90,30) #coordenadas, w,h
        boton1.clicked.connect(self.imprimir)
        
        boton2=QPushButton("boton 2",self)
        boton2.move(100,0) #mover boton2 en (x,y)
        boton2.clicked.connect(self.mensaje)
        
        boton3=QPushButton("boton 3",self)
        boton3.clicked.connect(self.dialogo)
        
        #LineEdit
        line_edit=QLineEdit(self)
        line_Edit2=QLineEdit(self)
        
        #labels
        self.label1=QLabel("")
        self.label1.hide()  #ocultar mensaje
        self.label1.move(300,0)
        
        label2=QLabel("etiqueta 2",self)
        
        #layouts
        #horizontal
        layout_horizontal=QHBoxLayout(self)
        layout_horizontal.addWidget(boton1)
        layout_horizontal.addWidget(boton2)
        layout_horizontal.addWidget(self.label1)
        layout_horizontal.addWidget(line_edit)
        self.setLayout(layout_horizontal)
        
        #vertical
        layout_vertical=QVBoxLayout(self)
        layout_vertical.addWidget(boton3)
        layout_vertical.addWidget(line_Edit2)
        layout_vertical.addWidget(label2)
        layout_horizontal.addLayout(layout_vertical)
        
        #Grid layout
        btn1=QPushButton("1",self)
        btn2=QPushButton("2",self)
        btn3=QPushButton("3",self)
        btn4=QPushButton("4",self)
        
        grilla=QGridLayout(self)
        grilla.addWidget(btn1,0,0)
        grilla.addWidget(btn2,0,1)
        grilla.addWidget(btn3,1,0)
        grilla.addWidget(btn4,1,1)
        
        layout_horizontal.addLayout(grilla)
        
        
        
    def imprimir(self):
        print "hola Moises!"
    
    def mensaje(self):
        self.label1.setText("impresion yeah!!")
        self.label1.show()
    
    def dialogo(self):
        nombre=QFileDialog.getOpenFileName(self,"abrir archivo")
        print nombre
        
app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()

#main loop que mantiene viva la aplicacion
sys.exit(app.exec_())    
    