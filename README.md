# Metro Rota Bulucu

Bu proje, bir metro ağı üzerinde en hızlı rota ve en az aktarmalı rota gibi soruları çözmek için iki farklı algoritma kullanarak çözüm üretir. Proje, şehir içi ulaşımda en verimli rotaların bulunmasına yardımcı olmak için tasarlanmıştır. Kullanıcılar, başlangıç ve hedef istasyonlarını girerek en hızlı rotayı veya en az aktarmalı rotayı bulabilirler.

# Kullanılan Teknolojiler ve Kütüphaneler

Python 3: Projeyi geliştirmek için Python 3 kullanılmıştır.

heapq: Python'un standart kütüphanelerinden biri olan heapq, en hızlı rota bulmak için A* algoritmasında kullanılmaktadır. Bu kütüphane, öncelik sırasına göre verilerin işlenmesi için min-heap veri yapısını sağlar.

collections: collections modülünden deque ve defaultdict gibi veri yapılarını kullanarak, genişletilmiş bir arama algoritması olan BFS'yi optimize etmek için kullanılmıştır.

# Algoritmaların Çalışma Mantığı

1. BFS (Breadth-First Search) Algoritması
   
BFS, bir grafın en kısa yolunu bulmak için kullanılan temel bir arama algoritmasıdır. Bu algoritma, her seferinde mevcut düğümlerin tüm komşularını ziyaret ederek hedefe en kısa yoldan ulaşmayı hedefler.

BFS Algoritmasının Çalışma Adımları:

* Başlangıç istasyonundan (düğümden) itibaren tüm komşular (istasyonlar) sırasıyla ziyaret edilir.

* Ziyaret edilen her istasyon, bir önceki istasyonla bağlantı oluşturularak takip edilir.

* Bu işlem, hedef istasyon bulunana kadar devam eder.

* BFS Neden Kullanıldı? BFS, her bir istasyonun komşularına sırasıyla bakarak en az aktarmalı rotayı bulmada etkilidir. Bu algoritma, her bir istasyonun eşit maliyetli olduğunu varsayar, yani her bir istasyon arasındaki geçişin süresi aynıdır.

2. A (A-star) Algoritması*

A* algoritması, en kısa yol algoritmalarından biridir ve özellikle hedefe en hızlı şekilde ulaşmayı amaçlar. A* algoritması, her düğümde iki değer hesaplar:

* g(n): Başlangıçtan mevcut düğüme kadar olan gerçek maliyet.

* h(n): Mevcut düğümden hedefe kadar olan tahmini maliyet (heuristik fonksiyon).

* A* algoritması, her iki değeri toplar ve bu toplamı minimize ederek en hızlı yolu bulur.

A* Algoritmasının Çalışma Adımları:

* Başlangıç istasyonundan (düğümden) hedef istasyona kadar olan yollar hesaplanır.

* Her düğüm için tahmin edilen maliyet ve mevcut maliyet hesaplanarak öncelik kuyruğuna eklenir.

* Öncelik kuyruğunda en düşük maliyete sahip düğüm seçilir ve bu düğümün komşuları keşfedilir.

Hedef istasyon bulunana kadar işlem devam eder.

A* Neden Kullanıldı?

A* algoritması, her bir istasyon arasındaki geçişlerin farklı sürelerde olabileceği durumlar için daha uygun bir çözümdür. Özellikle ulaşım ağlarında zaman farklılıkları söz konusu olduğunda, A* algoritması gerçek zamanlı olarak en hızlı rotayı bulmak için etkilidir.

# Örnek Kullanım ve Test Sonuçları

Aşağıdaki örnekte, "AŞTİ" istasyonundan "Kızılay" istasyonuna en hızlı rotayı ve en az aktarmalı rotayı bulacağız.

metro_ag = MetroAg()

#İstasyonlar ekleniyor

metro_ag.istasyon_ekle("AŞTİ", "M1")

metro_ag.istasyon_ekle("Kızılay", "M2")

metro_ag.istasyon_ekle("Ulus", "M1")

metro_ag.istasyon_ekle("Demetevler", "M3")

metro_ag.istasyon_ekle("OSB", "M2")

#Bağlantılar ekleniyor

metro_ag.baglanti_ekle("AŞTİ", "Kızılay", 10)

metro_ag.baglanti_ekle("Kızılay", "Ulus", 5)

metro_ag.baglanti_ekle("Ulus", "Demetevler", 20)

metro_ag.baglanti_ekle("Demetevler", "OSB", 15)

# En hızlı rota

rota, sure = metro_ag.en_hizli_rota_bul("AŞTİ", "OSB")

print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.idx for i in rota))

# En az aktarmalı rota

rota, aktarma_sayisi = metro_ag.en_az_aktarmali_rota_bul("AŞTİ", "OSB")

print(f"En az aktarmalı rota ({aktarma_sayisi} aktarma):", " -> ".join(i.idx for i in rota))

Test Sonuçları:

* En Hızlı Rota (AŞTİ -> OSB):

* AŞTİ -> Kızılay -> Demetevler -> OSB (30 dakika)

* En Az Aktarmalı Rota (AŞTİ -> OSB):

* AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB (5 aktarma)

# Projeyi Geliştirme Fikirleri

* Zaman Hesaplaması ve Gerçek Zamanlı Güncellemeler: Ulaşım sistemindeki trafik yoğunluğu gibi veriler eklenerek, rotalar gerçek zamanlı olarak güncellenebilir.

* Kullanıcı Dostu Arayüz: Bir grafiksel kullanıcı arayüzü (GUI) ile kullanıcıların metro rotalarını daha kolay bir şekilde seçmesi sağlanabilir.

* Mobil Uygulama Entegrasyonu: Bu projeyi bir mobil uygulamaya entegre ederek, şehirdeki metro sistemini kullanan kişilere daha pratik bir deneyim sunulabilir.

* Farklı Algoritmaların Denenmesi: Daha büyük ve karmaşık ağlar için, Dijkstra gibi diğer kısa yol algoritmaları da test edilebilir ve karşılaştırılabilir.
