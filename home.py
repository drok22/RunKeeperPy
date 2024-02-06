from datetime import datetime, timedelta
from tkinter import Button, E, N, S, Tk, W
from add_run import AddRunView
from add_shoes import AddShoesView
from constants import WINDOW_PAD_X, WINDOW_PAD_Y
from run import get_runs, Run
from shoes import get_shoes, Shoe
from weekly_running_frame_view import WeeklyRunningFrameView


class HomePage():
    def __init__(self) -> None:
        self.window: Tk = Tk()
        self.window.title("RunKeeper")
        self.window.config(padx=WINDOW_PAD_X, pady=WINDOW_PAD_Y, bg="black")

        self.add_run_button = Button(self.window, text="Add Shoes", highlightthickness=0, command=self.add_shoes)
        self.add_shoes_button = Button(self.window, text="Add Run", highlightthickness=0, command=self.add_run)

        self.runs: list[Run] = get_runs()
        self.shoes: list[Shoe] = get_shoes()

        #  Weekly charted workouts
        self.weekly_runs: list[Run] = self.get_weekly_running()
        self.weekly_running_view = WeeklyRunningFrameView(self.window, self.weekly_runs)

        self.grid_setup()
        self.window.mainloop()

    def add_shoes(self):
        '''Display the add new shoe window'''
        _ = AddShoesView(parent_window=self.window)

    def add_run(self):
        '''Display the add new run window'''
        _ = AddRunView(parent_window=self.window)

    def get_weekly_running(self) -> list[Run]:
        '''Return all the workouts completed during the current week's log'''
        weekly_runs: list[Run] = []
        date_format = '%m/%d/%Y, %H:%M:%S'
        today = datetime.today()
        week_begin_date = today - timedelta(days=today.weekday())
        # date without the time. probably a better way to do this.
        week_begin_date = datetime(month=week_begin_date.month,
                                   day=week_begin_date.day,
                                   year=week_begin_date.year)

        for run in self.runs:
            run_date = datetime.strptime(run.date, date_format)

            if run_date.year >= week_begin_date.year and run_date.month >= week_begin_date.month:
                difference = run_date - week_begin_date
                if difference.days >= 0 and difference.days < 7:
                    weekly_runs.append(run)

        return weekly_runs

    def grid_setup(self):
        '''display objects for this view on its tkinter grid'''
        self.weekly_running_view.grid(row=0, column=0, columnspan=2, sticky=N+E+S+W)

        self.add_run_button.grid(row=1, column=0, sticky=W)
        self.add_shoes_button.grid(row=1, column=1, sticky=W)
