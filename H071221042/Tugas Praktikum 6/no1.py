'''INPUTAN'''
from ast import Try


x= str(input())
y= str (input())

'''PROGRAM MENYALIN FILE'''
try:
    file1= open(f"{x}.txt")
    isi_file1= file1.read()

    file_copy= open(f"{y}.txt", "w")
    file_copy.write(isi_file1)
    print("Berhasil")
except:
    print("Gagal")
    