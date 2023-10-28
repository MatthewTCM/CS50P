import tkinter as tk
import project


def openadmin():

    admins = tk.Tk()
    admins.title("admin control pannel")
    admins.geometry("500x500")

    photo = tk.PhotoImage(file = "logo/Store logo.png")
    admins.iconphoto(False, photo)

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

    showname = tk.StringVar()
    showname.set(f"Welcome admin {project.get_admin()}!")

    button_add_back = tk.Button(admins, text="Back to main", font="Helvetica 16 bold", command=back_to_admin)
    button_add_back.place(x=0, y=0)

    show_label = tk.Label(admins, textvariable=showname, font="Helvetica 18 bold")
    show_label.place(x=100,y=60)


    button_add_admin = tk.Button(admins, text="Add admin", font="Helvetica 18 bold", bd=4, command=add_admin)
    button_add_admin.place(x=180,y=150)

    button_add_product = tk.Button(admins, text="Product Manage", font="Helvetica 18 bold", bd=4, command=add_product)
    button_add_product.place(x=150, y=240)

    admins.mainloop()