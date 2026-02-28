import pytest

from app.services.account_service import AccountService
from app.infrastructure.in_memory_account_repository import InMemoryAccountRepository
from app.domain.exceptions import NegativeValue


def create_service():
    repository = InMemoryAccountRepository()
    return AccountService(repository), repository


def test_deposit_creates_account_when_not_exists():
    """
    Tests whether a new deposit creates an account when it does not exist.

    This test verifies that performing a deposit on a non-existing account
    correctly creates the account with the specified initial balance.

    Assertions:
    - The created account ID matches the provided ID.
    - The created account balance matches the deposited amount.
    - The created account is stored in the repository with the correct balance.
    """
    service, repository = create_service()

    account = service.deposit(destination_id="100", amount=10)

    assert account.account_id == "100"
    assert account.balance == 10

    saved_account = repository.get("100")
    assert saved_account is not None
    assert saved_account.balance == 10


def test_deposit_adds_balance_when_account_exists():
    """
    Tests whether a deposit adds balance to an existing account.

    This test verifies that performing a deposit on an existing account
    correctly updates the account balance by adding the deposited amount.

    Assertions:
    - The account balance is correctly incremented after the deposit.
    """
    service, _ = create_service()

    service.deposit(destination_id="100", amount=10)
    account = service.deposit(destination_id="100", amount=5)

    assert account.balance == 15


def test_deposit_with_negative_value_raises_exception():
    """
    Tests whether a deposit with a negative value raises an exception.

    This test verifies that attempting to perform a deposit with a negative
    amount raises a `NegativeValue` exception.

    Assertions:
    - The `NegativeValue` exception is raised when attempting to deposit
      a negative amount.
    """
    service, _ = create_service()

    with pytest.raises(NegativeValue):
        service.deposit(destination_id="100", amount=-10)


@pytest.mark.parametrize("amount", [1, 10, 100])
def test_deposit_various_amounts(amount):
    """
    Tests deposits with different amounts.

    This test verifies that performing deposits with different values
    correctly updates the account balance.

    Parameters:
    - amount (int): The amount to be deposited into the account.

    Assertions:
    - The account balance matches the deposited amount.
    """
    service, _ = create_service()

    account = service.deposit(destination_id="100", amount=amount)

    assert account.balance == amount