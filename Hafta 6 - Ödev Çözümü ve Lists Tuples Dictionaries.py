#!/usr/bin/env python
# coding: utf-8

# Asal Sayı Ödevi Çözümü

# In[18]:


durum = True
for sayı in range(1,100):
    durum = True
    for bolen in range(2,sayı):
        if sayı % bolen == 0:
            durum = False
    if durum == True and sayı != 1:
        print(sayı," sayısı asaldır.")
        


# Arkadaş Sayı Ödev Çözümü

# In[22]:


toplam1 = 0
toplam2 = 0

for sayi in range(2,221):
    toplam1 = 0
    toplam2 = 0
    for bolen in range(1,sayi):
        if sayi % bolen == 0:
            toplam1 += bolen # toplam1 = toplam1 + bolen
    for bolen2 in range(1,toplam1):
        if toplam1 % bolen2 == 0 and sayi !=toplam1:
            toplam2 +=bolen2
    if sayi == toplam2:
        print(sayi, " ile ", toplam1 , " Arkadaş Sayıdır.")


# # Listeler (lists)

# In[23]:


liste1 = []


# In[24]:


type(liste1)


# In[35]:


liste2=[324,"deneme","a",[24,234,52,3],23.4,324]


# In[27]:


liste2[3]


# In[28]:


liste2[0]


# In[31]:


liste3 = list()


# In[32]:


type(liste3)


# In[39]:


for i in liste2:
    print("{} değerinin veri tipi {}".format(i,type(i)))


# In[40]:


len(liste2)


# In[43]:


liste2[6]


# In[58]:


metin = "Kütahya Teknik Bilimler Meslek Yüksek Okulu"
metin = metin.split(" ")
print(metin)
print(type(metin))


# In[59]:


listemetin = list(metin)


# In[60]:


print(listemetin)


# In[61]:


print(listemetin[2:5])


# In[62]:


listemetin[0] = "Tavşanlı"


# In[63]:


print(listemetin)


# In[64]:


metin2 = "alim"
metin2[0] = "i"


# In[65]:


liste2


# In[76]:


liste1 = ["a","b","123",(2,34,253,32),43.3]


# In[77]:


listetoplam = liste1 + liste2


# In[78]:


listetoplam


# In[79]:


type(listetoplam[3])


# In[ ]:




