import math

def mesafe_hesapla(son_lat, son_lon, lat, lon):
    # Haversine formülü ile iki koordinat arası mesafeyi metre cinsinden hesaplar
    R = 6371000
    a = (math.sin(math.radians((son_lat - lat) / 2)) ** 2 + math.cos(math.radians(son_lat)) * math.cos(math.radians(lat)) * math.sin(math.radians((son_lon - lon) / 2)) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    mesafe = R * c
    return mesafe


class GPSFilter:
    def __init__(self, pencere_boyutu=5, maks_hiz=12.0):
        self.pencere_boyutu = pencere_boyutu
        self.maks_hiz = maks_hiz
        self.pencere = []
        self.son_t = None
        self.son_lat = None
        self.son_lon = None

    def filtrele(self, t_sn, lat, lon):
        if self.son_lat is None:
            mesafe = 0.0
        else:
            mesafe = mesafe_hesapla(self.son_lat, self.son_lon, lat, lon)
            gecen_sure = t_sn - self.son_t
            izin_verilen_mesafe = self.maks_hiz * gecen_sure

            if mesafe > izin_verilen_mesafe:
                return "REJECTED", mesafe, None
        self.pencere.append((lat, lon))
        self.son_t = t_sn
        self.son_lat = lat
        self.son_lon = lon

        if len(self.pencere) > self.pencere_boyutu:
            self.pencere.pop(0)

        toplam_lat = 0.0
        toplam_lon = 0.0
        for nokta_lat, nokta_lon in self.pencere:
            toplam_lat += nokta_lat
            toplam_lon += nokta_lon

        ort_lat = toplam_lat / len(self.pencere)
        ort_lon = toplam_lon / len(self.pencere)

        return "VALID", mesafe, (ort_lat, ort_lon)


if __name__ == "__main__":
    veriler = [
        (1, 41.10000, 29.00000),
        (2, 41.10005, 29.00005),
        (3, 41.10500, 29.00500),
        (4, 41.10010, 29.00010)
    ]

    filtre = GPSFilter(pencere_boyutu=5, maks_hiz=12.0)

    print("--- GPS FİLTRELEME TEST SONUÇLARI ---")
    for i, (t_sn, lat, lon) in enumerate(veriler, start=1):
        durum, mesafe, ortalama_konum = filtre.filtrele(t_sn, lat, lon)
        if durum == "REJECTED":
            print(f"T{i} (t={t_sn}s): ({lat:.5f}, {lon:.5f}) -> REDDEDİLDİ ")
        elif i == 1:
            ort_lat, ort_lon = ortalama_konum
            print(f"T{i} (t={t_sn}s): ({lat:.5f}, {lon:.5f}) -> GEÇERLİ  Filtre Çıktısı: ({ort_lat:.5f}, {ort_lon:.5f})")
        else:
            ort_lat, ort_lon = ortalama_konum
            print(f"T{i} (t={t_sn}s): ({lat:.5f}, {lon:.5f}) -> GEÇERLİ (Mesafe = {mesafe:.1f} m < 12 m) | Filtre Çıktısı: ({ort_lat:.5f}, {ort_lon:.5f})")