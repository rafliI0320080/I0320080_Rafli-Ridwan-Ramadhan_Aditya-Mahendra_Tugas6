print("=====Menghitung nilai rata-rata=====")
Banyak_data = int(input("Banyak data: "))
Data = []
Jumlah = 0
for nilai in range(0,Banyak_data):
    temp = int(input("Masukkan data ke-%d: " % (nilai+1)))
    Data.append(temp)
    Jumlah += Data[nilai]
    rata_rata = Jumlah / Banyak_data
print("Rata-ratanya adalah: ", rata_rata)