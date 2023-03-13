##08.03.2023
###PYTHON VERİ TİPLERİ

metinsel veri tipi: str #karakter tutmamıza yarar.

numeriC veri tipleri: int,float,complex #integer ile tam sayıları, float ile ondalık sayıları, complex ile karmaşık sayıları (reel ve imajiner olarak iki kısımdan oluşur) tutarız.

dizi veri tipleri: list,tuple,range #list sıralı bir değer kümesini, tuple da list ile aynı şekilde gruplanmış bir veriyi temsil eder (listten farkı tuple'ın değiştirilemez olmasıdır.), range'i belli aralıktaki sayıları göstermek amacıyla kullanırız.

mapping veri tipi: dict #key ve value şeklinde farklı key'leri bulunan verileri saklayabileceğimiz bir veri yapısıdır.

set veri tipleri: set,frozenset #set ile aslında bir küme oluşturuyoruz ve bu kümede bir elemandan yalnızca bir tane olabilir ve sıralı bir veri tipi değildir. frozenset ise kısıtlanmış bir kümedir yani bu veri türüne ekleme, silme, değiştirme gibi işlemler yapılamıyor. 

boolean veri tipi: bool #bool ile mantıksal işlemler yapılır. Sadece 'true' ve 'false' değerlerini döndürür.

binary veri tipleri: bytes,bytearray,memoryview #bytes, byte nesnesi döndürür. bytearray byte veri tipinde oluşturulan veriler üzerinde değişiklik yapmak için kullanılır. memoryview bellek durumunu görüntülemek için kullanılır.

###Sitede değişken olarak kullanılan veriler ve veri tipleri:
#Kurs sayfasındaki dersin gün ve tarihi, yorumlar string veri tipiyle tutulmuştur.
#Yine aynı sayfada kursun tamamlanma yüzdesi integer veri tipiyle tutulmuştur.


###Kodlama.io sitesindeki şart blokları:
#Sitenin girişindeki kullanıcı adı ve şifre şart bloğu ile tutulmuştur.
#Bitir ve devam et butonuna bastıkça sol tarafta kalan icon değişikliği şart bloğuyla tutulmuştur.