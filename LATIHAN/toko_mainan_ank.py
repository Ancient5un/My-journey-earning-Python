class TokoMainan:
    def __init__(self):
        self.daftar_mainan = {
            "A001": {"nama": "Robot Transformer", "harga": 150000},
            "A002": {"nama": "Lego Creative", "harga": 200000},
            "A003": {"nama": "Puzzle Edukatif", "harga": 75000},
            "A004": {"nama": "Action Figure", "harga": 120000},
            "A005": {"nama": "Board Game", "harga": 180000}
        }
    
    def tampilkan_menu(self):
        print("SELAMAT DATANG DI TOKO MAINAN ANAK-ANAK!".center(50))
        print("*" * 50)
        print("\nDAFTAR MAINAN YANG TERSEDIA:")
        print("-" * 50)
        for kode, mainan in self.daftar_mainan.items():
            print(f"{kode}: {mainan['nama']} - Rp {mainan['harga']:,}")
        print("-" * 50)
    
    def proses_pembelian(self):
        # Input data pembeli
        nama = input("\nMasukkan nama anda: ").strip()
        if not nama:
            print("Nama tidak boleh kosong!")
            return
        
        kode_mainan = input("Masukkan kode mainan: ").upper()
        
        # Validasi kode mainan
        if kode_mainan not in self.daftar_mainan:
            print("Kode mainan tidak valid!")
            return
        
        mainan = self.daftar_mainan[kode_mainan]
        harga = mainan['harga']
        
        # Input jumlah dengan validasi
        try:
            jumlah_beli = int(input("Masukkan jumlah beli: "))
            if jumlah_beli <= 0:
                print("Jumlah beli harus lebih dari 0!")
                return
        except ValueError:
            print("Masukkan angka yang valid!")
            return
        
        # Hitung total
        total_harga = harga * jumlah_beli
        
        # Tampilkan struk
        self.cetak_struk(nama, kode_mainan, mainan['nama'], harga, jumlah_beli, total_harga)
    
    def cetak_struk(self, nama, kode, nama_mainan, harga, jumlah, total):
        print("\n" + "=" * 50)
        print("STRUK PEMBELIAN".center(50))
        print("=" * 50)
        print(f"Nama Pembeli : {nama}")
        print(f"Kode Mainan  : {kode}")
        print(f"Nama Mainan  : {nama_mainan}")
        print(f"Harga Satuan : Rp {harga:,}")
        print(f"Jumlah Beli  : {jumlah}")
        print("-" * 50)
        print(f"TOTAL HARGA  : Rp {total:,}")
        print("=" * 50)
        
        # Bonus jika beli banyak
        if jumlah >= 3:
            print("\n*** SELAMAT! Anda mendapatkan bonus stiker ***")
        
        print("\nTerima kasih telah berbelanja di toko mainan kami!")
        print("Semoga anak-anak senang dengan mainannya! 😊")

# Jalankan program
if __name__ == "__main__":
    toko = TokoMainan()
    toko.tampilkan_menu()
    toko.proses_pembelian()