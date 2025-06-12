import tkinter as tk
from PIL import Image, ImageTk
from Directories.Templates.footer import add_dynamic_footer

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#D7C0AE")
        self.controller = controller

        # Canvas for background
        self.canvas = tk.Canvas(self, bg="#D7C0AE", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        add_dynamic_footer(self.canvas, "Images/KonohaMain.png", max_height=129)

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Login", font=("Arial", 20), bg="#D7C0AE", fg="#1A1A1A")
        label.place(relx=0.5, rely=0.1, anchor="center")

        back_button = tk.Button(
            self,
            text="Back",
            width=20,
            height=3,
            font="Poppins",
            fg="beige",
            bg="#ad0505",
            bd=2,
            relief="groove",
            command=lambda: self.controller.show_main()
        )
        back_button.place(relx=0.5, rely=0.3, anchor="center")
