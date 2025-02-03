
import random
import tkinter as tk
from tkinter import font

from GetFileWords import init, Words, Pronunciation, Examples, Translate


class ShowingWords:
    def __init__(self, path, time):

        self.path = path
        self.time = time
        print(self.path, "   " , self.time)

        init(self.path);

        self.root           = None;
        self.label_top      = None;
        self.label_bottom   = None;
        self.custom_font    = None;

        self.regime         = None;
        self.rand_value     = None;
        self.after_id       = None;
        self.used_elements  =   [];

        self.archive = \
        { # key : value
            "words"         : Words,
            "translate"     : Translate,
            "pronunciation" : Pronunciation,
            "examples"      : Examples,
        };

    def make(self):
        self.root = tk.Tk()
        self.root.title("Mnemo")
        self.custom_font = font.Font(family="italic", weight="normal", size=150)
        self.root.resizable(False, False)
        self.root.wm_minsize(width=200, height=70)

    def create_label(self):
        self.label_top = tk.Label(self.root, font=self.custom_font, text="Hello, ", background="black", foreground="white")
        self.label_bottom = tk.Label(self.root, font=self.custom_font, text="there!", background="black", foreground="white")

        self.label_top.pack(pady=6)
        self.label_bottom.pack(pady=10)

        self.root.geometry(f"+{1}+{0}")

    def disappear(self):
        self.rand_value = self.get_random_number(len(self.archive["words"]))
        print(self.rand_value)
        self.root.withdraw()
        self.regime = True
        self.after_id = self.root.after(1000, self.update_label)

    def update_label(self) -> None:
        print("update")

        self.label_top.config(font=self.custom_font,text=("➜ " + self.archive["words"][self.rand_value] + " ")
                               if self.regime else
                               ("📚 " + self.archive["examples"][0]) + " ")

        self.label_bottom.config(font=self.custom_font,text=("➜ " + self.archive["pronunciation"][0] + " ")
                                  if self.regime else
                                  (self.archive["translate"][0]) + " ")

        if self.regime:
            print("if")
            self.after_id = self.root.after(1000, self.update_label)
            self.root.deiconify()
            self.root.update_idletasks()
            self.regime = False
        else:
            self.after_id = self.root.after(1000, self.disappear)
            print("else")

    def get_random_number(self, _len) -> int:
        while True:
            x = random.randrange(_len)

            if x not in self.used_elements:
                self.used_elements.append(x)
                return x

            if len(self.used_elements) >= _len:
                self.used_elements.clear()

    def exit(self) -> int:
        print("ShowingWords.exit")
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)

        self.root.withdraw()
        self.root.destroy()

        del self;

        return 0;

    def run(self):
        self.create_label();
        self.update_label();
        self.root.mainloop()
