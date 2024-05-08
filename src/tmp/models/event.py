from abc import ABC
from collections import deque
from functools import reduce
from uuid import UUID, uuid4
import attr


# frozen: make instance immutable after init


@attr.s(frozen=True, kw_only=True)
class Event:
    producer_id: UUID = attr.ib()


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


@attr.s(frozen=True, kw_only=True)
class CustomerCreated(Event):
    name: str = attr.field
    surname: str = attr.field
    age: int = attr.field


class Customer(Entity):
    def __init__(self, name: str, surname: str, age: int) -> None:
        super().__init__()
        self._take(
            CustomerCreated(producer_id=uuid4(), name=name, surname=surname, age=age)
        )
        
    def change_age(self):
        


# def withdraw(self, amount: Money) -> None:
#     if self.balance >= 



class Repository:
    # ...

    def get(self, entity_id):
        root = self._entity_class.construct()  # <-
        changes = self._event_store.all_events_for(entity_id)

        final_form = reduce(self._apply_event, changes, root)

        return final_form


customer = Customer("Jan", "Nowak", 28)
customer.change_age(55)

repo = CustomerRepository()
repo.save(customer)

assert repo.get(customer.id) == customer


# customer = Customer(events=[CustomerCreated("Jan", "Nowak", 23)])


# Retrieving state with SQL and ORM:
# 1. Select a racord from database
# 2. Feed the values to the (only) constuctor
# 3. Done


# Retrieving state from an event store
# 1. Create an empty shell of an Entity without emitting any events
# 2. Grab the history of events under given ID
# 3. Apply that sequenct of events on that empty shell starting with the `Create Event`
