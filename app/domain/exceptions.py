class AccountNotFound(Exception):
    """Raised when an account is not found in the repository."""
    pass

class InsufficientFunds(Exception):
    """Raised when an account does not have enough balance to perform a transaction."""
    pass

class NegativeValue(Exception):
    """Raised when a negative value is provided for a transaction amount."""
    pass