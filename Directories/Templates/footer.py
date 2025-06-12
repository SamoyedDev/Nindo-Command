from PIL import Image, ImageTk

def add_dynamic_footer(canvas, image_path, max_height=129):
    original_bg = Image.open(image_path)
    aspect_ratio = original_bg.height / original_bg.width

    def place_image():
        canvas_width = canvas.winfo_width()
        if canvas_width <= 1:  # Canvas not ready yet
            canvas.after(10, place_image)
            return

        initial_width = canvas_width
        initial_height = min(int(initial_width * aspect_ratio), max_height)

        if initial_width <= 0 or initial_height <= 0:
            initial_width = initial_height = 1

        resized_img = original_bg.resize((initial_width, initial_height), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(resized_img)
        image_id = canvas.create_image(0, canvas.winfo_height() - initial_height, anchor="nw", image=bg_image)

        # Store reference so image doesn't get garbage collected
        canvas._bg_image = bg_image

        def resize(event):
            new_width = event.width
            scaled_height = int(original_bg.height * (new_width / original_bg.width))
            new_height = min(scaled_height, max_height)

            if new_width <= 0 or new_height <= 0:
                return

            resized = original_bg.resize((new_width, new_height), Image.Resampling.LANCZOS)
            canvas._bg_image = ImageTk.PhotoImage(resized)
            canvas.itemconfig(image_id, image=canvas._bg_image)
            canvas.coords(image_id, 0, event.height - new_height)

        canvas.bind("<Configure>", resize)

    canvas.after_idle(place_image)
