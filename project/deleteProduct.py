import tkinter as tk
import tkinter.messagebox as tkmsg
import csv


def opendP():
    dP = tk.Tk()
    dP.title("Delete Product")
    dP.geometry("400x250")

    photo = tk.PhotoImage(file = "logo/Store logo.png")
    dP.iconphoto(False, photo)

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



    def back_to_admin():
        dP.destroy()
        import product_management as pm
        pm.openProduct_m()

    PId = tk.StringVar()

    button_add_back = tk.Button(dP, text="Back to managemnet", font="Helvetica 16 bold", command=back_to_admin)
    button_add_back.place(x=0, y=0)

    PId_label = tk.Label(dP, text="Product Id", font="Helvetica 16 bold")
    PId_label.place(x=110, y=70, width=180)

    Entry_PId = tk.Entry(dP, textvariable=PId, font="Helvetica 16 bold")
    Entry_PId.place(x=110, y=100, width=180)

    button_enter = tk.Button(dP, text="Delete", font="Helvetica 16 bold", bd=4, command=delete_Id)
    button_enter.place(x=160, y=180)

    dP.mainloop()