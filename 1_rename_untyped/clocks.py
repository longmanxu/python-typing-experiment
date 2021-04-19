# various "clock" classes:

class Clock:
    def __init__(self, time):
        self.time = time


class Timer:
    def __init__(self):
        self.time_left = 0.0


class Stopwatch:
    def __init__(self):
        self.time = 0.0


# various classes that use those "clocks":

class Watch:
    def __init__(self):
        self.clock = self.__make_clock()

    @staticmethod
    def __make_clock():
        return Clock(0.0)


class Microwave:
    def __init__(self):
        self.timer = self.__make_timer()

    @staticmethod
    def __make_timer():
        return Timer()


class Referee:
    def __init__(self):
        self.stopwatch = self.__make_stopwatch()

    @staticmethod
    def __make_stopwatch():
        return Stopwatch()


# some functions that use those classes:

def get_watch_time(w):
    return w.clock.time


def set_watch_time(w, t):
    w.clock.time = t


def get_microwave_time(m):
    return m.timer.time_left


def set_microwave_time(m, t):
    m.timer.time_left = t


def get_referee_time(r):
    return r.stopwatch.time


def set_referee_time(r, t):
    r.stopwatch.time = t
