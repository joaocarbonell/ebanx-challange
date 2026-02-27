from typing import Optional
from app.domain.account import Account


class InMemoryAccountRepository:
    def __init__(self):
        self._accounts: dict[str, Account] = {}

    def reset(self) -> None:
        self._accounts.clear()

    def get(self, account_id: str) -> Optional[Account]:
        return self._accounts.get(account_id)
