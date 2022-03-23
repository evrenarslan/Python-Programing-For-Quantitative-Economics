#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 20:25:19 2022

@author: earslan
"""
# =============================================================================
# katsayı=1
# ad="ece"
# yas=17
# print(ad)
# print(yas)
# print(yas+katsayı)
# ad='emre'
# yas=11
# print(ad)
# print(yas)
# print(yas+katsayı)
# #print(3+2)
# #print(4**(3+2))
# 
# =============================================================================
yoluzunlugu=125
adimuzunlugu=0.55

kacadim=yoluzunlugu/adimuzunlugu

# print("Yolun bitmesi için gerekli olan adım:",kacadim)

# print("Yol Uzunluğu Değişken Tipi:",type(yoluzunlugu))
# print("Kaç Adım Değişken Tipi:",type(kacadim))
# print("Ece Type:",type("ece"))



# dogru=True
# yanlis=False

# print("Doğru Tipi:",type(dogru))

# =============================================================================
# yas=16
# cinsiyet="E"
# 
# if (yas>=17) & (cinsiyet=="K") :
#     harclik=10
#     #print("1.:",harclik)
# elif (yas>=17) & (cinsiyet=="E"):
#     harclik=8
#     #print("2.:",harclik)
# elif (yas<17) | (cinsiyet=="K"):
#     harclik=4
#     print("3.:",harclik)
# else:
#     harclik=5
#     print("4.:",harclik)
# 
# # if (yas>=17) |(cinsiyet=="K"):
# #     harclik=10
# # print("1.:",harclik)
# # if (yas>=17) | (cinsiyet=="E"):
# #     harclik=8
# # print("2.:",harclik)
# 
# print("Harçlık:",harclik)
# 
# if False:
#     print("Evren")
# =============================================================================
# =============================================================================
# calisan="Evren"
# eskimaas=15
# if eskimaas>=15:
#     oran=0.15
# else:
#     oran=0.2
# print(calisan,":",eskimaas*(1+oran),"Zam Oranı:",oran)
# calisan="Ali"
# eskimaas=20
# if eskimaas>=15:
#     oran=0.15
# else:
#     oran=0.2
# print(calisan,":",eskimaas*(1+oran),"Zam Oranı:",oran)
# calisan="Özgül"
# eskimaas=10
# if eskimaas>=15:
#     oran=0.15
# else:
#     oran=0.2
# print(calisan,":",eskimaas*(1+oran),"Zam Oranı:",oran)
# =============================================================================

def zamoran(maas):
    if maas>=15:
        oran=0.15
    else:
        oran=0.20
    return oran

calisanlar={"Evren":15,"Ali":20,"Özgül":10}

for key in calisanlar:
    zam=zamoran(calisanlar[key])
    print(key,":",calisanlar[key]*(1+zam),"Zam Oranı:",zam)





    


    



