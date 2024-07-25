
from datetime import datetime



list='''
Sugar Rs:45/kg
Rice Rs:55/kg
Salt Rs:25/kg
Chilli powder Rs:245/kg
Red Dal Rs:95/kg
Garam masala Rs:145/kg
Chicken masala Rs:165/kg
Badam Rs:645/kg
Almonds Rs:745/kg
Gee Rs:725/kg
Dry Grapes Rs:250/kg
Sunflower Oil Rs:130/kg
Green dal Rs:105/kg


"Products names must enter same as above"
'''


price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
plist=[]
qlist=[]

items={
    "Sugar":45,
    "Rice" :55,
"Salt":25,
"Chilli powder":245,
"Red Dal":95,
"Garam masala":145,
"Chicken masala":165,
"Badam":645,
"Almonds":745,
"Gee":725,
"Dry Grapes":250,
"Sunflower Oil":130,
"Green dal":105,
}
name=input("Enter your Name: ")
option=int(input("To see the List of Items press 1: "))

if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("If you want to Buy press 1 ,for exit press 2: "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your buying product: ")
        quantity=int(input("Enter quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice=totalprice+price
            ilist.append(item)
            plist.append(price)
            qlist.append(quantity)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print("Sorry you enetred item is not available")
            print("We are only available this products")
            print(list)
    else:
        print("please enter 1 or 2 for buying or exit")
    inp=input("can I bill the products yes or no: ")
    if inp=="yes":
        pass
        if finalprice!=0:
            print("Your bill is :")
            print(25*"=","Rama supermarket",35*"=")
            print(28*" ","Kukatpally")
            print("Name: ",name,30*" ","Date: ",datetime.now())
            print(80*"-")
            print("sl.no:",8*" ","items:",8*" ","Quantity:",8*" ","Price:")
            for i in range(len(pricelist)):
                print(i,12*" ",ilist[i],12*" ",qlist[i],12*" ",plist[i])
            print(80*"-")
            print(50*" ","Total Amount: ","Rs.",totalprice)
            print("GST amount: ",52*" ","Rs.",gst)
            print(80*"-")
            print(50*" ","Final Amount: ","Rs.",finalprice)
            print(80*"-")
            print(25*" ","Thanks for visting")
            print(80*"-")
















































