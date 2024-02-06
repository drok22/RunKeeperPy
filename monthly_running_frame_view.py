from tkinter import Frame, Label


class MonthlyRunningFrameView(Frame):
    def __init__(self, master) -> None:
        super().__init__(master, bg='black')
        self.hello_world_label = Label(self, text="Hello, World. I am in the Monthly Running Frame", fg='white')

        self.grid_setup()

    def grid_setup(self):
        self.hello_world_label.grid(column=0, row=0)
