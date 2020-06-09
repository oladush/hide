import tkinter
import ctypes
import pyglet

pyglet.font.add_file("interface/font/circula-medium.otf")
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# password_true = "12345"
# error_count = 5


def main(password_true, error_count):
    password_status = False

    def enter(event):
        nonlocal label, password_status, password_true, error_count
        password = form.get()
        if password == password_true:
            error_count = 5
            password_status = True
            root.destroy()
        else:
            error_count -= 1
            text = 'permission denied: ' + str(error_count)
            error_text = tkinter.Label(root, text=text, font='circula-medium 12', fg="red", bg="black")
            error_text.place(relx=.5, rely=.75, anchor="center")

        if error_count <= 0:
            block()
            password_status = False

    def block():
        nonlocal label, form
        try:
            label.destroy()
            form.destroy()
        except NameError:
            pass
        label = tkinter.Label(root, text="ooops", font="circula-medium 25", fg="white", bg="black", relief="flat")
        label.place(relx=.5, rely=.4, anchor="center")

    root = tkinter.Tk()

    root.title("")
    root.geometry("600x300")
    root.iconbitmap("interface/icon/lock.ico")
    root.configure(background='black')
    root.resizable(width=False, height=False)

    if error_count > 0:
        label = tkinter.Label(root, text="enter password", font="circula-medium 25", fg="white", bg="black",
                              relief="flat")
        label.place(relx=.5, rely=.4, anchor="center")

        form = tkinter.Entry(root, font='Arial 22', show="•", relief="flat", justify="center")
        form.place(relx=.5, rely=.60, anchor="center", width=250, height=30)
        form.focus()

        form.bind("<Return>", enter)
    else:
        block()

    root.mainloop()
    return password_status

