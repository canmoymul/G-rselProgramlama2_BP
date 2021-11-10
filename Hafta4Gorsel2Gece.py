#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("""
     Basit Hesap Makinesi 
     4 Temel İşlem Yapar
""")

cevap = 'E'
while (cevap.upper() == 'E'):
    
    sayı1 = int(input("Birinci Sayıyı Gir : "))
    işlem = input("[* / + -] den biriniz giriniz:")
    sayı2 = int(input("İkinci Sayıyı Gir :"))

    if işlem == '+':
        print("\nSayılar Toplanıyor")
        print("{} {} {} = {}".format(sayı1,işlem,sayı2,sayı1+sayı2))
    elif işlem == '-':
        print("\nSayılar Çıkartılıyor")
        print("{} {} {} = {}".format(sayı1,işlem,sayı2,sayı1-sayı2))
    elif işlem == '*':
        print("\nSayılar Çarpılıyor")
        print("{} {} {} = {}".format(sayı1,işlem,sayı2,sayı1*sayı2))
    elif işlem == '/':
        print("\nSayılar Bölünüyor")
        print("{} {} {} = {}".format(sayı1,işlem,sayı2,sayı1/sayı2))
    else:
        print("Hatalı Giriş")

    cevap = input("Tekrar Hesaplama Yapmak İstiyor musun?[E/H]:")


# In[2]:


negatif_adet = 0
negatif_toplam = 0
pozitif_adet = 0
pozitif_toplam = 0
while True:
    sayı = int(input("Bir Sayı Girin:"))
    if (sayı<0):
        negatif_adet = negatif_adet + 1
        negatif_toplam = negatif_toplam + sayı
    elif (sayı>0):
        pozitif_adet += 1
        pozitif_toplam += sayı
    else: # girilen sayı 0 (sıfır) dır
        break
print("{} adet negatif sayının toplamı : {} ".format(negatif_adet,negatif_toplam))
print("{} adet pozitif sayının toplamı : {} ".format(pozitif_adet,pozitif_toplam))
        


# In[9]:


import random

sayı = random.randint(1,15)
print("1 ile 100 Arasında Sayı Tuttum Tahmin Et Bakalım")
tahminSayısı = 0
durum = False

while tahminSayısı<5:
    tahmin = int(input("Sayı Gir:"))
    tahminSayısı += 1  
    if sayı > tahmin:
        print("Bilemediniz.{}. Tahmin Hakkını Kullandınız. Sayıyı Büyült".format(tahminSayısı))
    elif sayı < tahmin:
        print("Bilemediniz.{}. Tahmin Hakkını Kullandınız. Sayıyı Küçült".format(tahminSayısı))
    else:
        durum = True
        print("Tebrikler.{}. Tahminde {} sayısını bildiniz.".format(tahminSayısı,sayı))
        break
if durum == False:
    print("Tahmin Hakkınız Doldu. Sayıyı Bilemediniz. Tuttuğum Sayı {} sayısıydı.".format(sayı))


# In[ ]:




