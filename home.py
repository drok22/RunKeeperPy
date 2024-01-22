from tkinter import Button, Tk, W
from add_run import AddRunView
from add_shoes import AddShoesView
from constants import WINDOW_PAD_X, WINDOW_PAD_Y


class HomePage():
    def __init__(self) -> None:
        self.window: Tk = Tk()
        self.window.title("RunKeeper")
        self.window.config(padx=WINDOW_PAD_X, pady=WINDOW_PAD_Y, bg="black")

        self.add_run_button = Button(self.window, text="Add Shoes", highlightthickness=0, command=self.add_shoes)
        self.add_shoes_button = Button(self.window, text="Add Run", highlightthickness=0, command=self.add_run)

        self.grid_setup()
        self.window.mainloop()

    def add_shoes(self):
        _ = AddShoesView(parent_window=self.window)

    def add_run(self):
        _ = AddRunView(parent_window=self.window)

    def grid_setup(self):
        self.add_run_button.grid(row=0, column=0, sticky=W)
        self.add_shoes_button.grid(row=0, column=1, sticky=W)
