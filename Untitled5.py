#!/usr/bin/env python
# coding: utf-8

# # Koşul Durumları Koşullu İfadeler

# In[7]:


ara_sinav_notu = int(input("Ara Sınav Notunu Giriniz:"))
final_notu = int(input("Final Notunu Giriniz : "))

sonuc = ara_sinav_notu * 0.40 + final_notu*0.60 

#if (eğer)

if final_notu >= 50:
    if sonuc >= 50:
        print("Geçtiniz")
    else:
        print("Ortalamadan Kaldınız")
else:
    print("Kaldınız")


# In[11]:


sayı = int(input("Bir Sayı Giriniz :"))

if sayı > 0:
    print("Girdiğiniz Sayı Pozitiftir")
elif sayı < 0:
    print("Girdiğiniz Sayı Negatiftir")
elif sayı == 0:
    print("Girdiğiniz Sayı 0 dır")
else:
    print("Hatalı Giriş")


# In[18]:


cinsiyet = input("Cinsiyet Bİlgisi Giriniz Erkek için 'E' Kadın için 'K' giriniz: ")
yaş = int(input("Yaşınızı Giriniz : "))

if yaş >= 20:
    if cinsiyet.upper() == 'E':
        print(cinsiyet.upper())
        print("Askere Gidebilir")
    elif cinsiyet.upper() == 'K':
        print("Askere Gidemez")
    else:
        print("Hatalı Bilgi Girişi Yaptınız")
else:
    print("Askerlik yaşınız Gelmemiş olabilir.")


# In[33]:


ara_sinav_notu = int(input("Ara Sınav Notunu Giriniz:"))
final_notu = int(input("Final Notunu Giriniz : "))

sonuc = ara_sinav_notu * 0.40 + final_notu*0.60 
if final_notu <0 or final_notu>100 or ara_sinav_notu <0 or ara_sinav_notu > 100:
    print("Hatalı giriş. Lütfen 0 ile 100 arasında tam sayı giriniz!!!")
else:
    
    if final_notu >= 50:
        if sonuc >= 88 and sonuc <= 100:
            print("AA")
        elif sonuc >= 80:
            print("BA")
        elif sonuc >= 73:
            print("BB")
        elif sonuc >= 66:
            print("CB")
        elif sonuc >= 60:
            print("CC")
        elif sonuc >= 55:
            print("CD")
        elif sonuc >= 50:
            print("DD")
        elif sonuc >= 45:
            print("FD")
        elif sonuc >= 0:
            print("FF")
        else:
            print("Hatalı Durumu oluştu")
    else:
        print("FF")


# In[ ]:





# In[ ]:




