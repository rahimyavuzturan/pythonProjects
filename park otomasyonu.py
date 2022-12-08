#Araçların park edebileceği nxn lik bir matrix oluşturma
#Bu matrixin en sağ alt kısmında bir kapı varmış gibi düşünüp araçları bu kapıya en yakın olacak şekilde dizme

def main():
    n = int(input("Otoparkın Bir Kenar Uzunluğu: ")) 
    otopark = otopark_olustur(n)
    print(f"Otopark:\n{otopark_ciz(otopark)}")
    while True: 
        try:
            cevap = int(input("Eklenecek Araç Sayısı Girin: "))
            arac_ekle(otopark, cevap) 
            print(f"Otopark:\n{otopark_ciz(otopark)}") 
        except ValueError: 
            print("Geçerli bir değer girilmedi! İşlem iptal ediliyor..")
            break
        except: 
            print("Hata! İşlem iptal ediliyor...")
            break

def otopark_olustur(n):
    otopark = []
    for i in range(n):
        width = []
        for j in range(n):
            width.append(0)
        otopark.append(width)
    return otopark

def otopark_ciz(otopark):
    newOtopark = '\n'.join(map(str, otopark))
    return newOtopark

        

def yer_bul(otopark):
    n = len(otopark)
    index = {}
    for i in range(n):
        for j in range(n):
            if (otopark[i][j]) == 0:
                index.update({f'{i},{j}':(i+j)})
            else:
                continue
    newIndex = list(sorted(index.items(), key = lambda item: item[1]))
    return newIndex[-1][0]


def arac_ekle(otopark, n):
    if n == 1:
        yer = yer_bul(otopark)
        otopark[int(yer[0])][int(yer[2])] = 1
    else:
        yer = yer_bul(otopark)
        otopark[int(yer[0])][int(yer[2])] = 1
        n = n-1
        arac_ekle(otopark,n)
        

main()
