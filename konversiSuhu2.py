# Konversi suhu 2

satuan = input("silahkan pilih satuan suhu\nyang kamu ketahui\n1. celcius\n2. reamur\n3. farenheit\n4. kelvin\n\nketikkan sesuai nomor:\t")

if satuan ==str(1) :
    suhu = float(input("masukkan nilai celcius:\t"))

    # reamur
    reamur = (4/5)*suhu
    print("Reamur :", reamur)

    # farenheit
    farenheit = (9/5)*suhu + 32
    print("farenheit :", farenheit)

    # kelvin
    kelvin = suhu + 273
    print("kelvin :", kelvin)

elif satuan == str(2):
    suhu = float(input("masukkan nilai reamur:\t"))

    # celcius
    celcius = (5/4)*suhu
    print("celcius :", celcius)

    # farenheit
    farenheit = (9/5)*celcius + 32
    print("farenheit :", farenheit)

    # kelvin
    kelvin = celcius + 273
    print("kelvin :", kelvin)

elif satuan == str(3):
    suhu = float(input("masukkan nilai farenheit:\t"))

    # celcius
    celcius = (5/9)*(suhu - 32)
    print("celcius :", celcius)

    # reamur
    reamur = (4/5)*celcius + 32
    print("reamur :", reamur)

    # kelvin
    kelvin = celcius + 273
    print("kelvin :", kelvin)

elif satuan == str(4):
    suhu = float(input("masukkan nilai kelvin:\t"))

    # celcius
    celcius = suhu - 273
    print("celcius :", celcius)

    # reamur
    reamur = (4/5)*celcius + 32
    print("reamur :", reamur)

    # farenheit
    farenheit = ((9/5)*celcius) + 32
    print("farenheit :", farenheit)

else :
    print("")
    print("maaf, argumen anda tidak diketahui.\n")

if satuan == 1 or 2 or 3 or 4:
    print("")

print("terimakasih:)")


