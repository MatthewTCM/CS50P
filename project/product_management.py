import tkinter as tk

pmopen = ""

def retupm():
    global pmopen
    return pmopen

def openProduct_m():
    product_m = tk.Tk()
    product_m.title("Product manager")
    product_m.geometry("400x300")

    photo = tk.PhotoImage(file = "logo/Store logo.png")
    product_m.iconphoto(False, photo)

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

    button_add_back = tk.Button(product_m, text="Back to admin", font="Helvetica 16 bold", command=back_to_admin)
    button_add_back.place(x=0, y=0)

    button_add_product = tk.Button(product_m, text="Add Product", font="Helvetica 16 bold", bd=4, command=writeProduct)
    button_add_product.place(x=10, y=100, width=180)

    button_del_product = tk.Button(product_m, text="Delete Product", font="Helvetica 16 bold", bd=4, command=deleteProduct)
    button_del_product.place(x=210, y=100, width=180)

    button_change_price = tk.Button(product_m, text="Change Price", font="Helvetica 16 bold", bd=4, command=changePrice)
    button_change_price.place(x=10, y=200, width=180)

    button_view_product= tk.Button(product_m, text="Product Review", font="Helvetica 16 bold", fg="red", bd=4, command=viewProduct)
    button_view_product.place(x=210, y=200, width=180)

    product_m.mainloop()
