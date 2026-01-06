import sys
from pathlib import Path

import numpy as np
import tensorflow as tf

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QGraphicsDropShadowEffect,
)
from PySide6.QtGui import QImage, QPixmap, QColor
from PySide6.QtCore import Qt


# =========================
# PyInstaller / runtime path
# =========================
def resource_path(relative_path: str) -> Path:
    """
    Работает:
    - обычный python
    - PyInstaller exe
    """
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return Path(__file__).resolve().parent.parent / relative_path


# =========================
# Безопасный numpy → QImage
# =========================
def np_to_qimage(img: np.ndarray) -> QImage:
    """
    Гарантированно безопасно:
    - C-contiguous
    - Qt получает собственную копию памяти
    """
    img = np.ascontiguousarray(img)
    
    if img.ndim == 3:
        h, w, ch = img.shape
        
        if ch == 3:
            qimg = QImage(
                img.tobytes(),
                w,
                h,
                3 * w,
                QImage.Format_RGB888,
            )
        elif ch == 4:
            qimg = QImage(
                img.tobytes(),
                w,
                h,
                4 * w,
                QImage.Format_RGBA8888,
            )
        else:
            raise ValueError(f"Unsupported channels: {ch}")
    
    elif img.ndim == 2:
        h, w = img.shape
        qimg = QImage(
            img.tobytes(),
            w,
            h,
            w,
            QImage.Format_Grayscale8,
        )
    else:
        raise ValueError(f"Unsupported image shape: {img.shape}")
    
    return qimg.copy()  # 🔑 КРИТИЧЕСКИ ВАЖНО


# =========================
# Project imports
# =========================
from core.model import predict_img
from gui.main_gui import Ui_MainWindow


# =========================
# Main Window
# =========================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.current_photo: str | None = None
        self.model = None
        
        self.setup_ui()
        self.setup_logic()
        self.load_model()
    
    # =========================
    # Model loading
    # =========================
    def load_model(self):
        model_path = resource_path("core/model.keras")
        
        if not model_path.exists():
            print(f"[ERROR] Model not found: {model_path}")
            return
        
        print(f"[INFO] Loading model from: {model_path}")
        self.model = tf.keras.models.load_model(
            str(model_path),
            compile=False,  # 🔑 обязательно
        )
        print("[OK] Model loaded")
    
    # =========================
    # UI styling
    # =========================
    def setup_ui(self):
        buttons = [
            self.ui.pushButton,  # Import
            self.ui.pushButton_4,  # Enhance
            self.ui.pushButton_5,  # Save
        ]
        
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
                    padding: 6px 18px;
                }
                QPushButton:hover {
                    background-color: rgb(50,50,50);
                }
            """)
        
        self.ui.label_4.setText("Photo Before")
        self.ui.label_4.setAlignment(Qt.AlignCenter)
        self.ui.label_4.setStyleSheet(
            "background-color: rgb(50,50,50); color: white;"
        )
        
        self.ui.label_5.setText("Photo After")
        self.ui.label_5.setAlignment(Qt.AlignCenter)
        self.ui.label_5.setStyleSheet(
            "background-color: rgb(50,50,50); color: white;"
        )
    
    # =========================
    # Signals
    # =========================
    def setup_logic(self):
        self.ui.pushButton.clicked.connect(self.import_photo)
        self.ui.pushButton_4.clicked.connect(self.enhance_photo)
        self.ui.pushButton_5.clicked.connect(self.download_photo)
    
    # =========================
    # Import photo
    # =========================
    def import_photo(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Photo",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        
        if not file_path:
            return
        
        self.current_photo = file_path
        pixmap = QPixmap(file_path)
        
        self.ui.label_4.setPixmap(
            pixmap.scaled(
                self.ui.label_4.width(),
                self.ui.label_4.height(),
                Qt.KeepAspectRatio,
            )
        )
        
        self.ui.label_5.clear()
        self.ui.label_5.setText("Photo After")
    
    # =========================
    # Enhance photo
    # =========================
    def enhance_photo(self):
        if not self.current_photo:
            print("[WARN] No photo selected")
            return
        
        if self.model is None:
            print("[ERROR] Model not loaded")
            return
        
        print("[INFO] Enhancing photo...")
        pred = predict_img(self.model, self.current_photo)
        
        # гарантия uint8
        if pred.dtype != np.uint8:
            pred = (pred * 255.0).clip(0, 255).astype(np.uint8)
        
        qimage = np_to_qimage(pred)
        
        pixmap = QPixmap.fromImage(qimage)
        self.ui.label_5.setPixmap(
            pixmap.scaled(
                self.ui.label_5.width(),
                self.ui.label_5.height(),
                Qt.KeepAspectRatio,
            )
        )
    
    # =========================
    # Save result
    # =========================
    def download_photo(self):
        pixmap = self.ui.label_5.pixmap()
        if pixmap is None:
            print("[WARN] Nothing to save")
            return
        
        default_path = str(Path.home() / "Downloads" / "result.png")
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Image",
            default_path,
            "Images (*.png *.jpg *.bmp)"
        )
        
        if file_path:
            pixmap.save(file_path)
            print(f"[OK] Saved to: {file_path}")


# =========================
# Entry point
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
