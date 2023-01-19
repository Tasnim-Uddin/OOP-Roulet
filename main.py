import random


class Outcome:
    """
    Each number has a variety of outcomes i.e. ("Red" 1:1)
    Test: test = Outcome("test",5), then test.winAmount(5) = 25
    Chapter 5, pages 37-43
    """

    def __init__(self, name: str, odds: int):
        self.name = str(name)
        self.odds = int(odds)

    def winAmount(self, amount: float) -> float:
        return self.odds * amount

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __ne__(self, other) -> bool:
        return self.name != other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return "{name:s} ({odds:d})".format_map(vars(self))

    def __repr__(self):
        return "{class_:s} ({name!r}, {odds!r})".format(
            class_=type(self).__name__, **vars(self)
        )


class Bin(frozenset):
    """
    Each bin will have 12-14 Outcomes
    Frozenset means a unique values, fixed once created
    Extended (inherits all methods from frozenset e.g. .add())
    Chapter 6, pages 45-48
    """
    pass


class Wheel:
    """
    Contains 38 bins
    Responsible for Random Number Generation (RNG)
    Chapter 7, pages 49-52
    """
    def __init__(self):
        self.bins = list(Bin() for _ in range(38))  # use _ instead of i because we are just adding 38 bin objects, not using the i
        self.rng = random.Random()
        self.rng.seed(4)

    def addOutcome(self, number, outcome):
        self.bins[number] = Bin(self.bins[number] | Bin([outcome]))

    def next(self):
        return self.rng.randint(0, 37)  # TODO

    def get(self, bin):
        return self.bins[bin]


w = Wheel()
print(w.next())
print(w.next())
print(w.next())
