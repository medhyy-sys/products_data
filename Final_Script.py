#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:09:18 2021

@author: assimimohamed
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
from sys import exit


o=1


Cat_Produit=["Crème visage","Soins contour des yeux","Masques pour le visage",
            "Exofiliants pour le visage","Zone de la bouche et des lèvres","Toniques et soin appaisant visage"]


    
Sub_cat=[ 
    #Soin visage
    [["https://www.notino.fr/cosmetiques/cosmetiques-visage/cremes-visage/?f={}-1-2-3645-8170-3663".format(o),"Crème pour le visage"]],
    ["https://www.notino.fr/serums-visage/?f={}-1-2-3645-8170-8199".format(o),"Sérum visage"],
    ["https://www.notino.fr/soins-visage/?f={}-1-2-3645-8170-3665".format(o),"Masque visage"],
    ["https://www.notino.fr/soins-visage/?f={}-1-2-3645-8170-3665".format(o),"Exofiliant pour visage"],
    ["https://www.notino.fr/soins-visage/?f={}-1-2-3645-8170-47328".format(o),"Soin local"],
    ["https://www.notino.fr/huile-pour-le-visage/?f={}-1-2-3645-8170-34896".format(o),"Huile pour visage"]],
   
      
    #Soins contour yeux
[["https://www.notino.fr/cosmetiques/cosmetiques-visage/cremes-et-gels-pour-les-yeux/?f={}-1-2-3645-35128-35129".format(o),"Crème pour les yeux"],    
 ["https://www.notino.fr/serum-contour-des-yeux/?f={}-1-2-3645-35128-35131".format(o),"Sérum contour yeux"],
 ["https://www.notino.fr/masques-yeux/?f={}-1-2-3645-35128-35130".format(o),"Masque yeux"]],
    
    
    #Masque pour visage
[["https://www.notino.fr/cosmetiques/cosmetiques-visage/masque-en-tissu/?f={}-1-2-3645-47278-47279".format(o),"Masque en tissu"],
     ["https://www.notino.fr/masques-visage/?f={}-1-2-3645-47278-47280".format(o),"Masque crème"],
     ["https://www.notino.fr/cosmetiques/cosmetiques-visage/masque-peel-off/?f={}-1-2-3645-47278-47281".format(o),"Masque peel-off"],
     ["https://www.notino.fr/masques-visage/?f={}-1-2-3645-47278-47285".format(o),"Masque spécial"],
     ["https://www.notino.fr/masques-visage/?f={}-1-2-3645-47278-47282".format(o),"Masque pour les yeux"],
     ["https://www.notino.fr/masques-visage/?f={}-1-2-3645-47278-47283".format(o),"Masque pour les lèvres"],
     ["https://www.notino.fr/masques-visage/?f={}-1-2-3645-47278-47286".format(o),"Masque pour le décolleté"],
     ["https://www.notino.fr/masques-visage/?f={}-1-2-3645-47278-47284".format(o),"Masque pour le nez"]],
    

  
    #Exofiliant pour visage
[["https://www.notino.fr/exfoliant-enzymatique/?f={}-1-2-3645-47273-47276".format(o),"peeling au enzymes"],
     ["https://www.notino.fr/peeling-visage/?f={}-1-2-3645-47273-47274".format(o),"Exofiliant"]],
    
    
    
    #Zone de la bouche et des lèvres
[["https://www.notino.fr/cosmetiques/cosmetiques-visage/baume-a-levres/?f={}-1-2-3645-8171-3662".format(o),"Beaume à lèvres"],
     ["https://www.notino.fr/soin-levres/?f={}-1-2-3645-8171-22375".format(o),"Produit pour le contour des lèvres"],
     ["https://www.notino.fr/cosmetiques/cosmetiques-visage/gommage-pour-les-levres/?f={}-1-2-3645-8171-47263".format(o),"Gaummage pour les lèvres"],
     ["https://www.notino.fr/cosmetiques/cosmetiques-visage/masque-pour-levres/?f={}-1-2-3645-8171-47266".format(o),"Masque pour les lèvres"]],
    

 
    #Toniques et soins appaisant visage
[["https://www.notino.fr/lotions-toniques/?f={}-1-2-3645-8136-8139".format(o),"Lotion tonique visage"],
     ["https://www.notino.fr/cosmetiques/cosmetiques-visage/brume-visage/?f={}-1-2-3645-8136-34916".format(o),"Brume visage"],
     ["https://www.notino.fr/cosmetiques/cosmetiques-visage/lotion-visage/?f={}-1-2-3645-8136-47277".format(o),"Lotion visage"]]



Link=[]
Marque=[]
Titre=[]
Prix=[]
Sous_titre=[]
Qte=[]
Description=[]
Caracteristiques=[]
Ingredients=[]
Application=[]
Type_de_peau=[]
Effet=[]
Quand_utiliser=[]
Ingredients_actifs=[]
Consistance=[]
Protection_solaire=[]
Type_huile=[]
Image_link=[]
Catégorie=[]
Sous_catégorie=[]




for i in [0]   : #range(len(Cat_Produit)):
    
    for j in range(len(Sub_cat[i])):
        res = requests.get(Sub_cat[i][j][0])
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        
        while True:
                try :
                    last_page=soup.findAll("p",{"class":"paging paging-slim"})[0].findAll("a")[-2].text
                    break
                except IndexError :
                    last_page=1
                    break
        #fetching product links
        for o in range(int(last_page)) :
            
            res = requests.get(Sub_cat[i][j][0])
            html_page = res.content
            soup = BeautifulSoup(html_page, 'html.parser')
            ul=soup.find("ul",{"id":"productsList"})
            liste = ul.findAll("li",{"class":"item"})
            
            for t in liste:
                
                Link.append("https://www.notino.fr"+t.findAll("a")[0]["href"])
                
                Catégorie.append(Cat_Produit[i])
                
                Sous_catégorie.append(Sub_cat[i][j][1])
                
                #fetching data
                res = requests.get(Link[-1])
                html_page = res.content
                soup = BeautifulSoup(html_page, 'html.parser')
                
                brand=soup.find("div",{"id":"pdHeader"}).find("a").text
                Marque.append(brand)
                

                image_link=soup.find("div",{"id":"pdImageGallery"}).find("img")["src"]
                Image_link.append(image_link)
                
                title=soup.find("div",{"id":"pdHeader"}).findAll("span")[1].text
                Titre.append(title)
                
                sous_titre=soup.find("div",{"id":"pdHeader"}).findAll("span")[-2].text
                Sous_titre.append(sous_titre)
                
                
                
                
                
                while True:
                    try :
                        prix=soup.find("div",{"id":"pd-price"}).findAll("span")[0].text
                        break
                    except AttributeError :
                        prix='To_be_Delleted'
                        break
                
                Prix.append(prix)
                
                
                while True:
                    try :
                        quantite_de_matiere=soup.find("div",{"class":"styled__FlexWrapper-h83s98-1 eNYrFC"}).findAll("span")[0].text
                        break
                    except AttributeError :
                        quantite_de_matiere='Non_Disponible'
                        break
        
                Qte.append(quantite_de_matiere)
        
                
                while True:
                    try :
                        description=soup.find("div",{"id":"pd-description-text"}).text.split("Caractéristiques")[0]
                        break
                    except AttributeError :
                        description='Non_Disponible'
                        break
                
                Description.append(description)
        
                
                
                while True:
                    try :
                        caracteristiques=[ i.text for i in soup.find("div",{"id":"pd-description-text"}).findAll("ul")[0].findAll("li")]
                        break
                    except IndexError :
                        caracteristiques='Non_Disponible'
                        break
                    except AttributeError :
                        caracteristiques='Non_Disponible'
                        break
                        
                
                Caracteristiques.append(caracteristiques)
                
                
                #ingredients=[ i.text for i in soup.find("div",{"id":"pd-description-text"}).findAll("ul")[1].findAll("li")]
                #Ingredients.append(ingredients)
                
                #application=soup.find("div",{"id":"pd-description-text"}).text
                #Application.append(application)
                
                while True:
                    try :
                        Clef=[ i.text for i in soup.find("dl",{"class":"styled__Dl-sc-1eu1dd2-7 ebZOHS"}).findAll("dt")]   
                        Valeur=[ i.text for i in soup.find("dl",{"class":"styled__Dl-sc-1eu1dd2-7 ebZOHS"}).findAll("dd")]
                        break
                    except AttributeError :
                        Clef=[]
                        Valeur=[]
                        break
                
                type_de_peau=[Valeur[i] for i in range(len(Valeur)) if Clef[i]=='Type de peau']
                if type_de_peau==[] :
                    type_de_peau="Non_applicable"
                Type_de_peau.append(type_de_peau) 
                
                    
                effet=[Valeur[i] for i in range(len(Valeur)) if Clef[i]=='Effet']
                if effet==[] :
                    effet="Non_applicable"
                Effet.append(effet)
                    
                quand_utiliser=[Valeur[i] for i in range(len(Valeur)) if Clef[i]=="Quant l'utiliser"]
                if quand_utiliser==[] :
                    quand_utiliser="Non_applicable"
                Quand_utiliser.append(quand_utiliser)
                
                ingredients_actifs=[Valeur[i] for i in range(len(Valeur)) if Clef[i]=="Ingrédients actifs"]
                if ingredients_actifs==[] :
                    ingredients_actifs.append("Non_applicable")
                Ingredients_actifs.append(ingredients_actifs)
                    
                consistance=[Valeur[i] for i in range(len(Valeur)) if Clef[i]=="Consistance"]
                if consistance==[] :
                    consistance="Non_applicable"
                Consistance.append(consistance)
                    
                    
                protection_solaire=[Valeur[i] for i in range(len(Valeur)) if Clef[i]=="Protection Solaire"]
                if protection_solaire==[] :
                    protection_solaire="Non_applicable"
                Protection_solaire.append(protection_solaire)
                    
                    
                type_huile=[Valeur[i] for i in range(len(Valeur)) if Clef[i]=="Type d'huile"]
                if type_huile==[] :
                    type_huile="Non_applicable"
                Type_huile.append(type_huile)
                print(len(Link))
               
                
                    
                
            



data = pd.DataFrame({'Image_link': Image_link, 'Marque':Marque, 'Titre': Titre, 'Prix (€)':Prix, 
                     'Sous_titre':Sous_titre,'Qte':Qte,'Description':Description,'Type huile':Type_huile,'Caracteristiques':Caracteristiques,'Catégorie':Catégorie,'Sous catégorie':Sous_catégorie,
                     'Type_de_peau':Type_de_peau,'Effet':Effet,'Ingredients_actifs':Ingredients_actifs,
                     'Consistance':Consistance,'Protection_solaire':Protection_solaire,'Product_link':Link})




data.to_excel('/Users/assimimohamed/Desktop/Products_data.xlsx', encoding="utf-8")









