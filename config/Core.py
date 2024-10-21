import tkinter
from tkinter import font

class SingletonMeta(type,tkinter.Tk):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class CoreTkinter(metaclass=SingletonMeta):
    def __init__(self):
        self.root_window = tkinter.Tk();
        self.custom_font = font.Font(family="italic", size=40,weight="normal");

    def set_appearence(self):
        self.root_window.title("Nemo");
        self.root_window.overrideredirect(1);
        # self.root_window.configure(background="black");
        self.root_window.attributes("-topmost", True);
