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



test = Outcome("test", 5)
test1 = Outcome("test", 5)
print(test.__eq__(test1))
print(test.__ne__(test1))

print(test.__hash__())
print(test1.__hash__())
