
import tkinter as tk
import sys


class MainWindow:
    def __init__(self, master=None):
        self.root = None
        self.master = master
        self.bg = 0;
        self.screen_width = 0;
        self.screen_height = 0;

    def setup(self):
        self.root = tk.Tk();
        self.root.title("Mnemo")
        self.root.minsize(400, 300)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # self.bg  = tk  .PhotoI mage(fi  le="./images/background.png");
        (self.root.geometry
         (f"400x300+{int(int(self.screen_width) / int(3))}+{int(int(self.screen_height) / int(3))}"));
        self.root.maxsize(400, 300)
        self.root.resizable(False, False)


    def show(self):
        self.root.mainloop()

