import tkinter as tk
from PIL import ImageTk, Image

class Home(tk.Frame):
    def __init__(self, parent, change_section):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.change_section = change_section
        self.label = tk.Label(self, text="Home")
        self.label.pack(fill="both", expand=1)

        # Background
        self.initial_bg = Image.open("home.PNG")
        self.bg = ImageTk.PhotoImage(self.initial_bg)
        self.bg_name = tk.Label(self, image=self.bg)
        self.bg_name.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.resize_image) 

        # Menubar
        self.menu_bar = tk.Menu(self.parent)
        self.parent.config(menu=self.menu_bar)
        
        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Menu", menu=self.file_menu)
        
        # Register menu item
        self.file_menu.add_command(label="Register", command=lambda: self.change_section(1))
        # Search menu item
        self.file_menu.add_command(label="Search Entry", command=lambda: self.change_section(3))

        #Resize image
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.initial_bg.resize((new_width, new_height), Image.NEAREST)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        self.bg_name.configure(image=self.bg_image)

    def present(self):
        self.pack()

    def hide(self):
        self.pack_forget()
