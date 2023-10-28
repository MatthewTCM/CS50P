import tkinter as tk
import tkinter.messagebox as tkmsg
import csv

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

def openwP():
    wP = tk.Tk()
    wP.title("Add Product")
    wP.geometry("600x250")

    photo = tk.PhotoImage(file = "logo/Store logo.png")
    wP.iconphoto(False, photo)

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
            PId.set("")
            PName.set("")
            PPrice.set("")
        else:
            tkmsg.showwarning(title="Warning", message="Please make sure product Id and Price is valid!")

    def back_to_admin():
        wP.destroy()
        import product_management as pm
        pm.openProduct_m()


    PId = tk.StringVar()
    PName = tk.StringVar()
    PPrice = tk.StringVar()

    button_add_back = tk.Button(wP, text="Back to managemnet", font="Helvetica 16 bold", command=back_to_admin)
    button_add_back.place(x=0, y=0)

    PId_label = tk.Label(wP, text="Product Id", font="Helvetica 16 bold")
    PName_label = tk.Label(wP, text="Product Name", font="Helvetica 16 bold")
    PPrice_label = tk.Label(wP, text="Product Price", font="Helvetica 16 bold")
    PId_label.place(x=10, y=70, width=180)
    PName_label.place(x=210, y=70, width=180)
    PPrice_label.place(x=410, y=70, width=180)

    Entry_PId = tk.Entry(wP, textvariable=PId, font="Helvetica 16 bold")
    Entry_PId.place(x=10, y=100, width=180)
    Entry_PName = tk.Entry(wP, textvariable=PName, font="Helvetica 16 bold")
    Entry_PName.place(x=210, y=100, width=180)
    Entry_PPrice = tk.Entry(wP, textvariable=PPrice, font="Helvetica 16 bold")
    Entry_PPrice.place(x=410, y=100, width=180)

    button_enter = tk.Button(wP, text="Add", font="Helvetica 16 bold", bd=4, command=enter_Product)
    button_enter.place(x=260, y=180)
    wP.mainloop()