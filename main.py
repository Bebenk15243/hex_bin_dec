from transformator import *
from tkinter import *

window = Tk()


class setup:
    def __init__(self):
        self.title = "bin to hex to dec"
        self.config = "Gray"
        self.setupconfig = "Whitesmoke"
        self.font = ("courier new", 20)
        self.text = "convert to..."
        self.run()

    def run(self):
        print("run")
        window.title(self.title)
        window.config(bg=self.config)
        window.maxsize(1000, 300)
        window.minsize(1000, 300)
        self.window_setup()

    def window_setup(self):

        confirmButton = Button(window, bg=self.setupconfig, text=self.text, font=self.font, command=self.inputed)

        self.entry = Entry(window, bg=self.setupconfig, font=self.font)
        self.output1 = Entry(window, bg=self.setupconfig, font=self.font)
        self.output2 = Entry(window, bg=self.setupconfig, font=self.font)

        self.entry.pack(side=TOP, fill=BOTH, expand=False)
        confirmButton.pack(side=BOTTOM, fill=BOTH, expand=True)
        self.output1.pack(side=LEFT, fill=BOTH, expand=True)
        self.output2.pack(side=RIGHT, fill=BOTH, expand=True)

        self.win_update()

    def inputed(self):
        if self.entry.get()[0] != "0":
            dec(self)
        else:
            if self.entry.get()[1] == "x":
                Hex(self)
            elif self.entry.get()[1] == "b":
                Bin(self)
            else:
                self.ERROR("SYNTAX ERROR", "")

    def win_update(self):
        print("mainloop")
        window.mainloop()

    def _input(self):
        return self.entry.get()

    def insert(self, output, output2):
        self.output1.delete(0, END)
        self.output1.insert(0, str(output))

        self.output2.delete(0, END)
        self.output2.insert(0, str(output2))

    def ERROR(self, error, error2):
        self.insert(error, error2)


if __name__ == '__main__':
    setup()
