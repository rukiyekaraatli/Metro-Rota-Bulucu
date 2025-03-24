from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        if istasyon1_id not in self.istasyonlar or istasyon2_id not in self.istasyonlar:
            raise ValueError(f"Hata: '{istasyon1_id}' veya '{istasyon2_id}' istasyonlardan biri bulunamadı!")
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:

        """BFS algoritması kullanarak en az aktarmalı rotayı bulur.
    
    Parametreler:
    - baslangic_id: Başlangıç istasyonunun ID'si.
    - hedef_id: Hedef istasyonun ID'si.

    Dönüş:
    - Eğer bir rota bulunursa, istasyon listesini döndürür.
    - Eğer rota bulunamazsa, None döndürür.
        """
  
        # 1️⃣ Başlangıç ve hedef istasyonlarının varlığını kontrol et
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:

            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # 2️⃣ BFS için kuyruk başlat (Başlangıç noktasından hareketle, rota içeren tuple)
        kuyruk = deque([(baslangic, [baslangic])])

        # 3️⃣ Ziyaret edilen istasyonları takip eden küme
        ziyaret_edildi = set()

        while kuyruk:
            mevcut_istasyon, rota = kuyruk.popleft()  # Kuyruğun başındaki istasyonu al
        
            # 🚀 Hedefe ulaşıldı mı?
            if mevcut_istasyon == hedef:
                return rota  # Hedefe ulaşıldı, en kısa aktarmalı rota bulundu
        
            # 4️⃣ Komşuları kontrol et
            for komsu, _ in mevcut_istasyon.komsular:
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    kuyruk.append((komsu, rota + [komsu]))  # Yeni rotayı kuyrukta sıraya ekle

        return None  # Eğer hedefe ulaşılmazsa None döndür


    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur.
    
    Parametreler:
    - baslangic_id: Başlangıç istasyonunun ID'si.
    - hedef_id: Hedef istasyonun ID'si.

    Dönüş:
    - Eğer bir rota bulunursa, (istasyon_listesi, toplam_sure) tuple'ını döndürür.
    - Eğer rota bulunamazsa, None döndürür.
        """

        # 1️⃣ Başlangıç ve hedef istasyonlarının varlığını kontrol et
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
             raise ValueError("Geçersiz istasyon ID'si girildi!")

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
  
        # 2️⃣ Öncelik kuyruğu (heap) oluştur (süre, id, istasyon, rota)
        pq = [(0, id(baslangic), baslangic, [baslangic])]  
        heapq.heapify(pq)

        # 3️⃣ Ziyaret edilen istasyonları süre ile takip et
        ziyaret_edildi = {}

        while pq:
           
           toplam_sure, _, mevcut_istasyon, rota = heapq.heappop(pq)  # En düşük süreye sahip düğümü al

           # 🚀 Hedefe ulaşıldı mı?
           if mevcut_istasyon == hedef:
                return rota, toplam_sure  # En hızlı rota bulundu
        
            # Eğer bu istasyon daha önce ziyaret edilmemişse veya daha kısa sürede ziyaret ediliyorsa devam et
           if mevcut_istasyon in ziyaret_edildi and ziyaret_edildi[mevcut_istasyon] < toplam_sure:
                
                continue

           ziyaret_edildi[mevcut_istasyon] = toplam_sure  # Ziyaret süresini kaydet

            # 4️⃣ Komşuları keşfet
           for komsu, gecis_suresi in mevcut_istasyon.komsular:
                    yeni_toplam_sure = toplam_sure + gecis_suresi

                    if komsu not in ziyaret_edildi or ziyaret_edildi[komsu] > yeni_toplam_sure:
                       heapq.heappush(pq, (yeni_toplam_sure, id(komsu), komsu, rota + [komsu]))

        return None  # Eğer hedefe ulaşılamazsa None döndür


# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    #Yeni senaryolar ekleyelim

    #Senaryo 4: Ulus'tan Sıhhiye'ye
    print("\n4. Ulus'tan Sıhhiye'ye:")
    rota = metro.en_az_aktarma_bul("K2", "M3")
    if rota:
       print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("K2", "M3")
    if sonuc:
       rota, sure = sonuc
       print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    #Senaryo 5: Demetevler'den Gar'a
    print("\n5. Demetevler'den Gar'a:")
    rota = metro.en_az_aktarma_bul("K3", "M4")
    if rota:
       print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("K3", "M4")
    if sonuc:
       rota, sure = sonuc
       print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

   
