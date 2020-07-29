import tkinter
import ctypes
import pyglet

pyglet.font.add_file("interface/font/circula-medium.otf")
ctypes.windll.shcore.SetProcessDpiAwareness(True)


class PasswordWindow():
    """This class describe logic and appearance window for enter password"""

    def __init__(self, password_true, attempt_count):
        self.password_stat = False
        self.password_true = password_true
        self.attempt_count = attempt_count

    def enter(self, event):
        password = self.form.get()
        if password == self.password_true:
            self.password_stat = True
            self.root.destroy()
        else:
            self.attempt_count -= 1
            text = "permission denied: " + str(self.attempt_count)
            error_text = tkinter.Label(self.root, text=text, font=self.principal_font, fg=self.font_error_color, bg=self.background_color)
            error_text.place(relx=.5, rely=.75, anchor="center")

            if self.attempt_count <= 0:
                self.block()

    def run(self):

        self.root.title("")
        self.root.geometry("600x300")
        self.root.iconbitmap("interface/icon/lock.ico")
        self.root.configure(background=self.background_color)
        self.root.resizable(width=False, height=False)

        if self.attempt_count > 0:
            self.label = tkinter.Label(self.root, text="enter password", font=self.principal_font + "25", fg=self.font_color, bg=self.background_color, relief=self.relief_design)
            self.label.place(relx=.5, rely=.4, anchor="center")

            self.form = tkinter.Entry(self.root, font='Arial 22', show="•", relief=self.relief_design, justify="center")
            self.form.place(relx=.5, rely=.60, anchor="center", width=250, height=30)
            self.form.focus()

            self.form.bind("<Return>", self.enter)
        else:
            self.block()
        self.root.mainloop()
        return self.password_stat

    def block(self):
        self.label.destroy()
        self.form.destroy()

        self.label = tkinter.Label(self.root, text="ooops", font=self.principal_font + "25", fg=self.font_color, bg=self.background_color, relief=self.relief_design)
        self.label.place(relx=.5, rely=.4, anchor="center")

    root = tkinter.Tk()

    # внешний вид

    font_color = "white"
    font_error_color = "red"
    principal_font = "circula-medium "
    background_color = "black"
    relief_design = "flat"


