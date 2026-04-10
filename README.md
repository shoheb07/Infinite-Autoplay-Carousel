# Infinite-Autoplay-Carousel
Creating an infinite autoplay carousel in Python is typically done using a GUI framework like Tkinter (for desktop apps). Below is a clean, working example with autoplay + looping.

📌 Project Overview
This project implements an infinite autoplay image carousel using Python’s Tkinter GUI library. The carousel automatically cycles through images at a fixed interval and loops back to the beginning, creating a continuous slideshow effect.

🎯 Features
Infinite looping carousel
Autoplay with adjustable delay
Image resizing for uniform display
Lightweight GUI using Tkinter
Easy to customize and extend
🛠️ Technologies Used
Python 3.x
Tkinter (built-in GUI library)
Pillow (for image processing)

📦 Installation
Clone or download this project
Install required dependency:
Bash
pip install pillow

📂 Project Structure

carousel-project/
│
├── main.py
├── image1.jpg
├── image2.jpg
├── image3.jpg
├── image4.jpg
└── README.md

▶️ Usage
Place your images in the project folder
Update the image paths in the script:
Python
image_list = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
    "image4.jpg"
]
Run the program:
Bash
python main.py

⚙️ How It Works
Images are loaded into a list
The index variable tracks the current image
After a fixed delay, the index updates
Modulo operation ensures infinite looping:
Python
self.index = (self.index + 1) % len(self.images)
after() function schedules automatic updates
🔧 Customization
You can modify:
⏱️ Delay time:
Python
delay=2000  # milliseconds

🖼️ Image size:
Python
resize((500, 300))

🚀 Future Improvements
Add Next/Previous buttons
Pause/Resume functionality
Smooth transition animations (fade/slide)
Load images dynamically from folder
Add captions or indicators

❗ Troubleshooting
Images not showing → Check file paths
Module not found (PIL) → Run pip install pillow
Window not opening → Ensure Python is properly installed

📜 License
This project is open-source and free to use for learning purposes.

🙌 Contribution
Contributions, suggestions, and improvements are welcome.
