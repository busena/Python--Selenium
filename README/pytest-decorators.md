## PyTestdeki decoratorleri araştırarak oluşturduğunuz notları bir "ReadMe" dosyası olarak githubda paylaşınız.

PyTest bir yazılım test çerçevesidir ve çeşitli yazılım testleri için kullanılabilir. Kodlarımızı istediğimiz şekilde modifiye edebilmemizi sağlar. 

> -> **pytest.mark.skip:** > Bir test fonksiyonunu koşulsuz olarak atlamamızı sağlar.

-> **pytest.mark.skipif:** Koşul 'True' ise test fonksiyonunu atlamamızı sağlar.

-> **pytest.mark.parametrize:** Bir test için bağımsız değişkenlerin parametreleştirilmesini sağlar. Bu sayede farklı parametrelerle farklı test senaryoları çalıştırılmış olur.

-> **pytest.mark.xfail:** Bir test işlevini başarısız olması bekleniyormuş gibi işaretler.

-> **pytest.fixture:** Bir test için bağımlı ve bağımsız olduğu özellikleri yönetebileceğimiz, veri sağlayabileceğimiz işlevlerdir.

-> **pytest.mark.timeout:** Belirli bir zaman aşımı sonrasında testi sonlandırır. 

-> **pytest.exit:** Test sürecinden çıkmamızı sağlar.
