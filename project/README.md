# Matthew's simple POS system used in convenient store
#### Video Demo:  <https://youtu.be/knX-eh-S-4U>
This project has used library: tkinter, re, csv, fpdf, datetime


## Table of content
- [Necessary](###important!-necessary-information)
- [Introduction](#introduction)
    - [Idea](#idea)
    - [Planning](#planning)
    - [Implement](#implement)
- [Code Analysis](#code-analysis)
    - [Code Analysis Route Map](#route-map)
    - [1. login](#1-login)  
    - [2. mainapp](#2-mainapp)  
    - [3. admin control](#3-admin-control)  
    - [3.1 admin management](#31-admin-management)  
    - [4. product control](#4-product-control)  
    - [4.1 product adding](#41-product-adding)  
    - [4.2 product deleting](#42-product-deleting)  
    - [4.3 product modifying](#43-product-modifying)  
    - [4.4 porduct reviewing](#44-porduct-reviewing) 
___


### Important! Necessary Information  
### !!!<font color="yellow">You are required to run project.py</font>!!!
The given admin name is: `CS50store`  
The given admin password is: `!CS50admin`  

The given product info is:
| Product ID  | Product name  | Price  |
| ----------- | ------------- | ------ |
| 012         | A Water       | $8     |
| 456         | B Water       | $9     |
| 707         | C water       | $5     |
| 369         | D Water       | $15    |
| 4568        | A Soda        | $12    |
| 8541        | B Soda        | $11    |
| 4777        | C Soda        | $11.5  |
| 5000        | D Soda        | $15.5  |
| 013         | A Energy Drink| $12    |
| 717         | B Energy Drink| $12.5  |
| 4001        | C Energy Drink| $10    |
| 8848        | D Energy Drink| $11    |
| 987         | A Ice Cream   | $15    |
| 1000        | B Candy       | $4     |
| 0505        | C Potato Chips| $13    |
| 343         | D Bread       | $10.5  |

___

## Introduction

### Idea
The idea of making a simple cashier app is because of the my part time working at a convenient store in summer hoilday that I've learned to use to process the transactions.That's why, I try to make a simple transaction application.
___

### Planning
Since I've plan to make a transaction app, I want to make it more user-friendly with GUI. Therefore, I researched and found that ``tkinter`` should be a matched library for me to make the GUI and then I learned some function of ``tkinter`` with following teacher:

    1. WWW.dasdjiaoia
    2. www.saduihdhahdhau
    
___
### Implement
The application mainly is divided into: ``internal use`` and ``external use``.  

#### 1. Internal Use  
For internal use, it is developed for 2 functions: ``admin management`` and ``product management``.  


__Admin managemnet__ is used to ``add`` admin only. The administrator have to open the csv file to delete or modify the admin data. It is because it is used to prevent any deletion of all admin data happened in GUI.

__Product management__ is used to ``add``, ``delete``, ``modify`` and ``review`` the current data dictionary of the product sold by the convenient store.  

#### 2. External Use  (mainapp)
For external use, it is developed for the ``sales transaction``. The ``mainapp`` have a numerical keypad for inputting the the product ID or the cash that the customer have given. And, there is a ``treeview table`` to show all the product purchaseing information.In addition, the ``mainapp`` include a label to show the change of money and a save pdf function to save the ``receipt ``into pdf which under ``file-receiptrecord`` and allow the cashier to print the ``receipt``.
___

## Code Analysis

### Route Map

[1. login](#1-login)  
[2. mainapp](#2-mainapp)  
[3. admin control](#3-admin-control)  
[3.1 admin management](#31-admin-management)  
[4. product control](#4-product-control)  
[4.1 product adding](#41-product-adding)  
[4.2 product deleting](#42-product-deleting)  
[4.3 product modifying](#43-product-modifying)  
[4.4 porduct reviewing](#44-porduct-reviewing)  
___
### 1. login
Main function in login page:
```python
def admin_login()
```
Within ``admin_login``, there are 3 parts: <font color="yellow">I. File locate and data get</font>, <font color="lightblue">II. user login check</font> and <font color=#FFCCCB>III. login process</font>  

#### <font color="yellow">I. File locate and data get</font>
The following python code is used to read the admin data which should be stored in `admin.csv`. If not, the program will automatically create a `admin.csv` and default admin name(CS50store) and password(ConvenientCS50) for in case any malfunction with others program 
```python
try:
    with open("admin.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            admins.append({"AdminId": row["AdminId"], "AdminPw": row["AdminPw"]})
except FileNotFoundError:
    with open("usrs_info.csv", "a", newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["AdminId","AdminPw"])
        writer.writeheader()
        writer.writerow({"AdminId": "CS50store", "AdminPw": "ConvenientCS50"})
```  

#### <font color="lightblue">II. user login check</font>  
The following python code is used to verify the entered admin name and password with `admin.csv`. The `admin_name` and `admin_pw`are used to store the admin name and password get from the entrybox. The `admins` is a list to store the data from `admin.csv`. The `found` is set to be defalut as `0` when the admin data unfound and `1` for found. Then, the for loop will do the searching if admin data found and do the login process.Otherwise, the system will warn user the input is wrong. 

```python
admin_name = admin_name_Entry.get()
admin_pw = admin_pw_Entry.get()
admins = []
found = 0
for admin in admins:
    if admin_name == admin["AdminId"] and admin_pw == admin["AdminPw"]:
        found = 1
if found == 0:
    tkmsg.showerror(message="Error, your user name or password is wrong, try again.")
else:
```

<font color=#FFCCCB>III. login process</font>  
The following python code is used to do the login process when the admin data verified. It will tell user sucessfully login, close the login window and open the mainapp window.
```python
tkmsg.showinfo(title="Welcome", message="How are you? " + admin_name)
login.destroy()
import project
project.set_admin(admin_name)
project.openapp()
```

___
### 2. mainapp
The mainapp contains lots of function which have 3 main purpose: <font color="yellow">I. Numerical keyboard</font>, <font color="lightblue">II. Product table</font> and <font color=#FFCCCB>III. Payment process</font>  

<font color="yellow">I. Numerical keyboard</font>  
The following python code is used to enter the numerical data into different entry(Product ID Entry, Quantity Entry and Payment Entry)

`def num_Entry(text):` is used to enter the value by clicking each number key in numberical keyboard and pass it to different entry. It also except error i.e. pointing nowhere but click the number key and try to pass the value.

`def idEntry_focusIn(event):`  , `def payEntry_focusIn(event):`  ,  `def QtyEntry_focusIn(event):` are used for those 3 different entry, when an entry is being click and waiting input, these function are used to tell the computer which entry is being used and store that entry value in `global getentry`. And that is used in function `num_Entry(text)` to enter the receiving number into that entry.
```python
getentry = None

def num_Entry(text):
    global getentry
    en = getentry
    try:
        entry = en.get()
        entry = entry + text
        en.delete(0, "end")
        en.insert("end", entry)
    except AttributeError or UnboundLocalError:
        pass

def retur(text):
    global getentry
    getentry = text

def idEntry_focusIn(event):
    retur(Id_Entry)

def payEntry_focusIn(event):
    retur(pay_Entry)

def QtyEntry_focusIn(event):
    retur(Qty_Entry)

Example:
Id_Entry.bind("<FocusIn>", idEntry_focusIn)
```  

<font color="lightblue">II. Product table</font>
`Enter_Value` is used to store the Id entered value. `Enter_qty` is used to store the quantity bought of the Product. `int_check(Enter_qty)` will verify the data type of `Enter_qty` in case of any malfunction. And then, `getPInfo(Enter_Value)` will verify the product ID. After that, `re_insert(getPInfo(Enter_Value),Enter_qty)` will insert the data into treeview table which list the product info and `cal_total(getPInfo(Enter_Value),Enter_qty)` calculate the total price of those products.

```python
def num_Enter():
    Enter_Value = Id_Entry.get()
    Enter_qty = Qty_Entry.get()
    if int_check(Enter_qty):
        if getPInfo(Enter_Value) != -1:
            re_insert(getPInfo(Enter_Value),Enter_qty)
            cal_total(getPInfo(Enter_Value),Enter_qty)
            Id_Entry.delete(0, "end")
            Qty_Entry.delete(0, "end")
            qty_entry_var.set("1")
        else:
            tkmsg.showwarning(title="Id not Found!", message='Id not Found!')
            Id_Entry.delete(0, "end")
    else:
        tkmsg.showwarning(title="Warning!", message="Quantity is invalid!")

def getPInfo(ProductId):
    with open("Product.csv") as file:
        reader = csv.DictReader(file)
        Products = []
        for row in reader:
            Products.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})

        for Product in Products:
            if ProductId == Product["PId"]:
                return f"{Product['PId']} {Product['PName']} {Product['PPrice']}"
        return -1

def re_insert(PInfo,qt):
    global count
    PId, PName, PPrice = PInfo.split(" ")
    receipt.insert(parent="", index="end", iid=count, values=(PId, PName, qt, PPrice))
    count += 1

def cal_total(PInfo,qt):
    global cal_sum
    _,_,PPrice = PInfo.split(" ")
    cal_sum = cal_sum + float(PPrice) * int(qt)
    cal_total_var.set(f"${cal_sum}")
```  

<font color=#FFCCCB>III. Payment process</font>  
The following python code is used to do the payment process. It will get the total price from `caltotal_Entry` and get the payment from `pay_Entry`. Then, it will calculate the change and pass all the data into `writetempcsv()` which store all the data of this transaction for `savepdf.py` as to save as a receipt.

```python
def pay_change():
    pay = pay_Entry.get()
    _,Tot = caltotal_Entry.get().split("$")
    if pay == "":
        tkmsg.showwarning(title="Payment warning!", message='Payment is null')
    else:
        if float(pay) < float(Tot):
            tkmsg.showwarning(title="Payment warning!", message='It is not enough to pay')
            set_0pay()
        else:
            change = float(pay) - float(Tot)
            change_var.set(f"${change}")
            writetempcsv()
            import savepdf
            savepdf.makepdf()

def writetempcsv():
    return_all_to_savepdf()
    item = []
    Product = []
    for record in receipt.get_children():
        item.append(receipt.item(record)["values"])
    for row in item:
        Product.append({"PId": row[0], "Product": row[1], "Qty": row[2],"Price": f"${row[3]}"})
    with open("tempreceipt.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["PId","Product","Qty","Price"])
        writer.writeheader()
        writer.writerows(Product)
```
___
### 3. admin control  
The admin control is provided 2 function with <font color=#FFCCCB>admin</font> and <font color="lightblue">product management</font>. The following python code is used to turn to admin, product or mainapp window.

```python
def add_admin():
    admins.destroy()
    import addadmin
    addadmin.openadding()

def add_product():
    admins.destroy()
    import product_management
    product_management.openProduct_m()

def back_to_admin():
    admins.destroy()
    project.openapp()
```
### 3.1 admin management
`addadmin.py` provided `Regular expression` to validate the input admin name and password. (1)admin name should start with capital letter with combination of letters and numbers which lengths between 8-14.(2)password should start with keyboard's symbol with combination of letters and numbers.  
(3) the input admin name and password is then write into the csv file `admin.csv` after user's double confirmation

```python
def name_validation(name):
    if re.search(r"^[A-Z]+(?=.*[a-zA-z])+(?=.*[0-9])", name):
        return True
    else:
        return False
    
def pw_validation(pw):
    if re.search(r"^[.!#$%&'*+\/=?^_`{|}~-]+(?=.*[a-zA-z])+(?=.*[0-9])", pw):
        return True
    else:
        return False
    
def name_length_check(name):
    if len(name) > 7 and len (name) < 15:
        return True
    else:
        return False
    
def pw_length_check(pw):
    if len(pw) > 7 and len(pw) < 13:
        return True
    else:
        return False

def adding_admin():
    admin_name = add_admin_name_Entry.get()
    admin_pw = add_admin_pw_Entry.get()
    if tkmsg.askyesno(title="Hi", message=f"Is admin name:{admin_name} and password:{admin_pw}?"):
        with open('admin.csv', 'a') as usr_file:
            writer = csv.DictWriter(usr_file, fieldnames=["AdminId", "AdminPw"])
            writer.writerow({"AdminId": admin_name, "AdminPw": admin_pw})
            tkmsg.showinfo(title="Welcome", message="You are successfully registered!")
            add_admin_name_Entry.delete(0, "end")
            add_admin_pw_Entry.delete(0, "end")
    else:
        add_admin_name_Entry.delete(0, "end")
        add_admin_pw_Entry.delete(0, "end")
        tkmsg.showwarning(title="Warning", message="Please enter again!")
```
___
### 4. product control
The product control provided 4 function to link to each window:adding, deleting, modifying and reviewing.

```python
def writeProduct():
    product_m.destroy()
    import writeProduct
    writeProduct.openwP()

def deleteProduct():
    product_m.destroy()
    import deleteProduct
    deleteProduct.opendP()

def changePrice():
    global pmopen
    pmopen = "pm"
    product_m.destroy()
    import changePrice
    changePrice.opencP()

def viewProduct():
    product_m.destroy()
    import viewProduct
    viewProduct.openvP("pm")

def back_to_admin():
    product_m.destroy()
    import admin
    admin.openadmin()
```
___
### 4.1 product adding
`writeProduct.py` is used to add product info into csv file `Product.csv`. To validate price, the price can only be `float` type. And, the input id should be `numberic` type. The function will validate the product in csv file `Product.csv` and write it in csv file `Product.csv` if the product is not duplicated.


```python
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
        
def input_correct(id,price,id_found):
    if id.isnumeric() and is_float(price) and id_found == 0 :
        return True
    else:
        return False
    
def find_product(P_Id):
    with open("Product.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["PId"] == P_Id:
                return 1
        return 0

def enter_Product():
    P_Id = Entry_PId.get().strip()
    P_Name = Entry_PName.get().strip()
    P_Price = Entry_PPrice.get().strip()
    Id_found = find_product(P_Id)
    if Id_found == 1:
        tkmsg.showwarning(title="Warning", message="Product Id is duplicated with database")
        Entry_PId.delete(0, "end")
    if input_correct(P_Id,P_Price,Id_found) and tkmsg.askyesno(title="Question", message=f"Check if it is correct: \nProduct Id:{P_Id}\nProduct Name:{P_Name}\nProduct Price:{P_Price}"):
        with open("Product.csv", "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["PId", "PName", "PPrice"])
            writer.writerow({"PId": P_Id, "PName": P_Name, "PPrice": P_Price})
    else:
        tkmsg.showwarning(title="Warning", message="Please make sure product Id and Price is valid!")
```
___
### 4.2 product deleting  
`deleteProduct.py` is used to delete the unwanted product by inputting product id.It will first search the product id in csv file `Product.csv`. If the product is in the file, that product id will not be appended into the new product list.Then, the new product list will write all the appended product to the csv file `Product csv`.

```python
def delete_Id():
        P_Id = Entry_PId.get().strip()
        tempProducts = []
        found = 0
        with open("Product.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["PId"] != P_Id:
                    tempProducts.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})
                else:
                    found = 1
        if found == 0:
            tkmsg.showwarning(title="Warning!", message="Product not found")
            Entry_PId.delete(0, "end")
        else:
            with open("Product.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["PId", "PName", "PPrice"])
                writer.writeheader()
                writer.writerows(tempProducts)
            Entry_PId.delete(0, "end")
            tkmsg.showinfo(title="", message=f"Product {P_Id} has been deleted")
```
___
### 4.3 product modifying
`changePrice` is used to modify the price of the product by inputting product id.It will first search the product id in csv file `Product.csv` and validate the data type of price.If the product is in the file, it will change the price in that product and append it into new temporary list. Then, the temp list will be appended into csv file `Product.csv`.

```python
def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

def change_Price():
    P_Id = Entry_PId.get()
    P_Price = Entry_PPrice.get()
    tempProducts = []
    found = 0
    if is_float(P_Price):
        with open("Product.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["PId"] == P_Id:
                    found = 1
                    row["PPrice"] = P_Price
                tempProducts.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})
        if found == 0:
            tkmsg.showwarning(title="Warning!", message="Product not found")
            Entry_PId.delete(0, "end")
        else:
            with open("Product.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["PId", "PName", "PPrice"])
                writer.writeheader()
                writer.writerows(tempProducts)
            Entry_PId.delete(0, "end")
            Entry_PPrice.delete(0, "end")
            tkmsg.showinfo(title="", message=f"Product {P_Id} has been changed to ${P_Price}")
    else:
        tkmsg.showwarning(title="Warning", message="Price is invalid")
        Entry_PPrice.delete(0, "end")
```
___
### 4.4 porduct reviewing
`viewProduct.csv` is used to search and view list of product that save in csv file `Product.csv`. User can search it by similar or exact id, name and price of product. All the product info are listed on treeview table. 

```python
def fileimporttree():
      with open("Product.csv") as file:
         reader = csv.DictReader(file)
         Products = []
         for row in reader:
               Products.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})
      
      for row in Products:
         global count
         Review.insert(parent="", index="end", iid=count, values=(row["PId"], row["PName"], row["PPrice"]))
         count += 1
      count = 0
```

That is total 8 combination of searching the product as id, name or price. Therefore, there are 8 functions listed as the order of the truth table. The 8 functions will update each different wanted product info into the treeview table and refreshed every 0.1s by `refresh()`.
```python
def refresh():
      #T for == | F for !=
      #TTT#
      #TTF#
      #TFT#
      #TFF#
      #FTT#
      #FTF#
      #FFT#
      #FFF#
      global glo_id, glo_name, glo_price, afterid
      getid = PID_Entry.get()
      getname = PName_Entry.get()
      getprice = Price_Entry.get()
      if getid == "" and getname == "" and getprice == "":#TTT#
         clearAll()
         fileimporttree()
      elif getid == "" and getname == "" and getprice != "":#TTF# Price
         if glo_price == getprice:
            pass
         else:
            glo_price = getprice
            clearAll()
            Price(getprice)
      elif getid == "" and getname != "" and getprice == "":#TFT# Name
         if glo_name == getname:
            pass
         else:
            glo_name = getname
            clearAll()
            Name(getname)
      elif getid == "" and getname != "" and getprice != "":#TFF# Name + Price
         if glo_name == getname and glo_price == getprice:
            pass
         else:
            glo_name = getname
            glo_price = getprice
            clearAll()
            Name_Price(getname,getprice)
      elif getid != "" and getname == "" and getprice == "":#FTT# Id
         if glo_id == getid:
            pass
         else:
            glo_id = getid
            clearAll()
            Id(getid)
      elif getid != "" and getname == "" and getprice != "":#FTF# Id + price
         if glo_id == getid and glo_price == getprice:
            pass
         else:
            glo_id = getid
            glo_price = getprice
            clearAll()
            Id_Price(getid,getprice)
      elif getid != "" and getname != "" and getprice == "":#FFT# Id + Name
         if glo_id == getid and glo_name == getname:
            pass
         else:
            glo_id = getid
            glo_name = getname
            clearAll()
            Id_Name(getid,getname)
      else:#FFF# 
         if glo_id == getid and glo_name == getname and glo_price == getprice:
            pass
         else:
            glo_id = getid
            glo_name = getname
            glo_price = getprice
            clearAll()
            All(getid,getname,getprice)
      
      afterid = Review.after(500,refresh)

   def Price(Price):
      with open("Product.csv") as file:
         reader = csv.DictReader(file)
         PriceProducts = []
         for row in reader:
            if row["PPrice"].startswith(Price):
               PriceProducts.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})
      for row in PriceProducts:
         global count
         Review.insert(parent="", index="end", iid=count, values=(row["PId"], row["PName"], row["PPrice"]))
         count += 1
      count = 0

   def Name(Name):
      with open("Product.csv") as file:
         reader = csv.DictReader(file)
         NameProducts = []
         for row in reader:
            if row["PName"].startswith(Name):
               NameProducts.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})
      for row in NameProducts:
         global count
         Review.insert(parent="", index="end", iid=count, values=(row["PId"], row["PName"], row["PPrice"]))
         count += 1
      count = 0

   def Name_Price(Name,Price):
      with open("Product.csv") as file:
         reader = csv.DictReader(file)
         Name_PriceProducts = []
         for row in reader:
            if row["PName"].startswith(Name) and row["PPrice"].startswith(Price):
               Name_PriceProducts.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})
      for row in Name_PriceProducts:
         global count
         Review.insert(parent="", index="end", iid=count, values=(row["PId"], row["PName"], row["PPrice"]))
         count += 1
      count = 0

   def Id(Id):
      with open("Product.csv") as file:
         reader = csv.DictReader(file)
         IdProducts = []
         for row in reader:
            if row["PId"].startswith(Id):
               IdProducts.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})
      for row in IdProducts:
         global count
         Review.insert(parent="", index="end", iid=count, values=(row["PId"], row["PName"], row["PPrice"]))
         count += 1
      count = 0

   def Id_Price(Id,Price):
      with open("Product.csv") as file:
         reader = csv.DictReader(file)
         Id_PriceProducts = []
         for row in reader:
            if row["PId"].startswith(Id) and row["PPrice"].startswith(Price):
               Id_PriceProducts.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})
      for row in Id_PriceProducts:
         global count
         Review.insert(parent="", index="end", iid=count, values=(row["PId"], row["PName"], row["PPrice"]))
         count += 1
      count = 0

   def Id_Name(Id,Name):
      with open("Product.csv") as file:
         reader = csv.DictReader(file)
         Id_NameProducts = []
         for row in reader:
            if row["PId"].startswith(Id) and row["PName"].startswith(Name):
               Id_NameProducts.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})
      for row in Id_NameProducts:
         global count
         Review.insert(parent="", index="end", iid=count, values=(row["PId"], row["PName"], row["PPrice"]))
         count += 1
      count = 0

   def All(Id,Name,Price):
      with open("Product.csv") as file:
         reader = csv.DictReader(file)
         AllProducts = []
         for row in reader:
            if row["PId"].startswith(Id) and row["PName"].startswith(Name) and row["PPrice"].startswith(Price):
               AllProducts.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})
      for row in AllProducts:
         global count
         Review.insert(parent="", index="end", iid=count, values=(row["PId"], row["PName"], row["PPrice"]))
         count += 1
      count = 0

```