Kütüphane Yönetim Sistemi
Bu PyQt6 tabanlı bir kütüphane yönetim sistemidir. Kullanıcılar, kitapları listeleyebilir, kitap detaylarını görüntüleyebilir, kitapları ödünç alabilir ve iade edebilirler.

Modüller ve Sınıflar
LoginScreen Sınıfı:
Giriş ekranını oluşturur.
Kullanıcı adı ve şifre girişi yapılabilir.
Giriş yap butonuna tıklanarak kullanıcı kimlik doğrulaması yapılır.
BookDetails Sınıfı:
Kitap detaylarını gösteren pencereyi oluşturur.
Geri, Ödünç Al ve İade Et butonlarıyla etkileşim sağlanabilir.
LibrarySystem Sınıfı:
Ana pencereyi oluşturur ve diğer ekranları yönetir.
Kullanıcı girişini sağlar.
Kütüphane ekranını ve kitap detaylarını gösterir.
LoginScreen Sınıfı
Metodlar:
__init__(self):
Giriş ekranı arayüzünü oluşturur.
Kullanıcı adı, şifre girişi ve giriş butonunu içerir.
login(self):
Kullanıcı girişini doğrular.
Başarılı veya başarısız giriş durumlarına göre geri bildirim sağlar.
BookDetails Sınıfı
Metodlar:
__init__(self, book_title):
Kitap detayları ekranını oluşturur.
Kitap başlığına göre bilgileri görüntüler.
go_to_library(self):
Kullanıcıyı kütüphane ekranına yönlendirir.
borrow_book(self):
Seçilen kitabı ödünç alır.
return_book(self):
Ödünç alınan kitabı iade eder.
LibrarySystem Sınıfı
Metodlar:
__init__(self):
Ana pencereyi oluşturur.
Kullanıcı giriş ekranını ve kütüphane ekranını içerir.
Kullanıcı arayüzünü ayarlar.
show_library(self):
Kullanıcıyı kütüphane ekranına yönlendirir.
populate_books(self):
Kitapları kütüphane ekranında listeler.
show_book_details(self, item):
Seçilen kitabın detaylarını gösterir.
fetch_book_info(self, book_title):
Seçilen kitabın bilgilerini API'den alır ve görüntüler.
Ana Uygulama
if __name__ == "__main__"::
Uygulamayı başlatır.
PyQt6 uygulama nesnesi oluşturur.
Kullanıcı arayüzü temasını ve rengini ayarlar.
LibrarySystem sınıfını başlatır ve ana pencereyi gösterir.
