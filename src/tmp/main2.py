from abc import ABC
from collections import deque
from functools import reduce
from uuid import UUID, uuid4
import attr


@attr.s(frozen=True, kw_only=True)
class Money:
    amount: int = attr.ib()
    currency: str = attr.ib()


@attr.s(frozen=True, kw_only=True)
class Event:
    producer_id: UUID = attr.ib()


@attr.s(frozen=True, kw_only=True)
class AccountCreated(Event):
    # deposit: Money = attr.ib()
    deposit: Money = attr.ib()


@attr.s(frozen=True, kw_only=True)
class AccountUpdatedWithdrawal(Event):
    withdrawal: Money = attr.ib()


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


class Account(Entity):
    def __init__(self, deposit: Money) -> None:
        super().__init__()
        self._take(AccountCreated(producer_id=uuid4(), deposit=deposit))

    def _take(self, acc_created: AccountCreated):
        self._changes.append(acc_created)
        # self._id = acc_created.producer_id

    def withdraw(self, money: Money):
        update = AccountUpdatedWithdrawal(producer_id=uuid4(), withdrawal=money)
        self._changes.append(update)


class Repository:
    ...

    def get(self, entity_id):
        root = self._entity_class.construct()
        changes = self._event_store.all_events_for(entity_id)

        final_form = reduce(self._apply_event, changes, root)

        return final_form


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

    account.withdraw(Money(amount=200, currency="PLN"))
    print(vars(account))

    # repo = Repository()
    # repo.get(entity_id="asdf")


if __name__ == "__main__":
    main()
