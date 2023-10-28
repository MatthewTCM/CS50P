import tkinter as tk
import tkinter.messagebox as tkmsg
import csv


def openlog():
    login = tk.Tk()
    login.title("CS50 Login")
    login.geometry("450x450")

    def admin_login():
        admin_name = admin_name_Entry.get()
        admin_pw = admin_pw_Entry.get()
        admins = []
        found = 0
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
        
        for admin in admins:
            if admin_name == admin["AdminId"] and admin_pw == admin["AdminPw"]:
                found = 1
        if found == 0:
            tkmsg.showerror(message="Error, your user name or password is wrong, try again.")
            admin_name_var.set("")
            admin_pw_var.set("")
        else:
            tkmsg.showinfo(title="Welcome", message="How are you? " + admin_name)
            login.destroy()
            import project
            project.set_admin(admin_name)
            project.openapp()

    photo = tk.PhotoImage(file = "logo/Store logo.png")
    login.iconphoto(False, photo)

    canvas = tk.Canvas(login, height=200, width=200)
    image_file = tk.PhotoImage(file = "logo/Store logo.png")
    canvas.create_image(0,0, anchor="nw", image=image_file)
    canvas.pack(side="top")

    tk.Label(login, text="User name: ", font="Helvetica 12").place(x=100, y= 250)
    tk.Label(login, text="Password: ", font="Helvetica 12").place(x=100, y= 290)

    admin_name_var = tk.StringVar()
    admin_name_Entry = tk.Entry(login, textvariable=admin_name_var, font="Helvetica 12")
    admin_name_Entry.place(x=210, y=250)

    admin_pw_var = tk.StringVar()
    admin_pw_Entry = tk.Entry(login, textvariable=admin_pw_var, show="*", font="Helvetica 12")
    admin_pw_Entry.place(x=210, y=290)

    button_login = tk.Button(login, text="login", font="Helvetica 16 bold", command=admin_login)
    button_login.place(x=190, y=320)

    login.mainloop()
