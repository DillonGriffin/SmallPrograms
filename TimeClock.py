import datetime

# define a TimeClock class
class TimeClock:
    def __init__(self):
        # initialize a list to store the start and end times for each punch
        self.punches = []

    def punch_in(self):
        # create a new punch and set the start time to the current time
        punch = {"start": datetime.datetime.now()}
        self.punches.append(punch)

    def punch_out(self):
        # retrieve the latest punch and set the end time to the current time
        punch = self.punches[-1]
        punch["end"] = datetime.datetime.now()

    def get_total_time(self):
        # initialize the total time to 0
        total_time = datetime.timedelta(0)

        # loop over the punches and add the time worked for each one to the total time
        for punch in self.punches:
            start = punch["start"]
            end = punch["end"]
            time_worked = end - start
            total_time += time_worked

        return total_time

# create a new TimeClock object
clock = TimeClock()

# punch in
clock.punch_in()

# simulate some work being done
# (in a real implementation, this could be any code that needs to be timed)
import time
time.sleep(5)

# punch out
clock.punch_out()

# punch in again
clock.punch_in()

# simulate some more work being done
time.sleep(5)

# punch out
clock.punch_out()

# calculate and print the total time worked
total_time = clock.get_total_time()
print("Total time worked:", total_time)
