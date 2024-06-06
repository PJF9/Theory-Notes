from time import time, sleep
from subprocess import run


class Exist_System:
    def __init__(self, mode, secs, mins=0, hours=0):
        try:
            int(secs)
            int(mins)
            int(hours)
        except ValueError:
            print("Invalid_args")
            exit()

        self.mode = mode if (mode == 'r') or (mode == 's') or (mode == 'l') else 'l'
        self.secs = secs
        self.mins = mins
        self.hours = hours

    def __get_total_seconds(self):
        return self.secs + self.mins*60 + self.hours*3_600

    def go(self):
        start = time()
        while int(time() - start) <= self.__get_total_seconds():
            sleep(1)

        run(f"shutdown /{self.mode}")
