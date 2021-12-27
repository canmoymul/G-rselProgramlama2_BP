#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dosya Açma ve Yazma İşlemleri 


# In[2]:


#Dosya Açmak
"""
open(dosya_adı,dosya_erişme_kipi)

"""


# In[3]:


# "w" dosya kipi
# Dosyalarımız açmak ve dosyalarımıza yazmak için "write" anlamına gelen "w" kipi
# kullınırız. 
#Eğer o dosya sistemde varsa dosyayı silip tekrar oluşturur. Eğer Dosya hiç yoksa
# dosyayı oluşturur

open("gedizogrencileri.txt","w")


# In[54]:


dosya = open("gedizogrencileri.txt","w")


# In[55]:


dosya.close() # Dosyayı Kapatmak için kullanılır.


# In[8]:


dosya = open("C:/Users/Users_Hp_8560/Desktop/Yeni klasör/deneme.txt","w")


# In[9]:


dosya.close()


# In[56]:


dosya = open("gedizogrencileri.txt","w",encoding="utf-8")


# In[57]:


dosya.write("Ömer Mert")


# In[17]:


dosya.close()


# In[13]:


dosya = open("gedizogrencileri.txt","w",encoding="utf-8")


# In[14]:


dosya.close()


# In[18]:


# "a" Kipiyle Dosyalara Yazmak
# "append"(ekleme) kelimesinin baş harfi olan "a" kipiyle bir dosya açıldığında
# Eğer Dosya Yoksa oluşturulur. Dosya Varsa dosya tekrar oluşturulmaz. 
# İçeriği Silmez


# In[60]:


dosya = open("gedizogrencileri.txt","a",encoding="utf-8")
dosya.write("\nibrahim özcan")


# In[22]:


dosya.close()


# In[61]:


dosya = open("gedizogrencileri.txt","a",encoding="utf-8")
dosya.write("\nYağmur öşürgeç")


# In[24]:


dosya.close()


# # Dosya Okuma İşlemleri

# Dosyayı okumak ve verileri almak için "r" kipiyle açmamız gerekiyor. Eğer "r" kipiyle açtığımız dosya bulunamıyorsa "FileNotFoundError" hatası verir. 

# In[25]:


dosya = open("gedizogrencileri.txt","r",encoding="utf-8")


# In[26]:


dosya.close()


# In[ ]:


dosya = open("gedizogrencileri2.txt","r",encoding="utf-8")


# In[28]:


try:
    dosya = open("gedizogrencileri2.txt","r",encoding="utf-8")
except FileNotFoundError:
    print("Dosya Bulunamadı")


# # For döngüsü ile Okuma

# In[29]:


dosya = open("gedizogrencileri.txt","r",encoding="utf-8") #Dosyayı okuma modunda açtık

for isim in dosya:
    print(isim)
dosya.close()


# In[30]:


dosya = open("gedizogrencileri.txt","r",encoding="utf-8") #Dosyayı okuma modunda açtık

for isim in dosya:
    print(isim,end="")
dosya.close()


# # read() fonksiyonu

# read() fonksiyonu eğer içine hiçbir değer vermezsek bütün dosyamızı okur.

# In[32]:


dosya = open("gedizogrencileri.txt","r",encoding="utf-8")

icerik = dosya.read()

print("Dosya İçeriği:\n",icerik,sep="")
dosya.close()


# In[34]:


dosya = open("gedizogrencileri.txt","r",encoding="utf-8")

icerik = dosya.read()

print("Dosya İçeriği:\n",icerik,sep="")

icerik2 = dosya.read()

print("Dosya İçeriği2:\n",icerik2,sep="")

dosya.close()


# # readline() fonksiyonu

# readline() fonksiyonu her çağrıldığında dosyanın sadece bir satırını okur. Her seferinde dosya imlecimiz(file) bir satır atlayarak devam eder.

# In[35]:


dosya = open("gedizogrencileri.txt","r",encoding="utf-8")


# In[36]:


print(dosya.readline())


# In[37]:


print(dosya.readline())


# In[38]:


print(type(dosya))


# In[39]:


print(dosya.readline())


# In[40]:


print(dosya.readline())


# In[41]:


print(dosya.readline())


# In[42]:


dosya.close()


# # readlines() fonksiyonu

# readlines() fonksiyonu ile dosyanın bütün satırları bir liste şeklinde döner.

# In[43]:


dosya = open("gedizogrencileri.txt","r",encoding="utf-8")


# In[45]:


dosya.readlines()


# # Dosyalarda Değişiklik Yapmak

# seek() ve write() 
# 
# Eğer bir dosyanın belli bir yerine seek() fonksiyonu ile gidip, write() fonksiyonu kullanılırsa, yazdığımız değerler öncesinde bulunan değerlerin üzerine yazılacaktır. Bunun için hem okuma hem de yazma işlemimizi yapmamızı sağlayan "r+" kipini kullanırız. 

# In[62]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    print(dosya.read())


# In[50]:


with open ("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    dosya.seek(5) #5. byte
    dosya.write("mer M")


# In[64]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    print(dosya.read())


# In[65]:


with open ("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    dosya.seek(6) #6. byte
    dosya.write("Faruk")


# In[66]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    print(dosya.read())


# # Dosyanın Sonunda Değişiklik Yapmak

# In[67]:


with open("gedizogrencileri.txt","a",encoding="utf-8") as dosya:
    dosya.write("\nKerim Karabacak")


# In[68]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    print(dosya.read())


# In[69]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    icerik = dosya.read()
    
    icerik = "Ahmet Kuzu\n" + icerik
    dosya.seek(0)
    dosya.write(icerik)
    


# In[70]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    print(dosya.read())


# # Dosyanın Ortasında Değişiklik Yapmak

# In[71]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    print(dosya.readlines())


# In[76]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    liste = dosya.readlines()
    liste.insert(3,"Hülya Özcan\n")
    dosya.seek(0)
    for satır in liste:
        dosya.write(satır)


# In[77]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    print(dosya.read())


# In[82]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    liste = dosya.readlines()
    liste.insert(3,"Ayşe Özcan\n")
    dosya.seek(0)
    dosya.writelines(liste)


# In[83]:


with open("gedizogrencileri.txt","r+",encoding = "utf-8") as dosya:
    print(dosya.read())


# # Dosyaları İleri Geri Sarmak

# seek() fonksiyonu dosya içerisinde ileri geri gitmemizi sağlar.
# tell() fonksiyonu ise dosya imlecinin hangi byte da olduğunu söyler.

# In[87]:


with open("gedizogrencileri.txt","r",encoding = "utf-8") as dosya:
    print(dosya.tell())


# In[85]:


with open("gedizogrencileri.txt","r",encoding = "utf-8") as dosya:
    dosya.seek(15)
    print(dosya.tell())


# In[89]:


with open("gedizogrencileri.txt","r",encoding = "utf-8") as dosya:
    dosya.seek(5) # 5.byte gidiyoruz.
    icerik = dosya.read(10)  # 10 karakteri okuyoruz.
    print(icerik)
    dosya.seek(0)
    icerik2 = dosya.read(6)
    print(icerik2)


# In[90]:


def not_hesapla(satır):
    
    satır = satır[:-1]
    
    liste = satır.split(",")
    
    isim = liste[0]
    
    not1 = int(liste[1])
    
    not2 = int(liste[2])
    
    not3 = int(liste[3])
    
    son_not = not1 *(3/10) + not2 * (3/10) + not3 * (4/10)
    
    if (son_not >= 90):

        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------------> " + harf + "\n"
    

with open("gorselprogramlama2.txt","r",encoding="utf-8") as dosya:
    isim_harf_notu_listesi = []
    
    for satırkayıt in dosya:
        isim_harf_notu_listesi.append(not_hesapla(satırkayıt))
    
    
    with open("harfnotlarison.txt","w",encoding="utf-8") as dosya2:
        
        for i in isim_harf_notu_listesi:
            dosya2.write(i)

        
    


# In[91]:


with open("harfnotlarison.txt","r",encoding = "utf-8") as dosya:
    print(dosya.read())


# In[ ]:




