import tkinter as tk
import csv
import tkinter.messagebox as tkmsg
import re


after_id = 0

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


def openadding():

    adding = tk.Tk()
    adding.title("Add admin")
    adding.geometry("400x350")

    photo = tk.PhotoImage(file = "logo/Store logo.png")
    adding.iconphoto(False, photo)
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
    
    def update_namef_check():
        admin_name = add_admin_name_Entry.get()
        if name_validation(admin_name):
            update_namef_var.set("✓ Start with uppercase,\n include letter & number")
            return True
        else:
            update_namef_var.set("✗ Start with uppercase,\n include letter & number")
            return False

    def update_namer_check():
        admin_name = add_admin_name_Entry.get()
        if name_length_check(admin_name):
            update_namer_var.set("✓ 8-14 letters")
            return True
        else:
            update_namer_var.set("✗ 8-14 letters")
            return False

    def update_pwf_check():
        admin_pw = add_admin_pw_Entry.get()
        if pw_validation(admin_pw):
            update_pwf_var.set("✓ Starting with symbol, include\nuppercase, letter & number")
            return True
        else:
            update_pwf_var.set("✗ Starting with symbol, include\nuppercase, letter & number")
            return False
        
    def update_pwr_check():
        admin_pw = add_admin_pw_Entry.get()
        if pw_length_check(admin_pw):
            update_pwr_var.set("✓ 8-12 letters")
            return True
        else:
            update_pwr_var.set("✗ 8-12 letters")
            return False

    def update_addcheck():
        getnf = update_namef_check()
        getnr = update_namer_check()
        getpwf = update_pwf_check()
        getpwr = update_pwr_check()
        if getnf and getnr and getpwf and getpwr:
            button_add_admin.config(state="active")
        else:
            button_add_admin.config(state="disabled")
        global after_id
        after_id = adding.after(100,update_addcheck)



    def back_to_admin():
        global after_id
        adding.after_cancel(after_id)
        adding.destroy()
        import admin
        admin.openadmin()

    tk.Label(adding, text="New name: ", font="Helvetica 12").place(x=50, y= 100)
    tk.Label(adding, text="Password: ", font="Helvetica 12").place(x=50, y= 180)

    add_admin_name_var = tk.StringVar()
    add_admin_name_Entry = tk.Entry(adding, textvariable=add_admin_name_var, font="Helvetica 12")
    add_admin_name_Entry.place(x=150, y=100)

    update_namef_var = tk.StringVar()
    update_namef_var.set("✗ Starting with uppercase,\n include letter & number")
    update_namef_label = tk.Label(adding, textvariable=update_namef_var, font="Helvetica 12")
    update_namef_label.place(x=150, y=120)

    update_namer_var = tk.StringVar()
    update_namer_var.set("✗ 8-14 letters")
    update_namer_label = tk.Label(adding, textvariable=update_namer_var, font="Helvetica 12")
    update_namer_label.place(x=150, y=160)

    add_admin_pw_var = tk.StringVar()
    add_admin_pw_Entry = tk.Entry(adding, textvariable=add_admin_pw_var, show="*", font="Helvetica 12")
    add_admin_pw_Entry.place(x=150, y=190)

    update_pwf_var = tk.StringVar()
    update_pwf_var.set("✗ Starting with symbol, include\nuppercase, letter & number")
    update_pwf_label = tk.Label(adding, textvariable=update_pwf_var, font="Helvetica 12")
    update_pwf_label.place(x=150, y=210)

    update_pwr_var = tk.StringVar()
    update_pwr_var.set("✗ 8-12 letters")
    update_pwr_label = tk.Label(adding, textvariable=update_pwr_var, font="Helvetica 12")
    update_pwr_label.place(x=150, y=250)

    button_add_admin = tk.Button(adding, text="ADD", font="Helvetica 16 bold", command=adding_admin)
    button_add_admin.place(x=170, y=280)
    button_add_admin.config(state="disabled")

    update_addcheck()

    button_add_back = tk.Button(adding, text="Back to admin", font="Helvetica 16 bold", command=back_to_admin)
    button_add_back.place(x=0, y=0)

    
    adding.mainloop()