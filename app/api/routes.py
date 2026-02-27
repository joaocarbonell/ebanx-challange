from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import Optional

from app.services.account_service import AccountService
from app.infrastructure.in_memory_account_repository import InMemoryAccountRepository
from app.domain.exceptions import AccountNotFound


router = APIRouter()

#Oringinal in-memory global state
repository = InMemoryAccountRepository()
service = AccountService(repository)


class EventRequest(BaseModel):
    type: str
    origin: Optional[str] = None
    destination: Optional[str] = None
    amount: int


@router.post("/reset")
def reset():
    service.reset()
    return PlainTextResponse(status_code=200, content="")


@router.get("/balance")
def get_balance(account_id: str):
    try:
        balance = service.get_balance(account_id)
        return PlainTextResponse(content=str(balance), status_code=200)
    except AccountNotFound:
        return PlainTextResponse(content="0", status_code=404)