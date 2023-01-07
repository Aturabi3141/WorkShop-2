#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = 100
id(a)


# In[9]:


for n in range (1,6):
    print(n)


# In[22]:


liste = list(range(5,50,2))
print(liste, end= "2" )


# In[20]:


print(*range(20,0,-1))


# In[42]:


for n in range(0,21,3):
    print(n, end = "\na")


# In[43]:


for sayi in range (1, 20):
    print("* " * sayi)
for sayis in range (20,0,-1):
    print("* " * sayis)


# In[48]:


top = 0
for i in range (1,100):
    top += i 
    print(top)


# In[50]:


top = 0
for i in range (1,100):
    top += i 

print(top)


# In[ ]:


range(10)


# In[ ]:


range(1,10)


# In[ ]:


range(1,10,2)


# In[51]:


range(10,0,-2)


# In[52]:


range(10,0,-1)


# In[ ]:


0,1,2,3,4 range(1,2)


# In[ ]:


range(1,1)==> ()
range(1,-1)==> ()


# In[68]:


for i in range (16):
    print("{0:3} {1:16}" .format(i, 10**i))
    


# In[86]:


degisken = ["B","İ","L","İ","Ş","İ","M"]
for i in range (0,8):
    len(degisken)*=i
    print(i)


# In[93]:


a="Bilişim"
for i in range (0,len(a)):
    for j in range (0,(i+1)):
        print(a[j], end = "")
    print()        


# In[96]:


sayi = int(input("Bir sayı değeri giriniz: "))
for satir in range (1, (sayi +1)):
    print("Satir #", satir)


# In[99]:


sayi = int(input("Bir sayi giriniz: "))
for satir in range (1, (sayi+1)):
    for sutun in range (1, (sayi+1)):
        deger = satir*sutun
        print(deger, end=" ")
    print()


# In[105]:


sayi = int(input("Bir sayi giriniz: "))
for satir in range (1, (sayi+1)):
    for sutun in range (1, (sayi+1)):
        print("*",  end=" ")
    print()


# In[110]:


sayi = int(input("Bir sayi giriniz: "))
for satir in range (1, (sayi+1)):
    for sutun in range (1, (sayi+1)):
        deger = satir * sutun
        print("{0:4}".format(deger), end =" ")
    print()


# In[114]:


for ilk in "ABC":
    for ikinci in "ABC":
        if ikinci != ilk :
            for ucuncu in "ABC":
                if ucuncu != ilk and ucuncu != ikinci:
                    print (ilk + ikinci + ucuncu )


# In[115]:


liste = [1,2,3,4,5,6,7]
for eleman in liste:
    print("Eleman", eleman)
    


# In[122]:


s = [(1,2),(3,4),(5,6),(7,8)]
for (i,j) in s:
    print(s, end= "\n")


# In[123]:


liste = [1,2,3,4,5,6,7,8,9]
for i in liste:
    if (i == 5):
        break
    print(i)


# In[127]:


liste = [1,2,3,4,5,6,7,8,9,10]
for i in liste:
    if (i==3 or i == 5):
        continue
    print("i:",i)


# In[134]:


for i in range (0,100):
    if(i % 3 == 1 or i % 3 == 2):
        continue
    print(i)


# In[ ]:




