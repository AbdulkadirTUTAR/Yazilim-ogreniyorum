# # 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# girilenSayi = int(input("Bir sayı giriniz: "))
# kosul = girilenSayi > 0 and girilenSayi < 100
# print(f'Girilen sayı 1-100 arasında bir sayıdır: {kosul}')

# # 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# girilenSayi = int(input("Bir sayı giriniz: "))
# kosul = girilenSayi > 0 and girilenSayi %2==0 
# print(f'Girilen sayı pozitif çift sayıdır: {kosul}')


# # 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
# email = 'abdulkadirtutarr@gmail.com'
# sifre = 'abcd'
# emailgir= input('Email:')
# sifregir= input('Şifre:')

# kosul = (emailgir == email) and (sifregir == sifre) 

# print(f'Giriş bilgileri doğru girdiniz.: {kosul}')

# # 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# result = (a>b) and (a>c)
# print(f'A en büyük sayıdır : {result}')

# result = (b>a) and (b>c)
# print(f'B en büyük sayıdır : {result}')
# result = (c>a) and (c>b)
# print(f'C en büyük sayıdır : {result}')

# # 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# vize1 = float(input('vize 1:'))
# vize2 = float(input('vize 2:'))
# final = float(input('final : '))

# ortalama = ((vize1+vize2)/2*0.6) + (final*0.4)
# kosul = ortalama >=50
# print(f'Dersten geçtiniz: {kosul}')
# # a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
# kosul = (ortalama>=50 and final>=50)
# print(f'Dersten geçtiniz: {kosul}')
# # b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# kosul = ortalama>=50 or final >=70
# print(f'Dersten geçtiniz: {kosul}')

# # 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül: (Kilo / boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (Obez)
ad = input('Adınız:')
kilo = int(input('Kilonuz:'))
boy = float(input('Boyunuz:'))
indeks = kilo / (boy**2)
normal = (indeks >= 18.5) and (indeks <=24.9)
fazlakilolu = (indeks >= 24.9) and (indeks <=29.9)
obez = (indeks >= 29.9) and (indeks <=34.9)
print(f'{normal}İndexsiniz:{indeks} indexiniz normal: {normal}')
print(f'{normal}İndexsiniz:{indeks} indexiniz normal: {fazlakilolu}')
print(f'{normal}İndexsiniz:{indeks} indexiniz normal: {obez}')

