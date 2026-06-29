class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


def normalize_name(name: str) -> str:
    if not name:
        raise ValueError("Name cannot be empty")
    return name.strip().title()


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)


def is_passing_score(score: int) -> bool:
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    return score >= 60
