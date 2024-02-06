from tkinter import Frame, Label
from run import Run


class WeeklyRunningFrameView(Frame):
    def __init__(self, master, weekly_runs: list[Run]) -> None:
        super().__init__(master, bg='black')

        self.weekly_runs: list[Run] = weekly_runs

        self.weekly_label = Label(self, fg='white', bg='black', text='Weekly Running:')

        self.date_label = Label(self, fg='white', bg='black', text="date")
        self.distance_label = Label(self, fg='white', bg='black', text="distance")
        self.duration_label = Label(self, fg='white', bg='black', text="duration")
        self.pace_label = Label(self, fg='white', bg='black', text="pace")
        self.notes_label = Label(self, fg='white', bg='black', text='notes')
        self.avg_bpm_label = Label(self, fg='white', bg='black', text="avg bpm")

        self.num_runs_label = Label(self, fg='white', bg='black', text="runs")
        self.total_distance_label = Label(self, fg='white', bg='black', text="total dist")
        self.total_time_label = Label(self, fg='white', bg='black', text="time")
        self.total_pace_label = Label(self, fg='white', bg='black', text="pace")
        self.avg_distance_label = Label(self, fg='white', bg='black', text="avg mi/run")
        self.total_bpm_label = Label(self, fg='white', bg='black', text="avg bpm")

        self.grid_setup()

    def grid_setup(self):
        row = 0
        column = 0

        self.weekly_label.grid(row=0, column=0)

        row = 1

        self.date_label.grid(row=row, column=column)
        self.distance_label.grid(row=row, column=column+1)
        self.duration_label.grid(row=row, column=column+2)
        self.pace_label.grid(row=row, column=column+3)
        self.notes_label.grid(row=row, column=column+4)
        self.avg_bpm_label.grid(row=row, column=column+5)

        row = 2

        for run in self.weekly_runs:
            date_label = Label(self, fg='white', bg='black', text=run.date)
            distance_label = Label(self, fg='white', bg='black', text=run.distance)
            duration_label = Label(self, fg='white', bg='black', text=run.duration)
            pace_label = Label(self, fg='white', bg='black', text='CalculateMe')
            notes_label = Label(self, fg='white', bg='black', text=run.type)
            avg_bpm_label = Label(self, fg='white', bg='black', text=run.avg_HR)

            date_label.grid(row=row, column=column)
            distance_label.grid(row=row, column=column+1)
            duration_label.grid(row=row, column=column+2)
            pace_label.grid(row=row, column=column+3)
            notes_label.grid(row=row, column=column+4)
            avg_bpm_label.grid(row=row, column=column+5)

            row = row + 1
        # ok, now maybe print a divider?

        self.num_runs_label.grid(row=row, column=column)
        self.total_distance_label.grid(row=row, column=column+1)
        self.total_time_label.grid(row=row, column=column+2)
        self.total_pace_label.grid(row=row, column=column+3)
        self.avg_distance_label.grid(row=row, column=column+4)
        self.total_bpm_label.grid(row=row, column=column+5)