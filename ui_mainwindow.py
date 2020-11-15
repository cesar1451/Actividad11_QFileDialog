# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(601, 512)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        font = QFont()
        self.actionAbrir.setFont(font)
        self.actionAbrir.setShortcutContext(Qt.WindowShortcut)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.origeny_spinBox = QSpinBox(self.groupBox)
        self.origeny_spinBox.setObjectName(u"origeny_spinBox")
        self.origeny_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.origeny_spinBox, 3, 2, 1, 2)

        self.destinox_spinBox = QSpinBox(self.groupBox)
        self.destinox_spinBox.setObjectName(u"destinox_spinBox")
        self.destinox_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.destinox_spinBox, 4, 2, 1, 2)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(99999)

        self.gridLayout_2.addWidget(self.velocidad_spinBox, 6, 2, 1, 2)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")
        self.mostrar_pushButton.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.mostrar_pushButton, 11, 0, 1, 4)

        self.origenx_spinBox = QSpinBox(self.groupBox)
        self.origenx_spinBox.setObjectName(u"origenx_spinBox")
        self.origenx_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.origenx_spinBox, 1, 2, 1, 2)

        self.destinoy_spinBox = QSpinBox(self.groupBox)
        self.destinoy_spinBox.setObjectName(u"destinoy_spinBox")
        self.destinoy_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.destinoy_spinBox, 5, 2, 1, 2)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.blue_spinBox = QSpinBox(self.groupBox_2)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.blue_spinBox, 3, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox_2)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.green_spinBox, 2, 1, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox_2)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setFrameShadow(QFrame.Plain)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 7, 0, 1, 4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 2)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMouseTracking(False)
        self.id_spinBox.setTabletTracking(False)
        self.id_spinBox.setFocusPolicy(Qt.WheelFocus)
        self.id_spinBox.setAcceptDrops(False)
        self.id_spinBox.setLayoutDirection(Qt.LeftToRight)
        self.id_spinBox.setAutoFillBackground(False)
        self.id_spinBox.setWrapping(False)
        self.id_spinBox.setMinimum(0)
        self.id_spinBox.setMaximum(99999)
        self.id_spinBox.setDisplayIntegerBase(10)

        self.gridLayout_2.addWidget(self.id_spinBox, 0, 2, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 2)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout_2.addWidget(self.agregar_final_pushButton, 9, 0, 1, 4)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout_2.addWidget(self.agregar_inicio_pushButton, 8, 0, 1, 4)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 2)

        self.sort_plane_pushButton = QPushButton(self.groupBox)
        self.sort_plane_pushButton.setObjectName(u"sort_plane_pushButton")

        self.gridLayout_2.addWidget(self.sort_plane_pushButton, 10, 0, 1, 2)

        self.desicion_plane_comboBox = QComboBox(self.groupBox)
        self.desicion_plane_comboBox.addItem("")
        self.desicion_plane_comboBox.addItem("")
        self.desicion_plane_comboBox.addItem("")
        self.desicion_plane_comboBox.setObjectName(u"desicion_plane_comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.desicion_plane_comboBox.sizePolicy().hasHeightForWidth())
        self.desicion_plane_comboBox.setSizePolicy(sizePolicy2)
        self.desicion_plane_comboBox.setTabletTracking(False)
        self.desicion_plane_comboBox.setLayoutDirection(Qt.LeftToRight)
        self.desicion_plane_comboBox.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.desicion_plane_comboBox, 10, 2, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")
        self.salida.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.salida.sizePolicy().hasHeightForWidth())
        self.salida.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(12)
        self.salida.setFont(font1)
        self.salida.setToolTipDuration(-1)
        self.salida.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.salida, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_5.addWidget(self.buscar_pushButton, 2, 1, 1, 1)

        self.table = QTableWidget(self.tab_2)
        self.table.setObjectName(u"table")

        self.gridLayout_5.addWidget(self.table, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_5.addWidget(self.buscar_lineEdit, 2, 0, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_5.addWidget(self.mostrar_tabla_pushButton, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_6.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.draw_pushButton = QPushButton(self.tab_3)
        self.draw_pushButton.setObjectName(u"draw_pushButton")

        self.gridLayout_6.addWidget(self.draw_pushButton, 1, 0, 1, 1)

        self.clear_pushButton = QPushButton(self.tab_3)
        self.clear_pushButton.setObjectName(u"clear_pushButton")

        self.gridLayout_6.addWidget(self.clear_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 601, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabWidget, self.id_spinBox)
        QWidget.setTabOrder(self.id_spinBox, self.origenx_spinBox)
        QWidget.setTabOrder(self.origenx_spinBox, self.origeny_spinBox)
        QWidget.setTabOrder(self.origeny_spinBox, self.destinox_spinBox)
        QWidget.setTabOrder(self.destinox_spinBox, self.destinoy_spinBox)
        QWidget.setTabOrder(self.destinoy_spinBox, self.velocidad_spinBox)
        QWidget.setTabOrder(self.velocidad_spinBox, self.red_spinBox)
        QWidget.setTabOrder(self.red_spinBox, self.green_spinBox)
        QWidget.setTabOrder(self.green_spinBox, self.blue_spinBox)
        QWidget.setTabOrder(self.blue_spinBox, self.agregar_inicio_pushButton)
        QWidget.setTabOrder(self.agregar_inicio_pushButton, self.agregar_final_pushButton)
        QWidget.setTabOrder(self.agregar_final_pushButton, self.sort_plane_pushButton)
        QWidget.setTabOrder(self.sort_plane_pushButton, self.desicion_plane_comboBox)
        QWidget.setTabOrder(self.desicion_plane_comboBox, self.mostrar_pushButton)
        QWidget.setTabOrder(self.mostrar_pushButton, self.salida)
        QWidget.setTabOrder(self.salida, self.table)
        QWidget.setTabOrder(self.table, self.buscar_lineEdit)
        QWidget.setTabOrder(self.buscar_lineEdit, self.buscar_pushButton)
        QWidget.setTabOrder(self.buscar_pushButton, self.mostrar_tabla_pushButton)
        QWidget.setTabOrder(self.mostrar_tabla_pushButton, self.graphicsView)
        QWidget.setTabOrder(self.graphicsView, self.draw_pushButton)
        QWidget.setTabOrder(self.draw_pushButton, self.clear_pushButton)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.desicion_plane_comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Colores (rgb):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino x:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en y: ", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x: ", None))
        self.sort_plane_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.desicion_plane_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Id (ascendente)", None))
        self.desicion_plane_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Distancia (descendente)", None))
        self.desicion_plane_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Velocidad (ascendente)", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id part\u00edcula", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.draw_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.clear_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

