from abc import ABC
from collections import deque
from functools import reduce, singledispatchmethod
from uuid import UUID, uuid4
import attr


class NotEnoughMoney(Exception):
    """Exception raised when funds on account are not sufficient"""

    pass


class UnknownEvent(Exception):
    """Raised when an Event kind is not known"""

    pass


@attr.s(frozen=True, kw_only=True)
class Event:
    producer_id: UUID = attr.ib()


@attr.s(frozen=True, kw_only=True)
class Money:
    amount: int = attr.ib()
    currency: str = attr.ib()

    def __sub__(self, other):
        amount = self.amount - other.amount
        return Money(amount=amount, currency=self.currency)


@attr.s(frozen=True, kw_only=True)
class AccountCreated(Event):
    deposit: Money = attr.ib()


@attr.s(frozen=True, kw_only=True)
class MoneyWithdrawn(Event):
    amount: Money = attr.ib()


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
        # self._id = acc_created.producer_id

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

    # def _balance(self) -> Money:
    #     # TODO: Implement it
    #     pass

    def withdraw(self, amount: Money):
        if self._balance >= amount:
            self._take(MoneyWithdrawn(producer_id=self._id, amount=amount))
        else:
            raise NotEnoughMoney()

        # update = AccountUpdatedWithdrawal(producer_id=uuid4(), withdrawal=money)
        # self._changes.append(update)


class Repository:
    ...

    def get(self, entity_id):
        root = self._entity_class.construct()
        changes = self._event_store.all_events_for(entity_id)

        final_form = reduce(self._apply_event, changes, root)

        return final_form

    def save(self, account):
        self._event_store.store(account.id, account.uncommited_changes)


def main():
    print("Hi")
    # event = Event(producer_id=uuid4())
    # print(vars(event))
    # print(event.producer_id)

    # entity = Entity()
    # print(entity)

    # acc_created = AccountCreated(
    #     producer_id=uuid4(), deposit=Money(amount=1000, currency="PLN")
    # )
    # print(acc_created)

    account = Account(Money(amount=1000, currency="PLN"))
    print(vars(account))
    print("\n")

    account.withdraw(Money(amount=200, currency="PLN"))
    print(vars(account))
    print("\n")

    account.withdraw(Money(amount=700, currency="PLN"))
    print(vars(account))
    print("\n")

    print(account._balance)

    # repo = Repository()
    # repo.get(entity_id="asdf")

    # repo = AccountRepository()
    # repo.save(account)

    # assert repo.get(account.id) == account


if __name__ == "__main__":
    main()
