import pytest

from app.services.account_service import AccountService
from app.infrastructure.in_memory_account_repository import InMemoryAccountRepository
from app.domain.exceptions import (
    AccountNotFound,
    InsufficientFunds,
    NegativeValue,
)


def create_service():
    repository = InMemoryAccountRepository()
    return AccountService(repository), repository


def test_withdraw_from_non_existing_account_raises_exception():
    """
    Tests that withdrawing from a non-existing account raises AccountNotFound.
    """
    service, _ = create_service()

    with pytest.raises(AccountNotFound):
        service.withdraw(origin_id="100", amount=10)


def test_withdraw_with_insufficient_funds_raises_exception():
    """
    Tests that withdrawing more than the available balance raises InsufficientFunds.
    """
    service, _ = create_service()

    service.deposit(destination_id="100", amount=10)

    with pytest.raises(InsufficientFunds):
        service.withdraw(origin_id="100", amount=20)


def test_withdraw_subtracts_balance_correctly():
    """
    Tests that a valid withdraw subtracts the correct amount from the balance.
    """
    service, repository = create_service()

    service.deposit(destination_id="100", amount=20)
    account = service.withdraw(origin_id="100", amount=5)

    assert account.balance == 15

    saved_account = repository.get("100")
    assert saved_account.balance == 15


def test_withdraw_with_negative_value_raises_exception():
    """
    Tests that withdrawing a negative amount raises NegativeValue.
    """
    service, _ = create_service()

    service.deposit(destination_id="100", amount=20)

    with pytest.raises(NegativeValue):
        service.withdraw(origin_id="100", amount=-5)