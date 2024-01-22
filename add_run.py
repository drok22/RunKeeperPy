from datetime import datetime
from json import dump, load
from json.decoder import JSONDecodeError
from tkinter import Button, Entry, Label, Toplevel, W
from constants import BACKGROUND_COLOR, SAVED_RUNS_PATH, TEXT_COLOR, WINDOW_PAD_X, WINDOW_PAD_Y


class AddRunView():
    def __init__(self, parent_window) -> None:

        self.window: Toplevel = Toplevel(parent_window)
        self.window.title("Add Run Data")
        self.window.config(padx=WINDOW_PAD_X, pady=WINDOW_PAD_Y, bg="black")

        self.date_label = Label(self.window, text="Date", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.distance_label = Label(self.window, text="Distance", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.duration_label = Label(self.window, text="Duration", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.type_label = Label(self.window, text="Run Type", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.hr_label = Label(self.window, text="Avg. HR", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

        self.date_entry = Entry(self.window, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.distance_entry = Entry(self.window, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.duration_entry = Entry(self.window, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.type_entry = Entry(self.window, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.hr_entry = Entry(self.window, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

        self.save_button = Button(self.window, text="Save", highlightthickness=0, command=self.save_run)

        self.grid_setup()
        self.init_entry()
        self.window.mainloop()

    def init_entry(self):
        date_today = datetime.now()
        date_today = date_today.strftime("%m/%d/%Y, %H:%M:%S")
        self.date_entry.insert(0, date_today)

    def save_run(self):
        '''Save run data to JSON file'''

        name = self.date_entry.get()
        run_data: dict = {name: {"date": self.date_entry.get(),
                                 "distance": self.distance_entry.get(),
                                 "duration": self.duration_entry.get(),
                                 "type": self.type_entry.get(),
                                 "avg_hr": self.hr_entry.get()}}

        try:
            with open(SAVED_RUNS_PATH, "r") as run_file:
                all_data = load(run_file)

        except FileNotFoundError:
            with open(SAVED_RUNS_PATH, "w") as run_file:
                dump(run_data, run_file, indent=4)

        except JSONDecodeError:
            # this might mean we're going to overwrite the file. bad idea?
            with open(SAVED_RUNS_PATH, "w") as run_file:
                dump(run_data, run_file, indent=4)

        else:
            all_data.update(run_data)

            with open(SAVED_RUNS_PATH, "w") as run_file:
                dump(all_data, run_file, indent=4)

        finally:
            pass  # close window, pass back errors, etc.

    def grid_setup(self):

        self.date_label.grid(row=0, column=0, sticky=W)
        self.distance_label.grid(row=1, column=0, sticky=W)
        self.duration_label.grid(row=2, column=0, sticky=W)
        self.type_label.grid(row=3, column=0, sticky=W)
        self.hr_label.grid(row=4, column=0)

        self.date_entry.grid(row=0, column=1, sticky=W)
        self.distance_entry.grid(row=1, column=1, sticky=W)
        self.duration_entry.grid(row=2, column=1, sticky=W)
        self.type_entry.grid(row=3, column=1, sticky=W)
        self.hr_entry.grid(row=4, column=1, sticky=W)

        self.save_button.grid(row=5, column=1, sticky=W)
