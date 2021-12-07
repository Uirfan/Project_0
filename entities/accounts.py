class Account:
    def __init__(self, account_id: int, account_name: str, user_id: int, balance: float):
        self.account_id = account_id
        self.account_name = account_name
        self.user_id = user_id
        self.balance = float(balance)

    def make_account_dictionary(self):
        return {
            "accountId": self.account_id,
            "accountName": self.account_name,
            "user_id": self.user_id,
            "balance": self.balance
        }
