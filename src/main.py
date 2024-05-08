from abc import ABC
from collections import deque
from functools import singledispatchmethod
from uuid import UUID, uuid4

import attr

from errors import DepositTooHigh, NotEnoughMoney, UnknownEvent


@attr.s(frozen=True, kw_only=True)
class Money:
    amount: int = attr.ib()
    currency: str = attr.ib()

    def __sub__(self, other):
        amount = self.amount - other.amount
        return Money(amount=amount, currency=self.currency)

    def __add__(self, other):
        amount = self.amount + other.amount
        return Money(amount=amount, currency=self.currency)


# Events:
@attr.s(frozen=True, kw_only=True)
class Event:
    producer_id: UUID = attr.ib()


@attr.s(frozen=True, kw_only=True)
class AccountCreated(Event):
    deposit: Money = attr.ib()


@attr.s(frozen=True, kw_only=True)
class MoneyWithdrawn(Event):
    amount: Money = attr.ib()


@attr.s(frozen=True, kw_only=True)
class MoneyDeposited(Event):
    amount: Money = attr.ib()


# @attr.s()
# /Events

class Entity(ABC):
    def __init__(self) -> None:
        self._constructor()

    def _constructor(self) -> None:
        self._id: UUID
        self._changes = deque()

    @classmethod
    def construct(cls):
        ag = object.__new__(cls)
        ag._constructor()
        return ag

    def _take(self, event: Event):
        """Handle an event, adds to changelog and update current state"""

        self._apply(event)
        self._changes.append(event)

    def _apply(self, event: Event) -> None:
        """Apply new event to current state"""

        raise UnknownEvent(event)


class Account(Entity):
    def __init__(self, deposit: Money) -> None:
        super().__init__()
        self._take(AccountCreated(producer_id=uuid4(), deposit=deposit))

    @singledispatchmethod
    def _apply(self, event):
        super()._apply(event)

    @_apply.register
    def _(self, event: AccountCreated):
        self._balance = event.deposit
        self._id = event.producer_id

    @_apply.register
    def _(self, event: MoneyWithdrawn):
        self._balance -= event.amount

    @_apply.register
    def _(self, event: MoneyDeposited):
        self._balance += event.amount

    def withdraw(self, amount: Money):
        if self._balance >= amount:
            self._take(MoneyWithdrawn(producer_id=self._id, amount=amount))
        else:
            raise NotEnoughMoney()

    def deposit(self, amount: Money):
        if amount.amount < 1000:
            self._take(MoneyDeposited(producer_id=self._id, amount=amount))
        else:
            raise DepositTooHigh()


def main():

    account = Account(Money(amount=1000, currency="PLN"))
    print(vars(account), "\n")

    account.withdraw(Money(amount=200, currency="PLN"))
    print(vars(account), "\n")

    account.withdraw(Money(amount=700, currency="PLN"))
    print(vars(account))
    print(account._balance, "\n")

    try:
        account.withdraw(Money(amount=1000, currency="PLN"))
        print(vars(account))
        print(account._balance)
    except Exception as e:
        print(e.__class__)
        print(e.__repr__, "\n")

    account.deposit(Money(amount=300, currency="PLN"))
    print(vars(account))
    print(account._balance)


if __name__ == "__main__":
    main()


# class Repository:
#     ...

#     def get(self, entity_id):
#         root = self._entity_class.construct()
#         changes = self._event_store.all_events_for(entity_id)

#         final_form = reduce(self._apply_event, changes, root)

#         return final_form

#     def save(self, account):
#         self._event_store.store(account.id, account.uncommited_changes)

# repo = Repository()
# repo.get(entity_id="asdf")

# repo = AccountRepository()
# repo.save(account)

# assert repo.get(account.id) == account
