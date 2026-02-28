from app.domain.account import Account
from app.domain.exceptions import AccountNotFound, InsufficientFunds

# This class defines the AccountService, which provides methods to manage bank accounts.
class AccountService:

    def __init__(self, repository):
        self.repository = repository

    # This method resets the state of the account repository by calling the reset method of the repository.
    def reset(self) -> None:
        self.repository.reset()

    # This method retrieves the balance of a specific account based on the provided account ID.
    # If the account does not exist in the repository, it raises an AccountNotFound exception.
    def get_balance(self, account_id: str) -> int:
        account = self.repository.get(account_id)

        if account is None:
            raise AccountNotFound()

        return account.balance

    # This method handles the deposit operation for a specific account.
    # It takes the destination account ID and the amount to be deposited as parameters.
    def deposit(self, destination_id: str, amount: int) -> Account:
        account = self.repository.get(destination_id)

        if not account:
            account = Account(destination_id, 0)

        account.deposit(amount)
        self.repository.save(account)

        return account

    # This method handles the withdrawal operation for a specific account.
    # It takes the origin account ID and the amount to be withdrawn as parameters.
    def withdraw (self, origin_id: str, amount: int) -> Account:
        account = self.repository.get(origin_id)

        if not account:
            raise AccountNotFound()

        if account.balance < amount:
            raise InsufficientFunds()

        account.withdraw(amount)
        self.repository.save(account)

        return account

    # This method handles the transfer operation between two accounts.
    # It takes the origin account ID, destination account ID, and the amount to be transferred
    #  as parameters. It checks if the origin account exists and has sufficient funds before performing the transfer.
    # If the destination account does not exist, it creates a new account with a balance of 0 before performing the transfer.
    def transfer(self, origin_id: str, destination_id: str, amount: int):
        origin = self.repository.get(origin_id)

        if not origin:
            raise AccountNotFound()

        if origin.balance < amount:
            raise InsufficientFunds()

        destination = self.repository.get(destination_id)
        if not destination:
            destination = Account(destination_id, 0)

        origin.withdraw(amount)
        destination.deposit(amount)

        self.repository.save(origin)
        self.repository.save(destination)

        return origin, destination
