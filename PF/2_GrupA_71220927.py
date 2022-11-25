print('====Selamat datang di Toko Andi Tersenyum, selamat belanja!====')
a=int(input('Total belanja : Rp.'))

if a<100000:
    print('Tidak ada diskon! Maka yang anda bayarkan adalah: Rp.',a)
elif a>=10000:
    print('Biaya yang harus dibayar setelah diskon adalah: Rp.',a-(a*0.02))
elif a>=50000:
    print('Biaya yang harus dibayar setelah diskon adalah: Rp.',a-(a*0.05))
elif a>=1000000:
    print('Biaya yang harus dibayar setelah diskon adalah: Rp.',a-(a*0.010))
else:
    print("woi")