import tkinter as tk
import tkinter.messagebox as tkmsg
import csv

def is_float(text):
        try:
            float(text)
            return True
        except ValueError:
            return False

def opencP():
    cP = tk.Tk()
    cP.title("Change Price")
    cP.geometry("400x250")

    photo = tk.PhotoImage(file = "logo/Store logo.png")
    cP.iconphoto(False, photo)

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

    def back_to_admin():
        cP.destroy()
        import product_management as pm
        pm.openProduct_m()

    PId = tk.StringVar()
    PPrice = tk.StringVar()

    button_add_back = tk.Button(cP, text="Back to managemnet", font="Helvetica 16 bold", command=back_to_admin)
    button_add_back.place(x=0, y=0)

    PId_label = tk.Label(cP, text="Product Id", font="Helvetica 16 bold")
    PId_label.place(x=10, y=70, width=180)
    PPrice_label = tk.Label(cP, text="Product Price", font="Helvetica 16 bold")
    PPrice_label.place(x=210, y=70, width=180)

    Entry_PId = tk.Entry(cP, textvariable=PId, font="Helvetica 16 bold")
    Entry_PId.place(x=10, y=100, width=180)
    Entry_PPrice = tk.Entry(cP, textvariable=PPrice, font="Helvetica 16 bold")
    Entry_PPrice.place(x=210, y=100, width=180)

    button_enter = tk.Button(cP, text="Change", font="Helvetica 16 bold", bd=4, command=change_Price)
    button_enter.place(x=160, y=180)

    cP.mainloop()