a=input('Masukan nama mahasiswa : ')
b=input('Masukan NIM-nya : ')
if b[0:2]=="71" and int(b[2:4])<=22 and int(b[2:4]>=20):
    print(f'{a},Merupakan Mahasiswa Informatika angkatan 20 hingga 22') 
else:
    print(f'{a},Bukan merupakan Mahasiswa Informatika angkatan 20 hingga 22')
