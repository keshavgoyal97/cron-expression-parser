class CronField:
    def validate(self):
        pass

    @classmethod
    def parse(cls, data: list):
        pass

    @classmethod
    def get_limits(cls):
        pass


class Minute(CronField):
    start_limit = 0
    end_limit = 59

    def __init__(self, minutes: list[int]):
        self.data = minutes

    @classmethod
    def parse(cls, data: list):
        return [eval(d) for d in data]

    def validate(self) -> bool:
        for mint in self.data:
            if mint > self.end_limit or mint < self.start_limit:
                return False
        return True

    @classmethod
    def get_limits(cls) -> (int, int):
        return cls.start_limit, cls.end_limit

    def __dict__(self):
        return "minute", " ".join(map(str, self.data))


class Hour(CronField):
    start_limit = 0
    end_limit = 23

    def __init__(self, hours: list[int]):
        self.data = hours

    def validate(self) -> bool:
        for hr in self.data:
            if hr > self.end_limit or hr < self.start_limit:
                return False
        return True

    @classmethod
    def parse(cls, data: list):
        return [eval(d) for d in data]

    @classmethod
    def get_limits(cls) -> (int, int):
        return cls.start_limit, cls.end_limit

    def __dict__(self):
        return "hour", " ".join(map(str, self.data))


class DayOfMonth(CronField):
    start_limit = 1
    end_limit = 31

    def __init__(self, days: list[int]):
        self.data = days

    def validate(self) -> bool:
        for day in self.data:
            if day > self.end_limit or day < self.start_limit:
                return False
        return True

    @classmethod
    def parse(cls, data: list):
        return [eval(d) for d in data]

    @classmethod
    def get_limits(cls) -> (int, int):
        return cls.start_limit, cls.end_limit

    def __dict__(self):
        return "day of month", " ".join(map(str, self.data))


class Month(CronField):
    start_limit = 1
    end_limit = 12

    def __init__(self, months: list[int]):
        self.data = months

    def validate(self) -> bool:
        for month in self.data:
            if month > self.end_limit or month < self.start_limit:
                return False
        return True

    @classmethod
    def get_limits(cls) -> (int, int):
        return cls.start_limit, cls.end_limit

    @classmethod
    def parse(cls, data: list):
        return [eval(d) for d in data]

    def __dict__(self):
        return "month", " ".join(map(str, self.data))


class DayOfWeek(CronField):
    start_limit = 1
    end_limit = 7

    def __init__(self, days_of_week: list[int]):
        self.data = days_of_week

    def validate(self) -> bool:
        for week_day in self.data:
            if week_day > self.end_limit or week_day < self.start_limit:
                return False
        return True

    @classmethod
    def get_limits(cls) -> (int, int):
        return cls.start_limit, cls.end_limit

    @classmethod
    def parse(cls, data: list):
        return [eval(d) for d in data]

    def __dict__(self):
        return "day of week", " ".join(map(str, self.data))


class Command:
    def __init__(self, command):
        self.command = command

    def __dict__(self):
        return "command", self.command
