# This module defines the Account class, which represents a bank account with an account ID and balance.
# The Account class includes a method for depositing funds, which updates the account balance accordingly.
from app.domain.exceptions import NegativeValue


class Account:
    """
        A class to represent a bank account.

        Attributes:
        ----------
        account_id : str
            A unique identifier for the account.
        balance : int
            The current balance of the account, default is 0.
    """

    def __init__(self, account_id: str, balance: int = 0):
        """
            Constructs all the necessary attributes for the Account object.

            Parameters:
            ----------
            account_id : str
                A unique identifier for the account.
            balance : int, optional
                The initial balance of the account (default is 0).
        """
        self.account_id = account_id
        self.balance = balance


    def deposit(self, amount: int):
        """
            Adds the specified amount to the account balance.

            This method increases the account's balance by the given amount. It assumes
            that the amount is a positive integer.

            Parameters:
            ----------
            amount : int
                The amount to be deposited into the account. Must be a positive integer.
        """
        if amount <= 0:
            raise NegativeValue()

        self.balance += amount

    def withdraw(self, amount: int):
        """
            Subtracts the specified amount from the account balance.

            This method decreases the account's balance by the given amount. It assumes
            that the amount is a positive integer and that the account has sufficient funds.

            Parameters:
            ----------
            amount : int
                The amount to be withdrawn from the account. Must be a positive integer.
        """
        if amount <= 0:
            raise NegativeValue()

        self.balance -= amount


