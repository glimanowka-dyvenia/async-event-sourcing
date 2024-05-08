from typing import Optional

from sqlmodel import SQLModel


# class Customer(SQLModel):
#     id: str
#     name: str
#     surname: str
#     email: str
#     phone_mobile: Optional[str]
#     country: str
#     address: str


# class CustomerCreated(SQLModel):
#     name: str
#     surname: str
#     phone_mobile: str
#     country: str
#     address: str


# class CustomerPartial(SQLModel):
#     name: Optional[str]
#     surname: Optional[str]
#     phone_mobile: Optional[str]
#     country: Optional[str]
#     address: Optional[str]


# import datetime
# from enum import Enum
# from typing import Optional

# from sqlmodel import SQLModel


# class CustomerRecordKind(Enum):
#     CUSTOMER_CREATED = "customer_created"
#     CUSTOMER_UPDATED = "customer_updated"


# class CustomerRecordSQL(SQLModel):
#     kind: CustomerRecordKind
#     name: Optional[str]
#     surname: Optional[str]
#     phone_mobile: Optional[str]
#     country: Optional[str]
#     address: Optional[str]
#     created_at: datetime  # record created at


# class CustomerCreatedSQL(SQLModel):
#     name: str
#     surname: str
#     email: str
#     phone_mobile: Optional[str]
#     country: str
#     address: str
#     created_at: datetime  # record created at


# class CustomerUpdatedSQL(SQLModel):
#     name: Optional[str]
#     surname: Optional[str]
#     phone_mobile: Optional[str]
#     country: Optional[str]
#     address: Optional[str]
#     created_at: datetime  # record created at


# class CustomerCreatedAPI(SQLModel):
#     """
#     Model for Create Customer scenario - incoming from API
#     """

#     name: str
#     surname: str
#     email: str
#     phone_mobile: Optional[str]
#     country: str
#     address: str


# class CustomerUpdatedAPI(SQLModel):
#     """
#     Model for Update Customer scenario - incoming from API
#     """

#     name: Optional[str]
#     surname: Optional[str]
#     phone_mobile: Optional[str]
#     country: Optional[str]
#     address: Optional[str]
