import tkinter as tk
import tkinter.ttk as ttk
import csv

count = 0
glo_id = ""
glo_name = ""
glo_price = ""
afterid = ""

def openvP(returnedtext):
   view = tk.Tk()
   view.title("Product review")
   view.geometry("700x550")

   photo = tk.PhotoImage(file = "logo/Store logo.png")
   view.iconphoto(False, photo)

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

   def clearAll():
      for record in Review.get_children():
         Review.delete(record)

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
         glo_price = getprice
         clearAll()
         Price(getprice)
      elif getid == "" and getname != "" and getprice == "":#TFT# Name
         glo_name = getname
         clearAll()
         Name(getname)
      elif getid == "" and getname != "" and getprice != "":#TFF# Name + Price
         glo_name = getname
         glo_price = getprice
         clearAll()
         Name_Price(getname,getprice)
      elif getid != "" and getname == "" and getprice == "":#FTT# Id
         glo_id = getid
         clearAll()
         Id(getid)
      elif getid != "" and getname == "" and getprice != "":#FTF# Id + price
         glo_id = getid
         glo_price = getprice
         clearAll()
         Id_Price(getid,getprice)
      elif getid != "" and getname != "" and getprice == "":#FFT# Id + Name
         glo_id = getid
         glo_name = getname
         clearAll()
         Id_Name(getid,getname)
      else:#FFF# 
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

   def back():
      global afterid
      if returnedtext == "main":
         Review.after_cancel(afterid)
         view.destroy()
         import project
         project.openapp()
      else:
         Review.after_cancel(afterid)
         view.destroy()
         import product_management
         product_management.openProduct_m()



   Review = ttk.Treeview(view)

   Review["columns"] = ("PId", "Product Name", "Price")

   Review.column("#0", width=0, stretch="NO")
   Review.column("PId", anchor="w", width=20)
   Review.column("Product Name", anchor="w", width=80)
   Review.column("Price", anchor="w", width=20)

   Review.heading("#0", text="", anchor="w")
   Review.heading("PId",text="PId", anchor="w")
   Review.heading("Product Name",text="Product Name", anchor="w")
   Review.heading("Price", text="Price", anchor="w")

   Review.place(x=0,y=0, width=450, height=550)

   tree_scroll = tk.Scrollbar(Review)
   tree_scroll.pack(side="right", fill="y")
   tree_scroll.config(command=Review.yview)
   Review.config(yscrollcommand=tree_scroll.set)

   PID_label = tk.Label(view, text="PId", font="Helvetica 18 bold")
   PID_label.place(x=545, y=50)
   PID_Entry = tk.Entry(view, font="Helvetica 18 bold")
   PID_Entry.place(x=470, y=90, width=200)

   PName_label = tk.Label(view, text="Product Name", font="Helvetica 18 bold")
   PName_label.place(x=485, y=150)
   PName_Entry = tk.Entry(view, font="Helvetica 18 bold")
   PName_Entry.place(x=470, y=190, width=200)

   Price_label = tk.Label(view, text="Price", font="Helvetica 18 bold")
   Price_label.place(x=535, y=250)
   Price_Entry = tk.Entry(view, font="Helvetica 18 bold")
   Price_Entry.place(x=470, y=290, width=200)

   button_back = tk.Button(view, text="Back", font="Helvetica 18 bold", command=back)
   button_back.place(x=620, y=500)

   fileimporttree()
   refresh()

   view.mainloop()