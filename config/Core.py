
import tkinter
from tkinter import font
import threading


class SingletonMeta(type,tkinter.Tk):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CoreTkinter(metaclass=SingletonMeta):

    def __init__(self, mode:bool):
        self.root_window = tkinter.Tk();
        self.custom_font = font.Font(family="italic",weight="normal", size=38); # 2560 × 1600
        self.mode = mode;

    def set_style(self):
        self.root_window.title("Nemo");
        self.root_window.overrideredirect(self.mode);
        self.root_window.configure(background="black");
        self.root_window.attributes("-topmost", True);

    def __exit(self):
        
        return 0;