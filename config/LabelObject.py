
from tkinter.ttk import Label, Style
import random

class LabelObject:
    def __init__(self, win, word, pronunciation, example, translation):

        self.labels                     = None;
        self.labels_text                = None;
        self.label                      = None;
        self.label_text                 = None;
        self.req_height                 = None;
        self.req_width                  = None;
        self.win                        = win.root_window;
        self.custom_font                = win.custom_font;

        self.random_value               = 0;
        self.turn:bool                  = True;


        self.word                       = word;
        self.pronunciation              = pronunciation;
        self.example                    = example;
        self.translation                = translation;

        self.used_element               = [];

        self.win.wm_minsize(width=200, height=70);
        self.win.title("Mnemo")

        self.style = Style()
        self.style.configure("Red.TLabel", background="white")  # Custom style for red background

    def create(self):

        self.label          = Label(self.win, text=self.label_text,
                                    font=self.custom_font,style="Red.TLabel");

        self.labels         = Label(self.win, text=self.labels_text,
                                    font=self.custom_font, style="Red.TLabel");

        self.label.pack(pady=6);
        self.labels.pack(pady=10);

        self.win.geometry(f"+{1}+{0}");

        self.update();

    def mintosec(self,x) -> int:
        return int(x) * 60;

    def disappear(self):
        self.random_value         = self.get_random_number(len(self.word));

        self.win.withdraw();
        self.turn = True;
        self.win.after(self.mintosec(1), self.update);


    def update(self) -> int:


        self.label.config (text=("✍🏼 "+self.word[self.random_value] + " ")
            if self.turn else ("📚 " + self.translation[self.random_value]) + " ");

        self.labels.config(text=("➜ " +self.example[self.random_value] + " ")
            if self.turn else ("️🗣 " + self.pronunciation[self.random_value]) + " ");

        if self.turn:
            self.win.after(4000, self.update)
            self.win.update_idletasks();
            self.win.deiconify();
            self.turn = False;
        else:
            self.win.after(8000, self.disappear);


    def get_random_number(self, range_) -> int:
        while 1:
            # The func will generate a random num
            x = random.randrange(range_);

            if x not in self.used_element:
                self.used_element.append(x)
                return x

            if len(self.used_element) >= range_:
                self.used_element.clear()

            else:
                continue
