import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

    return what


# async def main():
#     print("Hi")
#     # print(f"started at {time.strftime('%X')}")

#     # await say_after(1, "hello")
#     # await say_after(3, "world")

#     task1 = asyncio.create_task(say_after(4, "hello"))
#     task2 = asyncio.create_task(say_after(3, "world"))
#     print(f"started at {time.strftime('%X')}")

#     a = await task1
#     print("printin", a)

#     b = await task2

#     print(a, b)

#     print(f"finished at {time.strftime('%X')}")

#     # print(f"finished at {time.strftime('%X')}")


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(3, "hello"))
        task2 = tg.create_task(say_after(4, "world"))

        print(f"started at {time.strftime('%X')}")

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())


##

import json
from typing import List, Union
import typing
from fastapi import APIRouter
from fastapi import FastAPI

from email.message import Message

from requests import Session
from typing import Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: List["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name = str
    age: Optional[int] = Field(default=None, index=True)

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="heroes")


def main():
    print("Hello ")

    team = Team(name="team1", headquarters="some headquarters")
    print(team)

    key_error = KeyError("asdf adfdsdff dfdff")

    print(key_error)

    if "adfdsdff dfdff" == key_error:
        print("ASFFDFD")

    key_error.message
