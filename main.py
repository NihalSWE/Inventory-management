# Inventory management system (Practice Project)

import csv
print("For create a new inventory,press 'c':")
print("For update an inventory,press 'u':")
print("For get the price of an item,press 'p':")
print("For delate an item,press 'd':")
print("For exit,press 'e':")
X=input("Enter functions ,'c for new inv','u for update','p for get price','d for delete','e for exit':")
#Create inventory

if X=="c" or X=="C":
    inv_header=["Item","Price"]
    inventory=[]
    start=""
    while start!='e':
        item=input("Enter item name:")
        price=float(input("Enter price:"))
        inventory.append({"Item":item,"Price":price})
        start=input("Enter 'e' to exit or any key to continue:")

    with open ("Inventory.csv","w",newline='') as f:
        writer=csv.DictWriter(f,fieldnames=inv_header)
        writer.writeheader()
        for row in inventory:
            writer.writerow(row)
            print("Inventory created")

#update Inventory
elif X=="u" or X=="U":
    inv_header=["Item","Price"]
    inventory=[]
    start=""
    while start!='e':
        item=input("Enter item name:")
        price=float(input("Enter price:"))
        inventory.append({"Item":item,"Price":price})
        start=input("Enter 'e' to exit or any key to continue:")

    with open ("Inventory.csv","a",newline='') as f:
        writer=csv.DictWriter(f,fieldnames=inv_header)
        
        for row in inventory:
            writer.writerow(row)
            print("Inventory updated")

#get price of item
elif X=="p" or X=="P":
    inv_dict={}

    with open("Inventory.csv","r") as f:
        data_csv=csv.DictReader(f)
        for data in data_csv:
            x=data["Item"]
            y=data["Price"]
            inv_dict.update({x:y})
    start=""
    while start!='e':
        item=input("Enter item name:")
        print("Price of",item,inv_dict[item])
        start=input("Enter 'e' to exit or any key to continue:")

