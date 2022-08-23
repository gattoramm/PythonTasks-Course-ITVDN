import asyncio
from asyncio.coroutines import iscoroutine
import time


def sync_worker(number, divider):
    print('Sync worker with values {} / {}'.format(number, divider))
    time.sleep(3)
    print(number / divider)


# @_asyncio.coroutine
# def async_worker(number, divider):
#     print('Async Worker with values {} / {}'.format(number, divider))
#     yield from _asyncio.sleep(3)
#     print(number / divider)


async def async_worker(number, divider):
    print('Async Worker with values {} / {}'.format(number, divider))
    await asyncio.sleep(3)
    print(number / divider)

# sync
sync_worker(30, 10)
sync_worker(30, 10)

print(iscoroutine(sync_worker))
print(iscoroutine(async_worker(10, 2)))
print()

# async
event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(async_worker(30, 10)),
    event_loop.create_task(async_worker(50, 25))
]
task = asyncio.wait(task_list)
event_loop.run_until_complete(task)
event_loop.close()
