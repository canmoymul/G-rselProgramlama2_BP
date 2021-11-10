#!/usr/bin/env python
# coding: utf-8

# # range fonksiyonu

# In[1]:


for i in range(1,10):
    print(i)


# In[3]:


for i in range(3,20):
    print(i)


# In[4]:


for i in range(5,30,3):
    print(i)
    


# In[5]:


for i in range(1,50):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    


# In[12]:


liste = []
toplam = 0
for i in range(2,10000):
    for j in range(1,i):
        if i % j == 0:
            toplam = toplam + j
            liste.append(j)
    if toplam == i:
        print(i," Sayısı Mükemmel Sayıdır=",liste)
    toplam = 0
    liste.clear()
        


# In[13]:


for i in range(1,11):
    print("*****************")
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))


# In[14]:


while True:
    şifre = input("Şifrenizi Belirleyiniz:")
    
    if not şifre: # if şifre = ""
         print("Şifre Boş BırakılamazLütfen Bir Şifre Belirleyin!")
    elif len(şifre) in range(4,13):
        print("Şifreniz Başarıyla Oluşturuldu")
        break
    else:
        print("Şifreniz Dört Karakterden az Oniki Karakterden Fazla olmamalı!!!")


# In[19]:


for i in range(3):
    
    şifre = input("Şifrenizi Belirleyiniz:")
    
    if not şifre: # if şifre = ""
         print("Şifre Boş BırakılamazLütfen Bir Şifre Belirleyin!")
    elif len(şifre) in range(4,13):
        print("Şifreniz Başarıyla Oluşturuldu")
        break
    else:
        print("Şifreniz Dört Karakterden az Oniki Karakterden Fazla olmamalı!!!")
    
    if i == 2:
        print("Şifrenizi 3 Hakta Belirleyemediniz!Çıkış Yapılıyor...")
        break


# In[ ]:




