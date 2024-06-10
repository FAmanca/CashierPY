import datetime, os, time

dt = datetime.datetime.now()
sistem_operasi = os.name


def res():
    match sistem_operasi:
        case "posix":
            os.system("clear")
        case "nt":
            os.system("cls")


def menu():
    print("======================================")
    print("              GochuuMilk              ")
    print("======================================")
    print("List Menu")
    print("--------------------------------------")
    print("A . SD (Susu Dingin) : Rp. 6000")
    print("B . SMP (Susu Murni Panas) : Rp. 5000")
    print("C . SMA (Susu Madu Anget) : Rp. 10000")
    print("D . SMK (Susu Murni Kocok) : Rp. 13000")
    print("EX. TAMPILKAN MENU KHUSUS :V")
    print("======================================")


def ms():
    print("======================================")
    print("        The Taste From Heaven         ")
    print("======================================")
    print("List Menu Special")
    print("--------------------------------------")
    print("SM. Susu Makima : Rp. 140000")
    print("SW. Susu Watame : Rp. 135000")
    print("SG. Susu Ganyu : Rp. 170000")
    print("SS. Susu Shenhe : Rp. 200000")
    print("SN. Susu Nahida : Rp. 900000")
    print("======================================")


def strk():
    print("======================================")
    print("              GochuuMilk              ")
    print("======================================")
    print("Tanggal Pemesanan: ", dt.strftime("%Y-%m-%d %H:%M"))
    print("Menu :", listnama)
    print("Jumlah Beli :", jp)
    print("Harga : Rp.", harga)
    print("Diskon : Rp.", diskon)
    print("--------------------------------------")
    print("Dibayar : Rp.", byr)
    print("Jumlah Bayar : Rp.", ttl)
    print("kembalian : Rp.", kmb)
    print("======================================")
    print("          TERIMA KASIH", nm)
    print("======================================")


def pmb():
    print("------------------------------------")
    print("Anda beli : ", listnama)
    print("Total Belanjaan Anda : = Rp.", harga)
    print("Diskon Belanjaan Anda : = Rp.", diskon)
    print("Total Bayar = Rp.", ttl)
    print("------------------------------------")


res()
print("======================================")
print("    Selamat Datang Di GochuuMilk      ")
print("======================================")
nm = str(input("Masukan Nama Anda = "))
print("")
print("Halo", nm)
print("Silahkan Pilih Pesanan Anda :D")
print("======================================")
print("")
print("")
time.sleep(1)

res()
menu()
psn = str(input("Masukan Abjad Pesanan = "))
if psn == "EX" or psn == "ex":
    ms()
    psn = str(input("Masukan Abjad Pesanan = "))
jp = int(input("Masukan Jumlah Pesanan = "))
print("======================================")
print(
    """
    """
)

res()

if psn == "A" or psn == "a":
    listnama = "SD (Susu Dingin)"
    harga = 6000 * jp
    if jp >= 10:
        diskon = int(harga * 0.1)
        ttl = int(harga - diskon)
    else:
        diskon = 0
        ttl = int(harga - diskon)

if psn == "B" or psn == "b":
    listnama = "SMP (Susu Murni Panas)"
    harga = 5000 * jp
    if jp >= 10:
        diskon = int(harga * 0.1)
        ttl = int(harga - diskon)
    else:
        diskon = 0
        ttl = int(harga - diskon)

if psn == "C" or psn == "c":
    listnama = "SMA (Susu Madu Anget)"
    harga = 10000 * jp
    if jp >= 10:
        diskon = int(harga * 0.1)
        ttl = int(harga - diskon)
    else:
        diskon = 0
        ttl = int(harga - diskon)

if psn == "D" or psn == "d":
    listnama = "SMK (Susu Murni Kocok)"
    harga = 13000 * jp
    if jp >= 10:
        diskon = int(harga * 0.1)
        ttl = int(harga - diskon)
    else:
        diskon = 0
        ttl = int(harga - diskon)

if psn == "SM" or psn == "sm":
    listnama = "Susu Makima"
    harga = 140000 * jp
    if jp >= 10:
        diskon = int(harga * 0.1)
        ttl = int(harga - diskon)
    else:
        diskon = 0
        ttl = int(harga - diskon)

if psn == "SW" or psn == "sw" or psn == "Sw":
    listnama = "Susu Watame"
    harga = 135000 * jp
    if jp >= 10:
        diskon = int(harga * 0.1)
        ttl = int(harga - diskon)
    else:
        diskon = 0
        ttl = int(harga - diskon)

if psn == "SG" or psn == "sg" or psn == "Sg":
    listnama = "Susu Ganyu"
    harga = 170000 * jp
    if jp >= 10:
        diskon = int(harga * 0.1)
        ttl = int(harga - diskon)
    else:
        diskon = 0
        ttl = int(harga - diskon)

if psn == "SS" or psn == "ss" or psn == "Ss":
    listnama = "Susu Shenhe"
    harga = 200000 * jp
    if jp >= 10:
        diskon = int(harga * 0.1)
        ttl = int(harga - diskon)
    else:
        diskon = 0
        ttl = int(harga - diskon)

if psn == "SN" or psn == "sn" or psn == "Sn":
    listnama = "Susu Nahida"
    harga = 900000 * jp
    if jp >= 10:
        diskon = int(harga * 0.1)
        ttl = int(harga - diskon)
    else:
        diskon = 0
        ttl = int(harga - diskon)


pmb()
byr = int(input("Masukan Nominal Uang Anda = Rp."))
kmb = int(byr - ttl)


def gagal():
    print("======================================")
    print("       PEMABYARAN GAGAL COEG        ")
    print("      UANG ANDA TYDAK CUKUP :V      ")
    print("     DUID KAO KURENG  Rp.", ttl - byr)
    print("======================================")


if byr < ttl:
    res()
    gagal()
    while True:
        ilp = str(input("apakah ingin mengulang ? Y/N = "))
        if ilp == "Y" or ilp == "y":
            pmb()
            byr = int(input("Masukan Nominal Uang Anda = Rp."))
            kmb = int(byr - ttl)
            if byr < ttl:
                res()
                gagal()

        elif ilp == "N" or ilp == "n":
            res()
            print("======================================")
            print("  AOWKAOWKAOWKAWO GA MAMPU BAYAR :V   ")
            print("======================================")
            break

        else:
            print("INVALID INPUT")

        if byr >= ttl:
            kmb = int(byr - ttl)
            res()
            strk()
            break

else:
    res()
    strk()
