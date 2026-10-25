class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True
        self.warna_sama = 3

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        self.load_gambar(warna_baru)

    def load_gambar(self, warna):
        print("Load gambar bola warna:", warna)

    def tembak(self):
        if self.warna_sama >= 2:
            self.skor += 50

    def info_status(self):
        print("Warna Peluru:", self.warna_peluru)
        print("Skor:", self.skor)
        print("Status Aktif:", self.is_active)


# Uji coba

print()
print("Uji Coba Sesuai LKPD")
Katak = KatakZuma("kuning")
Katak.info_status()
Katak.tembak()
Katak.ganti_warna("hijau")
Katak.tembak()

print()
print("Status Akhir")
Katak.info_status()
