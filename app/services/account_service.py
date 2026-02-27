from app.domain.account import Account
from app.domain.exceptions import AccountNotFound, InsufficientFunds


class AccountService:
    def __init__(self, repository):
        self.repository = repository

    def reset(self) -> None:
        self.repository.reset()

    def get_balance(self, account_id: str) -> int:
        account = self.repository.get(account_id)

        if account is None:
            raise AccountNotFound()

        return account.balance