import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtWidgets import QCalendarWidget

class Hasta:
    def __init__(self, isim, tc):
        self.isim = isim
        self.tc = tc
        self.randevu_gecmisi = []  # Hasta randevu geçmişi

class Doktor:
    def __init__(self, isim, uzmanlik_alani):
        self.isim = isim
        self.uzmanlik_alani = uzmanlik_alani
        self.musaitlik_durumu = True  # True: Müsait, False: Meşgul

class Randevu:
    def __init__(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta

class HastaneRandevuSistemi:
    def __init__(self):
        self.hastalar = []
        self.doktorlar = []
        self.randevular = []

        # Debug: Eklenen hastaları ve doktorları yazdır
        print("Hastalar:")
        for hasta in self.hastalar:
            print(hasta.isim)
        print("Doktorlar:")
        for doktor in self.doktorlar:
            print(doktor.isim)

    def hasta_ekle(self, hasta):
        self.hastalar.append(hasta)

    def doktor_ekle(self, doktor):
        self.doktorlar.append(doktor)

    def randevu_al(self, hasta, doktor, tarih):
        if doktor.musaitlik_durumu:  # Doktorun müsait olup olmadığını kontrol et
            randevu = Randevu(tarih, doktor, hasta)
            self.randevular.append(randevu)
            doktor.musaitlik_durumu = False  # Doktoru meşgul olarak işaretle
            hasta.randevu_gecmisi.append(randevu)  # Hasta randevu geçmişine ekle
            return randevu
        else:
            return None  # Doktor meşgulse None döndür

    def randevu_iptal(self, randevu):
        self.randevular.remove(randevu)  # Randevuyu listeden kaldır
        randevu.doktor.musaitlik_durumu = True  # Doktoru tekrar müsait yap

class LoginScreen(QMainWindow):
    def __init__(self, hastane_sistemi):
        super().__init__()

        self.hastane_sistemi = hastane_sistemi

        self.setWindowTitle("Hastane Randevu Sistemi")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label_username = QLabel("Kullanıcı Adı:")
        layout.addWidget(self.label_username)

        self.entry_username = QLineEdit()
        layout.addWidget(self.entry_username)

        self.label_password = QLabel("Şifre:")
        layout.addWidget(self.label_password)

        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.entry_password)

        self.button_login = QPushButton("Giriş Yap")
        self.button_login.clicked.connect(self.login)
        layout.addWidget(self.button_login)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Stil Ayarları
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QLineEdit {
                background-color: #252525;
                color: #ffffff;
                border: 1px solid #ffffff;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #007acc;
                color: #ffffff;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005f80;
            }
        """)

    def login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        # Kullanıcı adı ve şifrenin doğruluğu kontrol ediliyor (örnek olarak sadece "admin" ve "password" kabul ediliyor)
        if username == "admin" and password == "password":
            QMessageBox.information(None, "Başarılı", "Giriş başarılı!")
            self.close()  # Giriş ekranını kapat
            self.randevu_sistemi_ui = RandevuSistemiUI(self.hastane_sistemi)  # Randevu sistemine geçiş yap
            self.randevu_sistemi_ui.show()
        else:
            QMessageBox.critical(None, "Hata", "Kullanıcı adı veya şifre hatalı!")


class RandevuSistemiUI(QMainWindow):
    def __init__(self, hastane_sistemi):
        super().__init__()

        self.hastane_sistemi = hastane_sistemi

        self.setWindowTitle("Hastane Randevu Sistemi")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label_hasta = QLabel("Hasta İsmi:")
        layout.addWidget(self.label_hasta)

        self.entry_hasta = QLineEdit()
        layout.addWidget(self.entry_hasta)

        self.label_doktor = QLabel("Doktor:")
        layout.addWidget(self.label_doktor)

        self.combo_doktor = QComboBox()
        self.combo_doktor.addItems([d.isim for d in self.hastane_sistemi.doktorlar])
        layout.addWidget(self.combo_doktor)

        self.label_tarih = QLabel("Randevu Tarihi:")
        layout.addWidget(self.label_tarih)

        self.calendar_widget = QCalendarWidget()
        layout.addWidget(self.calendar_widget)

        self.button_randevu_al = QPushButton("Randevu Al")
        self.button_randevu_al.clicked.connect(self.randevu_al)
        layout.addWidget(self.button_randevu_al)

        self.button_randevu_iptal = QPushButton("Randevu İptal")
        self.button_randevu_iptal.clicked.connect(self.randevu_iptal)
        layout.addWidget(self.button_randevu_iptal)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Stil Ayarları
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QLineEdit {
                background-color: #252525;
                color: #ffffff;
                border: 1px solid #ffffff;
                border-radius: 5px;
            }
            QComboBox {
                background-color: #252525;
                color: #ffffff;
                border: 1px solid #ffffff;
                border-radius: 5px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: #ffffff;
                border-left-style: solid;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
            }
            QPushButton {
                background-color: #007acc;
                color: #ffffff;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005f80;
            }
        """)

    def randevu_al(self):
        hasta_isim = self.entry_hasta.text()
        doktor_isim = self.combo_doktor.currentText()
        tarih = self.calendar_widget.selectedDate().toString("yyyy-MM-dd")

        # Hasta isminin sistemde olup olmadığını kontrol et
        hasta = next((h for h in self.hastane_sistemi.hastalar if h.isim == hasta_isim), None)
        if hasta is None:
            QMessageBox.critical(None, "Hata", "Hasta bulunamadı!")
            return

        # Doktor isminin sistemde olup olmadığını kontrol et
        doktor = next((d for d in self.hastane_sistemi.doktorlar if d.isim == doktor_isim), None)
        if doktor is None:
            QMessageBox.critical(None, "Hata", "Doktor bulunamadı!")
            return

        randevu = self.hastane_sistemi.randevu_al(hasta, doktor, tarih)
        if randevu is not None:
            QMessageBox.information(None, "Başarılı", "Randevu alındı!")
        else:
            QMessageBox.critical(None, "Hata", "Doktorun müsaitlik durumu yok!")

    def randevu_iptal(self):
        doktor_isim = self.combo_doktor.currentText()
        tarih = self.calendar_widget.selectedDate().toString("yyyy-MM-dd")

        doktor = None
        for d in self.hastane_sistemi.doktorlar:
            if d.isim == doktor_isim:
                doktor = d
                break

        if doktor is None:
            QMessageBox.critical(None, "Hata", "Doktor bulunamadı!")
            return

        # Hasta isimlerini bul
        hasta_isimler = [randevu.hasta.isim for randevu in self.hastane_sistemi.randevular if randevu.doktor.isim == doktor_isim and randevu.tarih == tarih]

        # Hasta isimlerini bir stringe dönüştür
        hasta_str = "\n".join(hasta_isimler)

        if hasta_str:
            reply = QMessageBox.question(None, "Randevu İptal", f"Aşağıdaki hastaların randevusunu iptal etmek istiyor musunuz?\n{hasta_str}", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                for randevu in self.hastane_sistemi.randevular:
                    if randevu.doktor.isim == doktor_isim and randevu.tarih == tarih:
                        self.hastane_sistemi.randevu_iptal(randevu)
                QMessageBox.information(None, "Başarılı", "Randevu(lar) iptal edildi!")
        else:
            QMessageBox.critical(None, "Hata", "Belirtilen tarihte randevu bulunamadı!")

# Test
if __name__ == "__main__":
    app = QApplication(sys.argv)
    hastane_sistemi = HastaneRandevuSistemi()
    hasta1 = Hasta("Ahmet", "123456789")
    hasta2 = Hasta("Ayşe", "987654321")
    doktor1 = Doktor("Dr. Mehmet", "Dahiliye")
    doktor2 = Doktor("Dr. Fatma", "Cerrahiye")
    hastane_sistemi.hasta_ekle(hasta1)
    hastane_sistemi.hasta_ekle(hasta2)
    hastane_sistemi.doktor_ekle(doktor1)
    hastane_sistemi.doktor_ekle(doktor2)
    login_screen = LoginScreen(hastane_sistemi)
    login_screen.show()
    sys.exit(app.exec())
