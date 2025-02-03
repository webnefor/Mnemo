
import ShowingWords


class Controller(object):
    def __init__(self,path, time, handler=None):
        self.destroy = handler; # exit handler
        self.path = path;
        self.time = time;
        self.showingWords = ShowingWords.ShowingWords(self.path, self.time);

    def run(self):
        print(self.path, "=", self.time);
        self.showingWords.make();
        self.showingWords.root.protocol("WM_DELETE_WINDOW", self.destroy);
        self.showingWords.run()

    def exit(self):
        self.showingWords.exit();
        return 0x0;
