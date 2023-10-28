import tkinter as tk
import tkinter.messagebox as tkmsg
import csv
import tkinter.ttk as ttk
from datetime import datetime

count = 0
cal_sum = 0
admin_name =""
getentry = None
after_id = 0

reTotal = ""
rePay = ""
reChange = ""

def int_check(text):
        try:
            int(text)
            return True
        except ValueError:
            return False

def set_admin(name):
    global admin_name
    admin_name = name

def get_admin():
    global admin_name
    return admin_name

def retuTotal():
    global reChange
    return reTotal

def retuPay():
    global rePay
    return rePay

def retuChange():
    global reChange
    return reChange

def getPInfo(ProductId):
        with open("Product.csv") as file:
            reader = csv.DictReader(file)
            Products = []
            for row in reader:
                Products.append({"PId": row["PId"], "PName": row["PName"],"PPrice": row["PPrice"]})

            for Product in Products:
                if ProductId == Product["PId"]:
                    return f"{Product['PId']},{Product['PName']},{Product['PPrice']}"
            return -1

def openapp():
    cashier = tk.Tk()
    cashier.title("Cashier")
    cashier.geometry("1260x900")

    photo = tk.PhotoImage(file = "logo/Store logo.png")
    cashier.iconphoto(False, photo)

    def idEntry_focusIn(event):
        retur(Id_Entry)

    def payEntry_focusIn(event):
        retur(pay_Entry)

    def QtyEntry_focusIn(event):
        retur(Qty_Entry)

    def retur(text):
        global getentry
        getentry = text

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


    def num_Backspace():
        global getentry
        en = getentry
        entry = en.get()
        entry = entry[:-1]
        en.delete(0, "end")
        en.insert("end", entry)


    def num_Clear():
        global getentry
        en = getentry
        en.delete(0, "end")


    def re_insert(PInfo,qt):
        global count
        PId, PName, PPrice = PInfo.split(",")
        receipt.insert(parent="", index="end", iid=count, values=(PId, PName, qt, PPrice))
        count += 1

    def cal_total(PInfo,qt):
        global cal_sum
        _,_,PPrice = PInfo.split(",")
        cal_sum = cal_sum + float(PPrice) * int(qt)
        cal_total_var.set(f"${cal_sum}")

    def del_Price():
        global cal_sum
        selec = receipt.selection()
        for record in selec:
            item = receipt.item(record)["values"]
            Price = item[3]
            cal_sum -= float(Price)
            cal_total_var.set(f"${cal_sum}")

    def set_0P():
        global cal_sum
        cal_sum = 0
        cal_total_var.set(f"${cal_sum}")

    def set_0C():
        change_var.set("$0")

    def set_0pay():
        pay_Entry.delete(0, "end")

    def remove_all():
        set_0P()
        set_0C()
        set_0pay()
        for record in receipt.get_children():
            receipt.delete(record)
        

    def remove_selec():
        del_Price()
        set_0C()
        set_0pay()
        selec = receipt.selection()
        for record in selec:
            receipt.delete(record)

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

    def logout():
        global after_id
        time_label.after_cancel(after_id)
        cashier.destroy()
        import login
        login.openlog()

    def openadmin():
        global after_id
        time_label.after_cancel(after_id)
        cashier.destroy()
        import admin
        admin.openadmin()

    
    def update_clock():
        nowtime = datetime.now()
        now_date = nowtime.strftime("%Y-%m-%d %a")
        now_time = nowtime.strftime("%H:%M:%S")
        date_label.config(text=now_date)
        time_label.config(text=now_time)
        global after_id
        after_id = time_label.after(1000,update_clock)

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

    def return_all_to_savepdf():
        gettotal =  caltotal_Entry.get()
        global reTotal
        reTotal = gettotal
        getpay =  pay_Entry.get()
        global rePay
        rePay = getpay
        getchange = change_entry.get()
        global reChange
        reChange = getchange

    def viewproduct():
        global after_id
        time_label.after_cancel(after_id)
        cashier.destroy()
        import viewProduct
        viewProduct.openvP("main")

    #============================================Num/Id input============================================#
    Id_Entry_label = tk.Label(cashier, text="Product Id", font="Helvetica 20 bold")
    Id_Entry_label.place(x=880, y=10, width=160, height=40)

    Qty_Entry_label = tk.Label(cashier, text="Qty", font="Helvetica 20 bold")
    Qty_Entry_label.place(x=1160, y=10, width=70, height=40)

    Id_Entry = tk.Entry(cashier, font="Helvetica 20 bold")
    Id_Entry.bind("<FocusIn>", idEntry_focusIn)
    Id_Entry.place(x=780, y=60, width=360, height=30)

    qty_entry_var = tk.StringVar()
    qty_entry_var.set("1")

    Qty_Entry = tk.Entry(cashier, textvariable=qty_entry_var, font="Helvetica 20 bold")
    Qty_Entry.bind("<FocusIn>", QtyEntry_focusIn)
    Qty_Entry.place(x=1140, y=60, width=120, height=30)

    button_7 = tk.Button(cashier, text="7", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("7"))
    button_8 = tk.Button(cashier, text="8", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("8"))
    button_9 = tk.Button(cashier, text="9", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("9"))
    button_backspace = tk.Button(cashier, text="←", font="Helvetica 32 bold", bd=4, bg="#616669", command=num_Backspace)
    button_7.place(x=780, y=120, width=120, height=165)
    button_8.place(x=900, y=120, width=120, height=165)
    button_9.place(x=1020, y=120, width=120, height=165)
    button_backspace.place(x=1140, y=120, width=120, height=165)

    button_4 = tk.Button(cashier, text="4", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("4"))
    button_5 = tk.Button(cashier, text="5", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("5"))
    button_6 = tk.Button(cashier, text="6", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("6"))
    button_clear = tk.Button(cashier, text="C", font="Helvetica 32 bold", bd=4, bg="#616669", command=num_Clear)
    button_4.place(x=780, y=285, width=120, height=165)
    button_5.place(x=900, y=285, width=120, height=165)
    button_6.place(x=1020, y=285, width=120, height=165)
    button_clear.place(x=1140, y=285, width=120, height=165)

    button_1 = tk.Button(cashier, text="1", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("1"))
    button_2 = tk.Button(cashier, text="2", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("2"))
    button_3 = tk.Button(cashier, text="3", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("3"))
    button_enter = tk.Button(cashier, text="Enter", width=7, height=8, font="Helvetica 24 bold", bd=4, bg="#616669",command=num_Enter)
    button_1.place(x=780, y=450, width=120, height=165)
    button_2.place(x=900, y=450, width=120, height=165)
    button_3.place(x=1020, y=450, width=120, height=165)
    button_enter.place(x=1140, y=450, width=120, height=330)

    button_0 = tk.Button(cashier, text="0", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("0"))
    button_dot = tk.Button(cashier, text=".", font="Helvetica 32 bold", bg="#fae7af", bd=4, command=lambda: num_Entry("."))
    button_0.place(x=780, y=615, width=240, height=165)
    button_dot.place(x=1020, y=615, width=120, height=165)

    #============================================Treeview============================================#
    receipt = ttk.Treeview(cashier)

    #define colums
    receipt["columns"] = ("PId", "Product Name", "Qty", "Price")

    #formate colums
    receipt.column("#0", width=0, stretch="NO")
    receipt.column("PId", anchor="w", width=80)
    receipt.column("Product Name", anchor="w", width=120)
    receipt.column("Qty", anchor="center", width=60)
    receipt.column("Price", anchor="center", width=60)

    #create heading
    receipt.heading("#0", text="", anchor="w")
    receipt.heading("PId",text="PId", anchor="w")
    receipt.heading("Product Name",text="Product Name", anchor="w")
    receipt.heading("Qty", text="Qty", anchor="center")
    receipt.heading("Price", text="Price", anchor="center")

    #add data parents:put thing inside another thing||| index="end":put thing at the bottom||| id cant repeat!!
    #receipt.insert(parent="", index="end", iid=0, values=("012", "AWater", 1, "8"))

    receipt.place(x=500,y=300, anchor="center", width=550, height=580) #x800

    button_remove_all = tk.Button(cashier, text="Remove All", font="Helvetica 22 bold", bd=4, command=remove_all)
    button_remove_all.place(x=225, y=590, width=275, height=95)

    button_remove_selec = tk.Button(cashier, text="Remove Selected", font="Helvetica 22 bold", bd=4, command=remove_selec)
    button_remove_selec.place(x=225, y=685, width=275, height=95)
    
    tree_scroll = tk.Scrollbar(receipt)
    tree_scroll.pack(side="right", fill="y")
    tree_scroll.config(command=receipt.yview)
    receipt.config(yscrollcommand=tree_scroll.set)


    #============================================Calculation============================================#
    change_var = tk.StringVar()
    change_var.set("$0")
    cal_total_var = tk.StringVar()
    cal_total_var.set("$0")

    pay_Label = tk.Label(cashier, text="Payment:", font="Helvetica 18 bold")
    pay_Label.place(x=500, y=590, width=110, height=34)
    pay_Entry = tk.Entry(cashier, font="Helvetica 18 bold")
    pay_Entry.bind("<FocusIn>", payEntry_focusIn)
    pay_Entry.place(x=610, y=590, width=165, height=34)

    caltotal_label = tk.Label(cashier, text="Total: ", font="Helvetica 18 bold")
    caltotal_label.place(x=500, y=624, width=110, height=34)
    caltotal_Entry = tk.Entry(cashier, textvariable=cal_total_var, font="Helvetica 18 bold", disabledforeground="red", state="disabled")
    caltotal_Entry.place(x=610, y=624, width=165, height=34)

    change_label = tk.Label(cashier, text="Change: ", font="Helvetica 18 bold")
    change_label.place(x=500, y=658, width=110, height=34)
    change_entry = tk.Entry(cashier, textvariable=change_var, font="Helvetica 18 bold", state="disabled")
    change_entry.place(x=610, y=658, width=165, height=34)

    button_pay = tk.Button(cashier, text="Pay", font="Helvetica 36 bold", fg="red", bd=4, command=pay_change)
    button_pay.place(x=500, y=692, width=275, height=88)

    #============================================left function============================================#
    button_admin = tk.Button(cashier, text="Admin", font="Helvetica 18 bold", fg="red", bd=4, command=openadmin)
    button_admin.place(x=0, y=0, height=60)
    button_logout = tk.Button(cashier, text="logout", font="Helvetica 18 bold", fg="red", bd=4, command=logout)
    button_logout.place(x=0, y=840, height=60)

    date_label = tk.Label(cashier, text="", font="Helvetica 18 bold")
    date_label.place(x=1040, y=780, width=240, height=30)
    time_label = tk.Label(cashier, text="", font="Helvetica 18 bold")
    time_label.place(x=1040, y=810, width=240, height=30)
    update_clock()

    showname = tk.StringVar()
    showname.set(get_admin())
    show_label = tk.Label(cashier, textvariable=showname, font="Helvetica 18 bold")
    show_label.place(x=1030, y=840, width=240, height=50)

    button_view_product = tk.Button(cashier, text="Product Review", font="Helvetica 18 bold", bd=4, command=viewproduct)
    button_view_product.place(x=0, y=100, height=60)

    #========================================================================================#
    cashier.mainloop()


def main():
   import login
   login.openlog()



if __name__ == "__main__":
   main()
