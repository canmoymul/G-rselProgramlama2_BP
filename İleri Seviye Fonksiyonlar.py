#!/usr/bin/env python
# coding: utf-8

# # İleri Seviye Karakter Dizileri (Stringler)

# upper() ve lower()

# In[1]:


"görsel programlama".upper()


# In[2]:


"DJANGO".lower()


# replace() -> yer değiştirme
# replace(x,y) -> Stringdeki x değerlerini y ile değiştirir

# In[3]:


"ANKARA BAŞ ŞEHİRDİR".replace("A","E")


# In[4]:


"İSTANBUL KOCAELİ SAKARYA BİLECİK KÜTAHYA".replace(" ","->")


# In[5]:


"Birer Birer".replace("Bir","İkiş")

startswith() ve endswith()
startswith(x) : String x ile başlıyorsa True, başlamıyorsa False değeri döndürür
endswith(x) : String x ile bitiyorsa True, bitmiyorsa False değeri döndürür
# In[14]:


"Kütahya Teknik Bilimler MYO".endswith("MYO")


# In[15]:


"Kütahya Dumlupınar Üniversitesi".startswith("Kütahya")


# split(a) : Verilen bir a değerine göre stringi parçalara ayırır ve her parca bir liste haline gelir.

# In[2]:


liste = "Kütahya Teknik Bilimler Meslek Yüksek Okulu".split(" ")


# In[3]:


print(liste)


# In[4]:


liste[0]


# In[18]:


notlar="Berkay Doğru,80,65,78".split(",")


# In[19]:


print(notlar)


# strip(), lstrip() ve rstrip()
# strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler
# lstrip(x) : Stringin sadece başındaki x değerlerini siler
# rstrip(x) : Stringin sadece sonunda ki x değerlerini siler

# In[20]:


"         Kütahya MYO       ".strip()


# In[21]:


"-------------------Görsel Programlama II------------".strip("-")


# In[23]:


"---------------------Görsel Programlama II--------------".lstrip("-")


# In[24]:


"---------------------Görsel Programlama II--------------".rstrip("-")


# join : Liste elemanlarını bir string değeriyle birleştirmemizi sağlar

# In[25]:


liste = ["22","12","2021"]


# In[26]:


"/".join(liste)


# In[27]:


".".join(liste)


# In[28]:


liste=["K","T","B","M","Y","O"]


# In[29]:


".".join(liste)


# count(x) : String içindeki x değerlerini sayar
# 
# count(x,index): Stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar

# In[32]:


"Kütahya Teknik Bilimler Meslek Yüksek Okulu".count("e")


# In[35]:


"Kütahya Teknik Bilimler Meslek Yüksek Okulu".count("e",15)


# find() ve rfind()
# 
# find(x) : x değerini en baştan arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
# rfind(x) : x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indekse döndürür. Bulamazsa "-1" değerini verir.

# In[36]:


"ibrahim.ozcandpu.edu.tr".find("@")


# In[42]:


"ibrahim.ozcan@dpu.edu.tr".find("a")


# In[43]:


"ibrahim.ozcan@dpu.edu.tr".rfind("a")


# # İleri Seviye Kümeler (Sets)

# In[44]:


küme = set()


# In[45]:


print(type(küme))


# In[46]:


liste = [1,1,1,2,3,4,5,2,3,34,5,45,2,34,4]


# In[47]:


küme = set(liste)


# In[48]:


type(küme)


# In[49]:


küme


# In[50]:


küme =set("Bilgisayar Operatörlüğü")


# In[51]:


küme


# In[8]:


x = {"Python","Java","C++","Php","Perl"} # Bu bir set (küme) dir


# In[9]:


for i in x:
    print(i)


# In[10]:


x[2]


# In[11]:


liste = list(x)


# In[12]:


liste[0]


# In[62]:


liste[4]


# Kümelerin Metodları 
# Eleman Eklemek : add() Metodu

# In[63]:


x = {1,2,3,4}


# In[64]:


x.add(4)


# In[65]:


x


# In[66]:


x.add(5)


# In[67]:


x


# In[68]:


x.add(1)


# In[69]:


x


# iki kümenin farkı: difference() metodu
# Bu metot birinci kümenin ikinci kümeden farkını döner.
# 
# küme1.difference(küme2) # Küme1 in Küme2 den farkı

# In[15]:


küme1 = {1,2,3,4,543,63,1234,646,32,562}
küme2 = {1,2,3,4,56,476,65,63,5432,24,63473}


# In[16]:


küme1.difference(küme2)


# In[17]:


küme1


# In[72]:


küme2.difference(küme1)


# iki kümenin farkı ve güncelleme : difference_update() metodu
# 
# Bu metot birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu farka göre günceller.

# In[18]:


küme1 = {1,2,3,8,9,6,23}
küme2 = {8,9,23,64357,345}


# In[19]:


küme1.difference_update(küme2)


# In[20]:


küme1


# In[76]:


küme2


# Kümeden Eleman Çıkartmak : discard() metodu
# İçine verilen değeri kümeden çıkartır. Eğer kümede öyle bir değer yoksa bu metot hiçbir şey yapmaz!(Hata VERMEZ)

# In[77]:


küme1 = {1,2,3,4,5,6,7}


# In[78]:


küme1.discard(4)


# In[79]:


küme1


# In[80]:


küme1.discard(9)


# In[81]:


küme1


# Küme Kesişimleri: intersection() metodu
# Bu metot iki kümenin kesişimlerini bulur

# In[85]:


küme1 = {1,2,3,54,65,745,8423,4532,2134}


# küme2 = {543,32,213,54,745,2134,3,654,74,436}

# In[89]:


küme1.intersection(küme2)


# Küme kesişimler ve güncelleme: intersection_update() metodu
# Bu metor birinci kümeyle ikinci kümenin kesişmelerini bulur ve birinci kümeyi bu kesişime göre günceller.

# In[90]:


küme1 = {32,5,6435,23,42,15,57,84,6}
küme2 = {1,2,3,5,6,76,46,15}


# In[93]:


küme1.intersection_update(küme2)


# In[94]:


küme1


# Kümeler ayrık Küme mi? : isdisjoint() metodu
# Bu metot, eğer iki kümenin kesişim kümesi boş ise True, değilse False döner.

# In[99]:


küme1 = {1,2,3,4,5,67,7}
küme2 = {645,8,4,23,543,6}
küme3 = {-1,-52,856,2617,24}


# In[100]:


küme1.isdisjoint(küme2)


# In[101]:


küme1.isdisjoint(küme3)


# Alt Küme mi? : issubset() metodu
# 
# Bu metot, birinci küme ikinci kümenin alt kümesiyse True değilse False

# In[104]:


küme1 = {1,2,3,4}
küme2 = {1,2,34,5,6,7,2,3,4,2634}
küme3 = {6475,754,845,84424532,52}


# In[105]:


küme1.issubset(küme2)


# In[106]:


küme1


# In[107]:


küme1.issubset(küme3)


# Birleşim Kümesi : union() metodu
# Bu metot iki kümenin birleşim kümesini döner.

# In[108]:


küme1 = {1,2,43,5,6765,8567,321}
küme2 ={2,3,4,5,75,8,96,4576,45}


# In[109]:


küme1.union(küme2)


# Birleşim Kümesi ve update : update() metodu
# Bu birinci kümeyle ikinci kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller.

# In[111]:


küme1 = {1,2,43,5,6765,8567,321}
küme2 ={2,3,4,5,75,8,96,4576,45}


# In[112]:


küme1.update(küme2)


# In[113]:


küme1


# İleri Seyi Listeler

# In[114]:


liste = [1,2,3,4]
liste.append(76)


# In[115]:


liste


# In[116]:


liste.append("KTBMYO")


# In[117]:


liste


# extend() metodu
# 

# In[118]:


liste.extend(["a","b","c"])


# In[119]:


liste


# insert() metodu

# In[120]:


liste.insert(5,"Dumlupınar Üniversitesi")


# In[121]:


liste


# pop() metodu

# In[122]:


liste.pop()


# In[123]:


liste


# In[124]:


liste.pop()


# In[125]:


liste


# In[126]:


liste.pop(6)


# In[129]:


liste


# remove()

# In[130]:


liste.remove(3)


# In[131]:


liste


# In[132]:


liste.remove("KTBMYO")


# index() metodu

# In[133]:


liste


# In[134]:


liste.index("Dumlupınar Üniversitesi")


# count() metodu

# In[21]:


liste =[1,2,3,45,5,2,23,3,4,23,3,3,3]


# In[22]:


liste.count(3)


# sort() metodu

# In[23]:


liste.sort()


# In[24]:


liste


# In[25]:


liste.sort(reverse=True)


# In[140]:


liste


# abs metodu()

# In[141]:


abs(-4)


# In[142]:


abs(4.5)


# In[143]:


abs(-4.5)


# round() fonksiyonu

# In[144]:


round(13.6)


# In[145]:


round(-13.6)


# In[28]:


round(2.3)


# In[34]:


round(2.5)


# In[35]:


max((34,53))



# In[154]:


max((34,53))


# In[36]:


min((23,453))


# In[37]:


pow(2,4)


# In[38]:


sum((3,4))


# In[ ]:




