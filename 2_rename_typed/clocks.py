# various "clock" classes:

class Clock:
    def __init__(self, time: float) -> None:
        self.time = time


class Timer:
    def __init__(self) -> None:
        self.time_left: float = 0


class Stopwatch:
    def __init__(self) -> None:
        self.time: float = 0


# various classes that use those "clocks":

class Watch:
    def __init__(self) -> None:
        self.clock = self.__make_clock()

    @staticmethod
    def __make_clock() -> Clock:
        return Clock(0)


class Microwave:
    def __init__(self) -> None:
        self.timer = self.__make_timer()

    @staticmethod
    def __make_timer() -> Timer:
        return Timer()


class Referee:
    def __init__(self) -> None:
        self.stopwatch = self.__make_stopwatch()

    @staticmethod
    def __make_stopwatch() -> Stopwatch:
        return Stopwatch()


# some functions that use those classes:

def get_watch_time(w: Watch) -> float:
    return w.clock.time


def set_watch_time(w: Watch, t: float) -> None:
    w.clock.time = t


def get_microwave_time(m: Microwave) -> float:
    return m.timer.time_left


def set_microwave_time(m: Microwave, t: float) -> None:
    m.timer.time_left = t


def get_referee_time(r: Referee) -> float:
    return r.stopwatch.time


def set_referee_time(r: Referee, t: float) -> None:
    r.stopwatch.time = t
