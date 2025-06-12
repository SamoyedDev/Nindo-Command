import tkinter as tk
from Directories.Frames.login_page import LoginPage
from Directories.Templates.footer import add_dynamic_footer

# Main window
window = tk.Tk()
window.title("Nindo Command")
window.configure(bg="#D7C0AE")
window.geometry("1250x700")
window.iconbitmap("C:/Users/Mattie/PycharmProjects/TkinterTest/Images/Icons/Cubed.ico")

# Page manager
class App:
    def __init__(self, root):
        self.root = root
        self.main_page = tk.Frame(root, bg="#D7C0AE")
        self.login_page = LoginPage(root, self)

        self.show_main()

    def show_main(self):
        self.login_page.pack_forget()
        self.main_page.pack(fill="both", expand=True)
        self.build_main()

    def show_login(self):
        self.main_page.pack_forget()
        self.login_page.pack(fill="both", expand=True)

    def build_main(self):
        for widget in self.main_page.winfo_children():
            widget.destroy()

        header = tk.Label(self.main_page, text="Nindo Command", font=("Arial", 20), bg="#D7C0AE", fg="#1A1A1A", pady=25)
        header.pack()

        btn_frame = tk.Frame(self.main_page, bg="#D7C0AE")
        btn_frame.pack(pady=20)

        login_btn = tk.Button(
            btn_frame,
            text="Login",
            width=20,
            height=3,
            font="Poppins",
            fg="beige",
            bg="#05ad05",
            bd=2,
            relief="groove",
            command=self.show_login
        )
        login_btn.pack(side="left", padx=10)

        reg_btn = tk.Button(
            btn_frame,
            text="Register",
            width=20,
            height=3,
            font="Poppins",
            fg="beige",
            bg="#05ad05",
            bd=2,
            relief="groove"
        )
        reg_btn.pack(side="left", padx=10)

        # 💡 Add dynamic background footer to main_page
        canvas = tk.Canvas(self.main_page, bg="#D7C0AE", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        add_dynamic_footer(canvas, "Images/KonohaMain.png", max_height=129)


# Run app
app = App(window)
window.mainloop()
