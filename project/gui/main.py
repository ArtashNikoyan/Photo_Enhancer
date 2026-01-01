# main.py
import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
from main_gui import Ui_MainWindow
import res_rc  # ресурсы

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_photo = None
        self.setup_ui()
        self.setup_logic()
    
    def setup_ui(self):
        """Настраиваем кнопки, тень и отступы"""
        buttons = [self.ui.pushButton, self.ui.pushButton_4, self.ui.pushButton_5]
        for btn in buttons:
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(15)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setColor(QColor(0, 0, 0, 180))
            btn.setGraphicsEffect(shadow)
            btn.setStyleSheet("""
                QPushButton {
                    border: 1.5px solid rgba(255,255,255,30);
                    border-radius: 10px;
                    background-color: rgb(30,30,30);
                    color: white;
                    padding: 5px 15px;       /* добавляем padding внутрь кнопки */
                }
                QPushButton:hover {
                    background-color: rgb(50,50,50);
                }
            """)
        
        # Фреймы остаются прозрачными, но сохраняем отступы layout
        frames = [self.ui.frame2, self.ui.frame_2, self.ui.frame3]
        for frame in frames:
            frame.setStyleSheet("background: none; border: none;")
            layout = frame.layout()
            if layout:
                layout.setContentsMargins(8, 8, 8, 8)  # внутренние отступы
                layout.setSpacing(5)  # расстояние между виджетами внутри
        
        # Плейсхолдеры для Photo Before / After
        self.ui.label_4.setText("Photo Before")
        self.ui.label_4.setAlignment(Qt.AlignCenter)
        self.ui.label_4.setStyleSheet("background-color: rgb(50,50,50); color: white;")
        self.ui.label_5.setText("Photo After")
        self.ui.label_5.setAlignment(Qt.AlignCenter)
        self.ui.label_5.setStyleSheet("background-color: rgb(50,50,50); color: white;")

    
    def setup_logic(self):
        """Подключаем кнопки к функциям"""
        self.ui.pushButton.clicked.connect(self.import_photo)
        self.ui.pushButton_4.clicked.connect(self.enhance_photo)
        self.ui.pushButton_5.clicked.connect(self.download_photo)

    def import_photo(self):
        """Выбор фото через стандартный диалог Windows"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Photo",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.svg)"
        )
        if file_path:
            self.current_photo = file_path
            print(f"Selected file: {file_path}")

            # Показать фото в Photo Before
            pixmap = QPixmap(file_path)
            self.ui.label_4.setPixmap(pixmap.scaled(
                self.ui.label_4.width(),
                self.ui.label_4.height(),
                Qt.KeepAspectRatio
            ))
            self.ui.label_4.setStyleSheet("")  # убираем плейсхолдер

            # Очистить Photo After
            self.ui.label_5.setText("Photo After")
            self.ui.label_5.setPixmap(QPixmap())
            self.ui.label_5.setStyleSheet("background-color: rgb(50,50,50); color: white;")
            self.ui.label_5.setAlignment(Qt.AlignCenter)

    def enhance_photo(self):
        """Пока без модели — копируем Photo Before в Photo After"""
        print("Enhance clicked")
        if self.current_photo:
            pixmap = QPixmap(self.current_photo)
            self.ui.label_5.setPixmap(pixmap.scaled(
                self.ui.label_5.width(),
                self.ui.label_5.height(),
                Qt.KeepAspectRatio
            ))
            self.ui.label_5.setStyleSheet("")  # убираем плейсхолдер

    def download_photo(self):
        """Сохранение изображения из Photo After — пока только вывод"""
        print("Download clicked")
        if self.ui.label_5.pixmap():
            downloads = str(Path.home() / "Downloads")
            file_path, _ = QFileDialog.getSaveFileName(
                    self,
                    "Save Photo",
                    f"{downloads}/untitled.png",
                    "Images (*.png *.jpg *.bmp)"
            )
            if file_path:
                self.ui.label_5.pixmap().save(file_path)
                print(f"Saved to: {file_path}")
        else:
            print("No photo to save!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
