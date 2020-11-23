from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot #Identificar cuando se ejecute el evento del boton
from ui_mainwindow import Ui_MainWindow #Importar libreria de la interfaz del designer en .py
from Actividad09_Particulas.particula import Particula
from Actividad09_Particulas.adminparticula import AdminParticula
#from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.particulas = AdminParticula() #instancia en la clase MainWindow
        
        self.ui = Ui_MainWindow() #crear un objeto de una vista del designer
        self.ui.setupUi(self) #Las configuraciones que se hacen se incrustan en el objeto
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio) #Decirle que cuando le de click se conecte a la función
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar) #Conectar el evento del boton a la función
        
        #Conectar eventos al presionar respectivos botones abrir y guardar 
        #Triggered -> Disparó
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        
        #Conexión a botones tabla
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.action_mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.action_buscar_id)
        
        #Conexión a botones dibujar
        self.ui.draw_pushButton.clicked.connect(self.action_dibujar)
        self.ui.clear_pushButton.clicked.connect(self.action_limpiar)
        
        #Crear Escena
        self.scene = QGraphicsScene() #Crear escena
        self.ui.graphicsView.setScene(self.scene) #Insertar scene
        
        #Button sort Plane and Edit
        self.ui.sort_plane_pushButton.clicked.connect(self.action_sort_plane)
    
    #Odenamientos sort()
    @Slot()
    def action_sort_plane(self):
        if self.ui.desicion_plane_comboBox.currentText() == "Id (ascendente)":
            self.particulas.sort_id()
        elif self.ui.desicion_plane_comboBox.currentText() == "Distancia (descendente)":
            self.particulas.sort_distancia()
        elif self.ui.desicion_plane_comboBox.currentText() == "Velocidad (ascendente)":
            self.particulas.sort_velocidad()
        else:
            return -1
        if len(self.particulas) > 0:
            QMessageBox.information(
                    self,
                    "Éxito",
                    "Se ordeno con éxito"
                )
        
    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)    
        
    @Slot()
    def action_dibujar(self):
        if len(self.particulas) > 0:
            pen = QPen() #Definir una pluma
            pen.setWidth(2) #Tamaño en pixelex del ancho de la pluma
            #Ingresar el color
            for particula in self.particulas:
                color = QColor(particula.red, particula.green, particula.blue)
                pen.setColor(color)
                
                self.scene.addEllipse(particula.origen_x, particula.origen_y, 3, 3, pen) #Dibujar un elipse -> (0, 0, 3, 3) ->posX, posY, radio, radio
                self.scene.addEllipse(particula.destino_x, particula.destino_y, 3, 3, pen)
                self.scene.addLine(particula.origen_x, particula.origen_y, particula.destino_x, particula.destino_y, pen) #Agregar linea entre los dos elipses
                
        else:
            QMessageBox.warning(
                self, 
                "Atención",
                'No hay partículas registradas'
            )
                
    @Slot()
    def action_limpiar(self):
        self.scene.clear()
        #Reestablecer la escala al predeterminado
        self.ui.graphicsView.setTransform(QTransform())
    
    @Slot()  
    def action_buscar_id(self):        
        busca_id = self.ui.buscar_lineEdit.text() #Obtener el texto del lineEdit
        if(len(busca_id) > 0):
            busca_id = int(busca_id)
        
        encontrado = False
        for particula in self.particulas:
            if busca_id == particula.id:
                self.ui.table.clear() #Limpiar tabla
                self.table_add_column()
                self.ui.table.setRowCount(1)
                
                self.table_widget(0, particula)
                
                encontrado = True
                return              
    
        if not encontrado:
            QMessageBox.warning(
                self, 
                "Atención",
                f'La partícula con el id "{busca_id}" no fue encontrada'
            )
        
    @Slot()
    def action_mostrar_tabla(self):
        self.table_add_column()
        self.ui.table.setRowCount(len(self.particulas)) #Agregar filas a la tabla
        
        row = 0 #Contador de filas
        for particula in self.particulas:
            self.table_widget(row, particula)
            row += 1
     
    def table_widget(self, row, particula:Particula):
        #construcción de Widgets
        id_widget = QTableWidgetItem(str(particula.id))
        origen_x_widget = QTableWidgetItem(str(particula.origen_x))
        origen_y_widget = QTableWidgetItem(str(particula.origen_y))
        destino_x_widget = QTableWidgetItem(str(particula.destino_x))
        destino_y_widget = QTableWidgetItem(str(particula.destino_y))
        velocidad_widget = QTableWidgetItem(str(particula.velocidad))
        red_widget = QTableWidgetItem(str(particula.red))
        green_widget = QTableWidgetItem(str(particula.green))
        blue_widget = QTableWidgetItem(str(particula.blue))
        distancia_widget = QTableWidgetItem(str(particula.distancia))
            
        #Ingresar información en la tabla
        self.ui.table.setItem(row, 0, id_widget)
        self.ui.table.setItem(row, 1, origen_x_widget)
        self.ui.table.setItem(row, 2, origen_y_widget)
        self.ui.table.setItem(row, 3, destino_x_widget)
        self.ui.table.setItem(row, 4, destino_y_widget)
        self.ui.table.setItem(row, 5, velocidad_widget)
        self.ui.table.setItem(row, 6, red_widget)
        self.ui.table.setItem(row, 7, green_widget)
        self.ui.table.setItem(row, 8, blue_widget)
        self.ui.table.setItem(row, 9, distancia_widget)
            
        
    def table_add_column(self):
        self.ui.table.setColumnCount(10) #Generar columnas en la tabla
        #Nombre de los headers en una lista
        headers = ["Id", "Origen x", "Origen y", "Destino x", "Destino y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.table.setHorizontalHeaderLabels(headers) #Ingresar el nombre de las columnas
        
        
    @Slot()
    def action_abrir_archivo(self):  
        #print("Abrir archivo")
        ubicacion = QFileDialog.getOpenFileName( #Regresa ubicación del archivo modo de apertura
            self,
            'Abrir Archivo',
            '.', #Decirle desde la carpeta que se esta trabajando
            'JSON (*.json)'
        )[0] 
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )
            
    @Slot()
    def action_guardar_archivo(self):
        #print('Guardar Archivo')
        ubicacion = QFileDialog.getSaveFileName( #Método para regresar la ubicación
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0] #pirmera posición de la tupla
        #print(ubicacion)
        if self.particulas.guardar(ubicacion): #invocar método de AdminParticula()
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )
    
    def limpiar(self):
        self.ui.id_spinBox.setValue(0)
        self.ui.origenx_spinBox.setValue(0)
        self.ui.origeny_spinBox.setValue(0)
        self.ui.destinox_spinBox.setValue(0)
        self.ui.destinoy_spinBox.setValue(0)
        self.ui.velocidad_spinBox.setValue(0)
        self.ui.red_spinBox.setValue(0)
        self.ui.green_spinBox.setValue(0)
        self.ui.blue_spinBox.setValue(0)  
        
    def entrada_datos(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        
        return particula

    @Slot() #Decirle que la siguiente función detectara eventos click
    def click_agregar_inicio(self):
        self.particulas.agregar_inicio(self.entrada_datos())
        self.limpiar()
        
    @Slot()
    def click_agregar_final(self):
        self.particulas.agregar_final(self.entrada_datos())
        self.limpiar()
    
    @Slot()
    def mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))
        #Grafo
        self.particulas.mandar_particulas_grafo()
        self.ui.salida_plainTextEdit.clear()    
        self.ui.salida_plainTextEdit.insertPlainText(self.particulas.get_grafo())
        print(self.particulas.get_grafo())    