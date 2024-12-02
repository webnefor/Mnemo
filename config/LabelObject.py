
import random
import tkinter as tk


def format_time(x) -> int:
    return int(x) * 60 * 1000;


class LabelObject:
    def __init__(self, win, word, pronunciation, example, translation, time):
        
        self.down_label         = None;        
        self.example_text       = None;

        self.top_label          = None;
        self.word_text          = None;
      
        self.req_height         = None;
        self.req_width          = None;
    
        self.random_value       = 0;
        self.turn:bool          = True;

        self.word               = word;
        self.pronunciation      = pronunciation;
        
        self.example            = example;
        self.translation        = translation;
                
        self.used_element       = [];


        self.win                = win.root_window;
        self.custom_font        = win.custom_font;

        self.win.wm_minsize(width=200, height=70);
        self.time               = time;

    def create(self):

        self.top_label          = tk.Label(self.win, text=self.word_text,
                                    font=self.custom_font, background="black", foreground="white");

        self.down_label         = tk.Label(self.win, text=self.example_text,
                                    font=self.custom_font,background="black", foreground="white");

        self.top_label.pack(pady=6);
        self.down_label.pack(pady=10);

        self.win.geometry(f"+{1}+{0}");

        self.update();

    def disappear(self):
        self.random_value         = self.get_random_number(len(self.word));

        self.win.withdraw();
        self.turn = True;
        self.win.after(format_time(self.time), self.update);


    def update(self) -> None:
        
        self.top_label.config (text=("➜ " + self.word[self.random_value] + " ")
            if self.turn else ("📚 " + self.example[self.random_value]) + " ");

        self.down_label.config(text=("➜ " +self.pronunciation[self.random_value] + " ")
            if self.turn else (self.translation[self.random_value]) + " ");

        if self.turn:
            self.win.after(20000, self.update);
            self.win.update_idletasks();
            self.win.deiconify();
            self.turn = False;
        else:
            self.win.after(14000, self.disappear);


    def get_random_number(self, range_) -> int:
        while 1:
            # The func will generate a random num
            x = random.randrange(range_);

            if x not in self.used_element:
                self.used_element.append(x);
                return x;

            if len(self.used_element) >= range_:
                self.used_element.clear();

            else:
                continue;
