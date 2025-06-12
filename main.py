import tkinter as tk
from PIL import Image, ImageTk

# Create main window
window = tk.Tk()
window.title("Nindo Command")
window.configure(bg="#D7C0AE")
window.iconbitmap("C:/Users/Mattie/PycharmProjects/TkinterTest/Images/Icons/Cubed.ico")
window.minsize(width=1250, height=700)
window.maxsize(width=2000, height=1000)


# ========== PAGE MANAGEMENT ==========
main_page = tk.Frame(window, bg="#D7C0AE")
login_page = tk.Frame(window, bg="#D7C0AE")

pages = [main_page, login_page]
current_index = 0


def move_next_page():
    global current_index
    current_index += 1
    if current_index >= len(pages):
        current_index = 0  # Optional: loop back to start

    for p in pages:
        p.pack_forget()
    pages[current_index].pack(fill="both", expand=True)


# ========== MAIN PAGE CONTENT ==========
main_page_header = tk.Label(
    main_page,
    text="Nindo Command",
    font=("Arial", 20),
    bg="#D7C0AE",
    fg="#1A1A1A",
    pady=25
)
main_page_header.pack()

main_page_frame = tk.Frame(main_page, bg="#D7C0AE")
main_page_frame.pack(pady=20)

login_button = tk.Button(
    main_page_frame,
    text="Login",
    width=20,
    height=3,
    font="Poppins",
    fg="beige",
    bg="#05ad05",
    bd=2,
    relief="groove",
    command=move_next_page
)
login_button.pack(side="left", padx=10)

registration_button = tk.Button(
    main_page_frame,
    text="Register",
    width=20,
    height=3,
    font="Poppins",
    fg="beige",
    bg="#05ad05",
    bd=2,
    relief="groove"
)
registration_button.pack(side="left", padx=10)

# ========== LOGIN PAGE CONTENT ==========
login_page_header = tk.Label(
    login_page,
    text="Login",
    font=("Arial", 20),
    bg="#D7C0AE",
    fg="#1A1A1A",
    pady=25
)
login_page_header.pack()

back_button = tk.Button(
    login_page,
    text="Back",
    width=20,
    height=3,
    font="Poppins",
    fg="beige",
    bg="#ad0505",
    bd=2,
    relief="groove",
    command=lambda: show_page(main_page)
)
back_button.pack(pady=20)


def show_page(page):
    global current_index
    for p in pages:
        p.pack_forget()
    page.pack(fill="both", expand=True)
    current_index = pages.index(page)


# ========== START WITH MAIN PAGE ==========
main_page.pack(fill="both", expand=True)

# ========== BACKGROUND IMAGE SETUP ==========
original_bg = Image.open("Images/KonohaMain.png")
aspect_ratio = original_bg.height / original_bg.width
max_height = 129

initial_width = 1000
initial_height = min(int(initial_width * aspect_ratio), max_height)
resized_img = original_bg.resize((initial_width, initial_height), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(resized_img)

my_canvas = tk.Canvas(window, bg="#D7C0AE", highlightthickness=0)
my_canvas.pack(fill="both", expand=True)
image_id = my_canvas.create_image(0, 0, anchor="nw", image=bg_image)


def resizer(event):
    global bg_image
    canvas_height = my_canvas.winfo_height()
    new_width = event.width
    scaled_height = int(original_bg.height * (new_width / original_bg.width))
    new_height = min(scaled_height, max_height)

    resized = original_bg.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized)
    my_canvas.itemconfig(image_id, image=bg_image)
    my_canvas.coords(image_id, 0, canvas_height - new_height)


def initial_layout():
    canvas_height = my_canvas.winfo_height()
    initial_scaled_height = min(int(original_bg.height * (initial_width / original_bg.width)), max_height)
    my_canvas.coords(image_id, 0, canvas_height - initial_scaled_height)


window.bind("<Configure>", resizer)
window.after_idle(initial_layout)

# Run the application
window.mainloop()
