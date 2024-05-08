import asyncio
from random import randrange
import time
import pytest
import pytest_asyncio


# @pytest.mark.asyncio(scope="class")
# class TestClassScoopedLoop(IsolatedAsyncIOTestCase):
#     loop: asyncio.AbstractEventLoop

#     # def setUp(self):
#     #     assert 1 == 3

#     # def asdf(self):
#     #     print("asdf")

#     async def test_remember_loop(self):
#         TestClassScoopedLoop.loop = asyncio.get_running_loop()

#     async def test_this_runs_in_same_loop(self):
#         assert asyncio.get_running_loop() is TestClassScoopedLoop.loop


async def async_add(x: int, y: int):
    print("calculating")
    asyncio.sleep(5)
    print("calculated")
    return x + y


async def async_sub(x: int, y: int):
    print("calculating")
    asyncio.sleep(5)
    print("calculated")
    return x - y


# redis =


# @pytest.mark.asyncio
# async def test_async_add():
#     result = await async_add(1, 2)
#     assert result == 3


# @pytest.mark.asyncio
# async def test_async_sub():
#     result = await async_sub(31, 6)
#     assert result == 25


@pytest.fixture
def my_fixture():
    return "Hello world"


# def test_my_fixture1(my_fixture):
#     assert my_fixture == "Hello world"


# def test_my_fixture2(my_fixture):
#     assert my_fixture == "Hello world"


# async fixtures :


@pytest_asyncio.fixture
async def loaded_data():

    print("fixture loading")
    wait = randrange(10)

    await asyncio.sleep(wait)
    print("fixture finished")

    return {"key": "value"}


@pytest.mark.asyncio
async def test_fetch_data(loaded_data):
    assert loaded_data["key"] == "value"


@pytest.mark.asyncio
async def test_fetch_data2(loaded_data):
    assert loaded_data["key"] == "value"


@pytest.mark.asyncio
async def test_fetch_data3(loaded_data):
    assert loaded_data["key"] == "value"


# class SomeClass:
#     init = False

#     def __init__(self):
#         print("fixture loading")
#         wait = randrange(10)

#         time.sleep(10)
#         print("fixture finished")

#         self.init = True


# @pytest_asyncio.fixture
# async def load_instance():
#     yield SomeClass()


# @pytest.mark.asyncio()
# async def test_load_instance(load_instance):
#     assert load_instance.init == True


# @pytest.mark.asyncio()
# async def test_load_instance_2(load_instance):
#     assert load_instance.init == True


# @pytest.mark.asyncio()
# async def test_load_instance_3(load_instance):
#     assert load_instance.init == True
