from json import dump, load
from json.decoder import JSONDecodeError
from tkinter import Button, Entry, Label, Tk, Toplevel, W
from constants import BACKGROUND_COLOR, SAVED_SHOES_PATH, TEXT_COLOR, WINDOW_PAD_X, WINDOW_PAD_Y


class AddShoesView():
    def __init__(self, parent_window: Tk) -> None:
        self.window: Toplevel = Toplevel(parent_window)
        self.window.title("Add Shoe Data")
        self.window.config(padx=WINDOW_PAD_X, pady=WINDOW_PAD_Y, bg="black")

        self.brand_label = Label(self.window, text="Brand", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.name_label = Label(self.window, text="Name", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.run_total_label = Label(self.window, text="Total Runs", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.miles_total_label = Label(self.window, text="Total Miles", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.color_label = Label(self.window, text="Color", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

        self.brand_entry = Entry(self.window, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.name_entry = Entry(self.window, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.run_total_entry = Entry(self.window, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.miles_total_entry = Entry(self.window, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.color_entry = Entry(self.window, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

        self.save_button = Button(self.window, text="Save", highlightthickness=0, command=self.save_shoes)

        self.grid_setup()
        self.window.mainloop()

    def init_entry(self):
        pass

    def save_shoes(self):
        '''Save shoe data to JSON file'''

        name = self.name_entry.get()
        shoe_data: dict = {name: {"brand": self.brand_entry.get(),
                                  "name": self.name_entry.get(),
                                  "run_total": self.run_total_entry.get(),
                                  "miles_total": self.miles_total_entry.get(),
                                  "color": self.color_entry.get()}}

        try:
            with open(SAVED_SHOES_PATH, "r") as shoe_file:
                all_data = load(shoe_file)

        except FileNotFoundError:
            with open(SAVED_SHOES_PATH, "w") as shoe_file:
                dump(shoe_data, shoe_file, indent=4)

        except JSONDecodeError:
            # this might mean we're going to overwrite the file. bad idea?
            with open(SAVED_SHOES_PATH, "w") as shoe_file:
                dump(shoe_data, shoe_file, indent=4)

        else:
            all_data.update(shoe_data)

            with open(SAVED_SHOES_PATH, "w") as shoe_file:
                dump(all_data, shoe_file, indent=4)

        finally:
            pass  # close window, pass back errors, etc.

    def grid_setup(self):

        self.brand_label.grid(row=0, column=0, sticky=W)
        self.name_label.grid(row=1, column=0, sticky=W)
        self.run_total_label.grid(row=2, column=0, sticky=W)
        self.miles_total_label.grid(row=3, column=0, sticky=W)
        self.color_label.grid(row=4, column=0, sticky=W)

        self.brand_entry.grid(row=0, column=1, sticky=W)
        self.name_entry.grid(row=1, column=1, sticky=W)
        self.run_total_entry.grid(row=2, column=1, sticky=W)
        self.miles_total_entry.grid(row=3, column=1, sticky=W)
        self.color_entry.grid(row=4, column=1, sticky=W)

        self.save_button.grid(row=5, column=1, sticky=W)
