import os
from tkinter import *
from tkinter.filedialog import askopenfilename

import Controller
import pathlib

class Menu:
    # it shows the label elements
    def __init__(self, screen):
        self.screen         = screen.root; # main window

        self.LabelTime      = None;
        self.timeChoose     = None;
        self.labelExplain   = None;
        self.chooseFile     = None;
        self.controllerWin  = None;
        self.startButton    = None;
        self.getPath        = None;

        self.draw();

    def draw(self):
        print("Drawing");
        self.startButton = Button(self.screen, text="Run", command=lambda:self.start());
        self.startButton.place(x=200,y=250);

        self.labelExplain = Label(self.screen, text="Path to file with words:", anchor=W);
        self.labelExplain.place(x=140,y=15);

        self.getPath = Entry(self.screen);
        self.getPath.place(x=140, y=40);

        self.chooseFile = Button(self.screen, text="Choose", command=lambda : self.chooseFileWin());
        self.chooseFile.place(x=335,y=38, width=60);

        self.LabelTime = Label(self.screen, text="frequency (in minutes):", anchor=W);
        self.LabelTime.place(x=140,y=92);

        self.timeChoose = Spinbox(self.screen, from_=1, to=45, font="Arial 15 bold", buttonbackground='white',
                                  width=5, increment=1)
        self.timeChoose.place(x=297, y=90)


    def chooseFileWin(self):
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        # with open(filepath, mode="r", encoding="utf-8") as input_file:
        #     text = input_file.read()

        # self.getPath.config(text=filepath);#state=DISABLED)
        self.getPath.insert(0, filepath)
        print("the chosen file is: ", filepath);
        print(self.timeChoose.get());


    def start(self):

        print("Start testing");

        time = self.timeChoose.get();
        path = self.getPath.get()

        print(time);
        print(path);

        if not path:
            print("No file selected");
            # self.getPath.insert(0, "/");
            return;

        if pathlib.Path(path).exists():
            try:

                self.screen.withdraw();

                self.controllerWin = Controller.Controller(path, time, handler=self.stop);
                self.controllerWin.run();

            except Exception as e:
                print(e);
        else:
            print("the file ain't existed");
            self.getPath.delete(0, END);
            # self.getPath.insert(0, "File not found");


    def stop(self):
        print("Stop");
        self.controllerWin.exit();
        self.screen.deiconify();