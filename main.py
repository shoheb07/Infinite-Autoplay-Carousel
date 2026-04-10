import tkinter as tk
from PIL import Image, ImageTk

class Carousel:
    def __init__(self, root, image_paths, delay=2000):
        self.root = root
        self.image_paths = image_paths
        self.delay = delay  # time in ms
        self.index = 0

        # Load images
        self.images = [ImageTk.PhotoImage(Image.open(img).resize((500, 300))) 
                       for img in image_paths]

        # Label to display images
        self.label = tk.Label(root)
        self.label.pack()

        # Start carousel
        self.show_image()

    def show_image(self):
        self.label.config(image=self.images[self.index])
        self.index = (self.index + 1) % len(self.images)  # infinite loop
        self.root.after(self.delay, self.show_image)


# Main Window
root = tk.Tk()
root.title("Infinite Autoplay Carousel")
root.geometry("520x320")

# Add your image paths here
image_list = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
    "image4.jpg"
]

carousel = Carousel(root, image_list, delay=2000)

root.mainloop()
