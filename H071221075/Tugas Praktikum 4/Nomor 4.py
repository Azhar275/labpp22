def faktorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return (number * faktorial(number - 1))
num = int(input("Masukkan Angka : "))
print(f"Nilai Faktorial dari {num} adalah {faktorial(num)}")