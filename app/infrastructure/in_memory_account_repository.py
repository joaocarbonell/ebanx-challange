from typing import Optional
from app.domain.account import Account

# This class implements an in-memory repository for managing Account objects.
# It provides methods to reset the repository, retrieve an account by its ID, and save an account to the repository.
# The accounts are stored in a dictionary, where the keys are account IDs and the values are Account instances.
class InMemoryAccountRepository:
    def __init__(self):
        self._accounts: dict[str, Account] = {}

    # This method clears all accounts from the repository, effectively resetting its state.
    def reset(self) -> None:
        self._accounts.clear()

    # This method retrieves an account from the repository based on the provided account ID.
    def get(self, account_id: str) -> Optional[Account]:
        return self._accounts.get(account_id)

    # This method saves an account to the repository. If an account with the same ID already exists, it will be overwritten.
    def save(self, account: Account) -> None:
        self._accounts[account.account_id] = account

