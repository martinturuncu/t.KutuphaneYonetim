import sys
import requests
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QWidget, QStackedWidget, QListWidget, QListWidgetItem, QMessageBox,
    QCalendarWidget, QHBoxLayout
)
from PyQt6.QtGui import QColor, QFont, QPalette, QPixmap, QIcon
from PyQt6.QtCore import Qt

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.username_label = QLabel("Kullanıcı Adı:", self)
        self.username_label.move(50, 50)
        self.username_input = QLineEdit(self)
        self.username_input.move(150, 50)

        self.password_label = QLabel("Şifre:", self)
        self.password_label.move(50, 100)
        self.password_input = QLineEdit(self)
        self.password_input.move(150, 100)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Giriş Yap", self)
        self.login_button.move(150, 150)
        self.login_button.clicked.connect(self.login)

        self.status_label = QLabel(self)
        self.status_label.move(150, 200)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Kullanıcı adı ve şifre kontrolü
        if username == "kullanici" and password == "sifre":
            self.status_label.setText("Giriş Başarılı!")
            self.status_label.setStyleSheet("color: green")
            self.window().show_library()
        else:
            self.status_label.setText("Hatalı Kullanıcı Adı veya Şifre!")
            self.status_label.setStyleSheet("color: red")

class BookDetails(QWidget):
    def __init__(self, book_title):
        super().__init__()

        self.setWindowTitle("Kitap Detayları")
        self.setGeometry(100, 100, 600, 300)

        self.book_title = book_title

        self.back_button = QPushButton("Geri", self)
        self.back_button.move(10, 10)
        self.back_button.clicked.connect(self.go_to_library)

        self.borrow_button = QPushButton("Ödünç Al", self)
        self.borrow_button.move(300, 250)
        self.borrow_button.clicked.connect(self.borrow_book)

        self.return_button = QPushButton("İade Et", self)
        self.return_button.move(400, 250)
        self.return_button.clicked.connect(self.return_book)

        self.book_label = QLabel(f"<b>{self.book_title}</b>", self)
        self.book_label.move(50, 50)
        self.book_label.setFont(QFont("Arial", 14))  # Kitap adı fontunu büyüt

        self.author_label = QLabel("Yazar: Bilinmiyor", self)
        self.author_label.move(50, 80)

        self.publisher_label = QLabel("Yayın Evi: Bilinmiyor", self)
        self.publisher_label.move(50, 110)

        self.year_label = QLabel("Basım Yılı: Bilinmiyor", self)
        self.year_label.move(50, 140)

        self.cover_label = QLabel(self)
        self.cover_label.move(400, 50)
        self.cover_label.setFixedSize(150, 200)

    def go_to_library(self):
        self.window().show_library()

    def borrow_book(self):
        QMessageBox.information(self, "Ödünç Alma", f"{self.book_title} kitabı ödünç alındı.")

    def return_book(self):
        QMessageBox.information(self, "İade Etme", f"{self.book_title} kitabı iade edildi.")

class LibrarySystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kütüphane Yönetim Sistemi")
        self.setGeometry(100, 100, 800, 400)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_screen = LoginScreen()
        self.login_screen.setStyleSheet("background-color: #333; color: white")
        self.stacked_widget.addWidget(self.login_screen)

        self.library_screen = QWidget()
        self.library_layout = QHBoxLayout()
        self.library_screen.setLayout(self.library_layout)
        self.stacked_widget.addWidget(self.library_screen)

        self.books_list = QListWidget()
        self.books_list.setStyleSheet("""
            background-color: #001F3F;
            color: white;
            font-size: 18px;  /* Kitap adları için font boyutunu büyüt */
        """)
        self.books_list.itemClicked.connect(self.show_book_details)
        self.library_layout.addWidget(self.books_list)

        self.show()

    def show_library(self):
        self.stacked_widget.setCurrentIndex(1)
        self.populate_books()

    def populate_books(self):
        books = [
            "1984",
            "Bülbülü Öldürmek",
            "Sefiller",
            "Harry Potter ve Felsefe Taşı",
            "Dönüşüm",
            "Yeraltından Notlar"
        ]
        self.books_list.clear()
        for book in books:
            item = QListWidgetItem(book)
            item.setForeground(QColor("white"))
            self.books_list.addItem(item)

    def show_book_details(self, item):
        book_title = item.text()
        self.book_details = BookDetails(book_title)
        self.stacked_widget.addWidget(self.book_details)
        self.stacked_widget.setCurrentWidget(self.book_details)
        self.fetch_book_info(book_title)

    def fetch_book_info(self, book_title):
        book_info = {
            "1984": {"author": "George Orwell", "publisher": "Yayınevi A", "year": "1949", "cover_url": "https://i.dr.com.tr/cache/600x600-0/originals/0000000064038-1.jpg"},
            "Bülbülü Öldürmek": {"author": "Harper Lee", "publisher": "Yayınevi B", "year": "1960", "cover_url": "https://via.placeholder.com/150"},
            "Sefiller": {"author": "Victor Hugo", "publisher": "Yayınevi C", "year": "1862", "cover_url": "https://via.placeholder.com/150"},
            "Harry Potter ve Felsefe Taşı": {"author": "J.K. Rowling", "publisher": "Yayınevi D", "year": "1997", "cover_url": "https://via.placeholder.com/150"},
            "Dönüşüm": {"author": "Franz Kafka", "publisher": "Yayınevi E", "year": "1915", "cover_url": "https://via.placeholder.com/150"},
            "Yeraltından Notlar": {"author": "Fyodor Dostoyevski", "publisher": "Yayınevi F", "year": "1864", "cover_url": "https://via.placeholder.com/150"}
        }
        info = book_info.get(book_title)
        if info:
            self.book_details.author_label.setText(f"Yazar: {info['author']}")
            self.book_details.publisher_label.setText(f"Yayın Evi: {info['publisher']}")
            self.book_details.year_label.setText(f"Basım Yılı: {info['year']}")
            response = requests.get(info['cover_url'])
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.book_details.cover_label.setPixmap(pixmap)
            self.book_details.cover_label.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    palette = app.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#001F3F"))  # Koyu mavi tema
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    app.setPalette(palette)

    window = LibrarySystem()
    window.show()
    sys.exit(app.exec())
