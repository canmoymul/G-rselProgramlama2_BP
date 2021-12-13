#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dosya açmak için open()  
# open(dosya_adı,dosya_erişme_kipi)

file = open("gorselprogramlama2.txt","w")


# In[2]:


#dosyayı kapatmak
file.close()


# In[66]:


file = open("gorselprogramlama2.txt","w",encoding="utf-8")


# In[67]:


file.write("Buğra Çakır")


# In[68]:


file.close()


# In[92]:


# a Kipiyle Dosyaya yazmak append(ekleme) Dosya varsa ekleme
#yapmak için açar Dosya yoksa oluşturur.
file = open("gorselprogramlama2.txt","a",encoding="utf-8")


# In[93]:


file.write("\nMustafa Okburan")


# In[94]:


file.close()


# In[72]:


#r ile dosyayı okuma amaçlı açarız 
file = open("gorselprogramlama2.txt","r",encoding="utf-8")


# In[73]:


file.close()


# In[74]:


try:
    file = open("gorselprogramlama3.txt","r",encoding="utf-8")
except FileNotFoundError:
    print("Dosya Bulunamadı!!!")


# In[75]:


file = open("gorselprogramlama2.txt","r",encoding="utf-8")

for isimler in file:
    print(isimler, end="")
file.close()


# In[76]:


file = open("gorselprogramlama2.txt","r",encoding="utf-8")

isimler = file.read()

print("isim Lİstemiz:\n",isimler,sep="")

isimler2 = file.read()

print("2. isim Lİstemiz:\n",isimler2,sep="")
file.close()


# In[77]:


#readline() fonksiyonu her çağrıldığında sadece bir satırı okur. Her seferinde dosya imleceimiz bir satır atlayarak devam eder.
file = open("gorselprogramlama2.txt","r",encoding="utf-8")


# In[78]:


print(file.readline())


# In[79]:


print(file.readline())


# In[80]:


print(file.readline())


# In[81]:


print(file.readline())


# In[82]:


file.close()


# In[87]:


file = open("gorselprogramlama2.txt","r",encoding="utf-8")
file.readlines()


# In[84]:


file.close()


# In[85]:


#seek() write()
# r+ hem okuam hem yazma işlemi yapmamızı sağlar

with open("gorselprogramlama2.txt","r+",encoding="utf-8") as file:
    print(file.read())


# In[86]:


with open("gorselprogramlama2.txt","r+",encoding="utf-8") as file:
    file.seek(4)
    file.write("ozcan")


# In[65]:


with open("gorselprogramlama2.txt","r+",encoding="utf-8") as file:
    print(file.read())


# In[96]:


with open("gorselprogramlama2.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Akif Karataş\n")
    file.seek(0)
    for satır in liste:
        file.write(satır)


# In[97]:


with open("gorselprogramlama2.txt","r+",encoding="utf-8") as file:
    icerik = file.read()
    print(icerik)


# In[98]:


with open("gorselprogramlama2.txt","r+",encoding="utf-8") as file:
    print(file.tell())


# In[116]:


import os
with open("gorselprogramlama2.txt","r+",encoding="utf-8") as file:
    file.seek(0,os.SEEK_END)

    print(file.tell())


# In[123]:


def not_hesapla(satır):
    
    satır = satır[:-1]
    
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    
    son_not = not1 *(3/10) + not2 * (3/10) + not3 * (4/10)
    
    if (son_not >=90):
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
        
    return isim + " -----> " + harf + "*\n"

with open("gorselprogramlama2.txt","r+",encoding="utf-8") as file:
    eklenecekler_listesi = []
    
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
        
    with open("harfnotlari.txt","w",encoding="utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)


# In[ ]:





# In[ ]:




