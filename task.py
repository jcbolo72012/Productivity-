import time
class Task:
    def __init__(self, units, goal, unit, breakfreq, breaklength, timegoal):
        self.units = units
        self.unit = unit
        self.goal = goal
        self.complete = 0
        self.time = 0.0
        self.break_frequency = breakfreq
        self.break_length = breaklength
        if self.unit == 'm':
            self.time_goal = time.time() + timegoal*60
        elif self.unit == 'h':
            self.time_goal = time.time() + timegoal*3600
        else:
            self.time_goal = time.time() + timegoal
    def __repr__(self):
        unitrepr = "seconds"
        if self.unit == 'm':
            unitrepr = 'minutes'
        elif self.unit == 'h':
            unitrepr = 'hours'
        else:
            pass
        s = self.units + " complete so far: " + str(self.complete) + "\n"
        s += self.units + " left to go: " + str(self.amt_left()) + " (goal: " + str(self.goal) + ")"
        tpu = self.format_time(self.time_per_unit())
        s += "\naverage time per " + self.units + ": " + str(tpu) + " " + unitrepr
        s += "\ntime left until goal reached: " + str(self.format_time(self.time_to_reach_goal())) + " " + unitrepr + "\n"
        c = self.check_time()
        s += c
        return s


    def update_time(self, time):
        self.complete += 1
        self.time += time


    def time_per_unit(self):
        if self.time!= 0.0:
            return self.time / self.complete
        else:
            return 0.0


    def amt_left(self):
        return self.goal - self.complete


    def time_to_reach_goal(self):
        return self.time_per_unit() * self.amt_left()


    def format_time(self, time):
        if self.unit == 'h':
            return time / 3600
        elif self.unit == 'm':
            return time / 60
        else:
            return time

    def check_time(self):
        diff = self.time_goal - (time.time() + self.time_to_reach_goal())
        if diff >= 0:
            return "you'll finish with: " + str(self.format_time(diff)) + " " + self.unit + " to spare!"
        else:
            speedup = abs(diff)/(self.goal - self.complete)
            return "you'll need to shave " + str(self.format_time(speedup)) + " " + self.unit + " off each unit in order to make your goal!"



