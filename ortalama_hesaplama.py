def ortalama_hesaplama():
    puanlar = []

    while True:
        puan = input("puanınızı girin (çıkmak için q): ")
        if puan == 'q':
            break

        try:
            puan = int(puan)
            if 0 < puan <= 100:
                puanlar.append(puan)
            else:
                print("0 ile 100 arasında not girmelisiniz.")
        except ValueError:
            print("Geçerli bir sayı girin ya da çıkmak için 'q'ya tıklayın.")

    if len(puanlar) == 0:
        print("Puan girmediğiniz için ortalama yoktur.")
    else:
        print(f"Puanlarınız şu şekildedir: {puanlar}")
        ortalama = sum(puanlar) / len(puanlar)
        print(f"Puanlarınızın ortalaması: {ortalama:.2f}")

ortalama_hesaplama()
