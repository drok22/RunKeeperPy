from constants import SAVED_RUNS_PATH
from json import load


class Run():
    def __init__(self, run_data: dict = {}):
        self.date = run_data.get('date', None)
        self.distance = run_data.get('distance', 0)
        self.duration = run_data.get('duration', 0)
        self.avg_HR = run_data.get('avg_HR', 0)
        self.type = run_data.get('type', None)


def get_runs() -> list:
    '''downloads all stored run data and returns as a list of Run objects'''
    runs = []

    with open(SAVED_RUNS_PATH, 'r') as run_file:
        run_data = load(run_file)

    for key in run_data:
        run = Run(run_data[key])
        runs.append(run)

    return runs
