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