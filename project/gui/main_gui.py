# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(926, 702)
        MainWindow.setMaximumSize(QSize(2000, 2000))
        MainWindow.setStyleSheet(u"background-color: rgb(4, 1, 20);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 861, 611))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.frame)

        self.frame1 = QFrame(self.widget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"background-color: none;\n"
"\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame1)

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setEnabled(True)
        self.widget1.setMaximumSize(QSize(16777215, 70))
        self.widget1.setStyleSheet(u"background-color: rgb(0, 0, 8);\n"
"border: 1px solid rgb(0, 0, 8);\n"
"border-radius: 15%;\n"
"\n"
"padding: 0;")
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame2 = QFrame(self.widget1)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setStyleSheet(u"border: 1.2px solid rgba(255, 255, 255, 50);\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.frame2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border: 1.5 px solid rgba(255, 255, 255, 30);")
        icon = QIcon()
        icon.addFile(u":/icon/icons/upload_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_6.addWidget(self.frame2)

        self.frame_2 = QFrame(self.widget1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: 1.2px solid rgba(255, 255, 255, 50);")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"border: 1.5 px solid rgba(255, 255, 255, 30);")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/wand_shine_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(32, 32))
        self.pushButton_4.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.horizontalLayout_6.addWidget(self.frame_2)

        self.frame3 = QFrame(self.widget1)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setStyleSheet(u"border: 1.2px solid rgba(255, 255, 255, 50);")
        self.horizontalLayout_4 = QHBoxLayout(self.frame3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"border: 1.5 px solid rgba(255, 255, 255, 30);")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/download_2_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton_5)


        self.horizontalLayout_6.addWidget(self.frame3)


        self.verticalLayout.addWidget(self.widget1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 926, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Before", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"After", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Photo Before", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Photo After", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Enhance", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

