#!/usr/bin/env python
# coding: utf-8

# In[10]:


vizenotu = int(input("Vize(Ara Sınav) notunu Giriniz"))
finalnotu = int(input("Final Notunuzu Giriniz:"))
print(finalnotu >= 50)
sonuc = vizenotu*0.40 + finalnotu*0.60
print(sonuc >= 50)


# In[9]:


vizenotu = int(input("Vize(Ara Sınav) notunu Giriniz:"))
finalnotu = int(input("Final Notunuzu Giriniz:"))
sonuc = vizenotu*0.40 + finalnotu*0.60

if finalnotu >= 50:
    if sonuc >= 50:
        print("Geçtiniz",sonuc)
    else:
        print("Kaldınız {}".format(sonuc))
else:
    print("Kaldınız")


# In[2]:


vizenotu = int(input("Vize(Ara Sınav) notunu Giriniz:"))
finalnotu = int(input("Final Notunuzu Giriniz:"))
sonuc = vizenotu*0.40 + finalnotu*0.60

if finalnotu >= 50 and sonuc >= 50:
    print("Sonuç Hesaplanacak.")
    print(sonuc, " ile Geçtiniz")
    print("Vize Notu: {} \nFinal Notu : {} \nSonuc : {} ile Geçtiniz".format(vizenotu,finalnotu,sonuc))
else:
    print("Kaldınız")


# In[6]:


sayı = int(input("Bir Sayı Giriniz:"))

if sayı > 0 :
    print("Sayı Pozitif")
elif sayı < 0 :
    print("Sayı Negatif")
else:
    print("Sayı Sıfırdır")


# In[37]:


cinsiyet = input("Cinsiyet Bilgisi Kadın için 'K-k' Erkek için 'E-e' giriniz :")

if cinsiyet == 'K' or cinsiyet == 'k':
    print("Kadınlar Türkiye de Askerlik yapamaz.")
elif cinsiyet.upper() == 'E':
    yaş = int(input("Yaşınızı Giriniz:"))
    if yaş>=20:
        print("Askere Gidebilir")
    else:
        print("Yaşınız Askerlik için uygun değil")
else:
    print("Hatalı Giriş yaptınız!!")


# In[53]:


vizenotu = int(input("Vize(Ara Sınav) notunu Giriniz:"))
finalnotu = int(input("Final Notunuzu Giriniz:"))
sonuc = vizenotu*0.40 + finalnotu*0.60


if vizenotu<0 or vizenotu>100 or finalnotu<0 or finalnotu>100:
    print("0 ile 100 arasında not giriniz!!! ")
else:
    
    if finalnotu>=50:
        if sonuc >= 89:
            print("AA")
        elif sonuc >= 79:
            print("BA")
        elif sonuc >= 75:
            print("BB")
        elif sonuc >= 70:
            print("CB")
        elif sonuc >= 64:
            print("CC")
        elif sonuc >= 57:
            print("CD")
        elif sonuc >= 50:
            print("DD")
        elif sonuc >= 45:
            print("FD")
        else:
            print("FF")
    else:
        print("Final Notu 50 altında Kaldınız.")


# In[10]:


print("""
     Basit Hesap Makinesi 
     4 Temel İşlem Yapar
""")
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


# In[ ]:




