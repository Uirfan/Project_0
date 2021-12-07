class NegativeOrZeroDeposit(Exception):
    def __init__(self, message: str):
        self.message = message

class NoFunds(Exception):
    def __init__(self, message: str):
        self.message = message