#Deklarasi Dictionary
rental = {}

# rental = {nama_mobil : {bulan : total sewa}}
with open("data_penyewaan_mobil.txt","r") as f:
    result = f.read().split("\n")
    for i in range(len(result)):
        row = result[i].split(" ")
        bulan = row[0].split("-")[1]
        nama = row[1]
        total_sewa = int(row[2])

        found_nama = False
        for key, val in rental.items():
            # cek apakah ada nama mobil yang sama
            if nama == key:
                found_nama = True
                found_bulan = False
                for data_bulan in val.keys():
                # cek apakah ada bulan yang sama
                    if bulan == data_bulan:
                        rental[key][bulan] += total_sewa
                        found_bulan = True
                        break
                if not found_bulan:
                    rental[key][bulan] = total_sewa
        if not found_nama:
            rental[nama] = {bulan : total_sewa}

#Fungsi mobil yang sering disewa
def favorit(data_dictionary):
    max = 0
    nama_mobil = ""
    for nama, val in data_dictionary.items():
        jumlah = 0
        for bulan in val.keys():
            jumlah += val[bulan]
        if jumlah > max:
            nama_mobil = nama
            max = jumlah

    return nama_mobil

#Fungsi Report rata rata sewa mobil
def report(data_dictionary):
    data_info = {}
    n = len(list(rental.keys()))
    for bulan in [str(i) for i in range(1,13)]:
        jumlah = 0
        for val in data_dictionary.values():
            if bulan in list(val.keys()):
                jumlah += val[bulan]
        jumlah /= n
        if jumlah == 0:
            data_info[bulan] = 0
        else:
            data_info[bulan] = jumlah

    print("------------------------------")
    print("bulan\trata-rata sewa")
    print("------------------------------")
    for key, val in data_info.items():
        print("%s\t%.2f"%(key,val))

def main():
    while True:
        print("Menu Rental Yuk")
        print("1. Tampilkan data penyewaan")
        print("2. Tampilkan mobil yang paling banyak di rental")
        print("3. Tampilkan laporan Rata Rata Sewa")
        print("4. exit")
        inp = int(input("Masukan pilihan: "))
        
        print("================================\n")
        if inp == 1:
            print("---- Data Dictionary Penyewaan ----")
            print("{")
            for key, val in rental.items():
                print("\t",key,":" ,val)
            print("}")
            print("\n================================\n")
        elif inp == 2:
            result = favorit(rental)
            print("mobil yang paling banyak di rental adalah", result)
            print("\n================================\n")
        elif inp == 3:
            report(rental)
            print("\n================================\n")
        elif inp == 4:
            break
        else:
            print("Input yang anda masukan salah!!!")
            print("\n================================\n")

if __name__ == "__main__":
    main()
    print("Program selesai")