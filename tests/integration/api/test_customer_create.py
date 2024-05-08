import asyncio
import pytest


async def async_add(x: int, y: int):
    print("calculating")
    asyncio.sleep(5)
    print("calculated")
    return x + y


@pytest.mark.asyncio
async def test_async_add2():
    result = await async_add(1, 2)
    assert result == 3
