import random
import sys
import tkinter
from tkinter import font, Button, Canvas
import Menu


class SingletonMeta(type,tkinter.Tk):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("Creating new instance");
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Engine(metaclass=SingletonMeta):
    def __init__(self, mode : bool = 0):

        self.screen_height  = 0;
        self.screen_width   = 0;

        self.root           = tkinter.Tk();
        self.custom_font    = font.Font(family="italic", weight="normal", size=45);  # 2560 × 1600
        self.canvas         = Canvas(self.root, width=400, height=300);

        self.mode           = mode;

        self.label          = None
        self.font_text      = None;
        self.text_canvas    = None;

        self.colors         = []; # ["red","blue", "violet", "yellow","pink"]
        self.num            = 0;
        self.index          = 0;

        # Gradient color shades
        self.red            = (0, 0, 188);
        self.black          = (188, 0, 0);

        self.showHello      = [
            "Ciao 🇮🇹", "你好 🇨🇳", "こんにちは 🇯🇵",
            "नमस्ते 🇮🇳", "Hello 🇬🇧", "שלום 🇮🇱",
            "Привет 🇷🇺", "Bonjour 🇫🇷", "🇸🇦 مرحبا"
        ];
        # setting
        self.x              = 55;
        self.y              = 10;

        self.set_style();
        self.set_settings();
        self.backgroundAnimate();

    def set_style(self):
        self.root.title("Mnemo");
        self.root.overrideredirect(self.mode);
        # self.root.configure(background="black");
        self.root.attributes("-topmost", True);


    def backgroundAnimate(self):
        if self.mode == 0:
            self.generate_gradient(self.red,self.black, 130);
            self.mode = 1
        else:
            self.generate_gradient(self.black,self.red, 130);
            self.mode = 0;

        self.canvas.delete("all")  # Clear canvas
        for i in range(0, 500, 20):
            self.font_text = font.Font(family="Monaco", weight="normal", size=25-len(str(self.showHello[self.num])));
            color = self.colors[(self.index + i // 20) % len(self.colors)]
            self.canvas.create_rectangle(0, i, 145, i+20,fill=color,width=0, outline="");

            self.canvas.create_line(0, i, 145, 20, fill=color);
            # self.canvas.create_(0, 1, self.canvas.winfo_screenheight(), 20, fill="black", width=2)

            self.canvas.create_text(self.x + 15, self.y + 20, text=self.showHello[self.num], fill="white", font=self.font_text);
            self.canvas.create_text(self.x+15, 30, text="Mnemo", fill=color[::2], font=self.font_text);

        self.y += 2;

        if self.y > 310:
            self.y = 10;

            if (x := random.randrange(0, len(self.showHello))) != self.num:
                self.num = x;

        self.index = (self.index + 1) % len(self.colors)

        self.root.after(50, self.backgroundAnimate)

    def generate_gradient(self,start_color, end_color, steps):
        # sel = []
        for i in range(steps):
            ratio = i / (steps - 1)
            r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
            g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
            b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
            self.colors.append(f'#{r:02X}{g:02X}{b:02X}')

    def set_settings(self):
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.canvas.place(x=-5, y=-5, width=145)#(row=0, column=0, sticky=tkinter.NSEW);

        # self.label = tkinter.Label(self.root, text="Mnemo", font=self.font_text);
        # self.label.grid(row=0, column=0, sticky=tkinter.NSEW);

        # https: // duckduckgo.com /?q = crayons & t = osx relwidth=50, relheight=500, relx=300, rely=100
        self.root.geometry(f"400x300+{int(int(self.screen_width) / int(3))}+{int(int(self.screen_height) / int(3))}");
        self.root.resizable(width=False, height=False);

        self.root.maxsize(400, 300)


    def start(self):
        self.root.mainloop();

def Run():
    Eng = Engine();
    Menu.Menu(Eng); #set additional widgets

    Eng.start();


