import tkinter as tk
from PIL import Image, ImageTk

# Create main window
window = tk.Tk()
window.title("Nindo Command")
window.configure(bg="#D7C0AE")
window.iconbitmap("C:/Users/Mattie/PycharmProjects/TkinterTest/Images/Icons/Cubed.ico")
window.minsize(width=1250, height=700)
window.maxsize(width=2000, height=1000)

# Top label
main_header = tk.Label(
    text="Nindo Command",
    font=("Arial", 20),
    bg="#D7C0AE",
    fg="#1A1A1A",
    pady = 25
)
main_header.pack()

main_button = tk.Button(
    window,
    text = "PlACEHOLDER ENTRY",
    width = 20,
    height = 3,
    font = "Poppins",
    fg = "beige",
    bg = "#05ad05",
    bd = "2",
    relief = "groove"
)
main_button.pack(side = "top", pady=20, padx=0)

# Canvas for dynamic background image
my_canvas = tk.Canvas(window, bg="#D7C0AE", highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Load original background image
original_bg = Image.open("Images/KonohaMain.png")
aspect_ratio = original_bg.height / original_bg.width
max_height = 129

# Placeholder resized image
initial_width = 1000
initial_height = min(int(initial_width * aspect_ratio), max_height)
resized_img = original_bg.resize((initial_width, initial_height), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(resized_img)
image_id = my_canvas.create_image(0, 0, anchor="nw", image=bg_image)

# Resize handler to keep image pinned and properly scaled
def resizer(event):
    global bg_image
    canvas_height = my_canvas.winfo_height()
    new_width = event.width
    scaled_height = int(original_bg.height * (new_width / original_bg.width))
    new_height = min(scaled_height, max_height)

    # Resize and update image
    resized = original_bg.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized)
    my_canvas.itemconfig(image_id, image=bg_image)

    # Reposition to always pin bottom-left
    my_canvas.coords(image_id, 0, canvas_height - new_height)

# Ensure proper initial placement
def initial_layout():
    canvas_height = my_canvas.winfo_height()
    initial_scaled_height = min(int(original_bg.height * (initial_width / original_bg.width)), max_height)
    my_canvas.coords(image_id, 0, canvas_height - initial_scaled_height)

window.after_idle(initial_layout)


# Bind resize event
window.bind("<Configure>", resizer)


# Run the application
window.mainloop()
