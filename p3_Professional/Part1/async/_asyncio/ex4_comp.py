import asyncio

@asyncio.coroutine
def async_worker(number, divider):
    print('Worker with values {} / {}'.format(number, divider))
    yield from asyncio.sleep(0)
    print(number / divider)


event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(async_worker(30, 10)),
    event_loop.create_task(async_worker(30, 10))
]
task = asyncio.wait(task_list)
event_loop.run_until_complete(task)
event_loop.close()
