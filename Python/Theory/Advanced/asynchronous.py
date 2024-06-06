"""
Sychronous Programming:
----------------------

- The structure of a sychronous program is executed sequencially. That means that each
    statementhas to wait for the previous one to finish executing.
- On Sychronous Programming the speed in which the program is going to be executed
    depends on the thread and CPU/GPU power in general.
"""
"""
Asychronous Programming:
-----------------------

- On Asycrhonous Programming the notion of sequence cease to exist. That means that in
    order for a given statement to start executing, it doesn't need necessarily the previous
    one to be completed.
- Examples of asychronous programs are `server connections`, `internet downloads`, etc.
- According to Wikipedia, "Asychrony, refers to the occurrence of events independent of
    the main program flow and ways to deal with such events."

`Coroutines`
- The first thing in order to create an Asychronous Program is creating a `coroutine`.
- Coroutines are wrappers that allow functions and other components of the program to
    run asynchronously.
- To define a function as coroutine before the `def` keyword we are adding the keyword
    `async`.
- We can call asynchronous functions with the keyword `await`. If we skip `await` and
    try to call the function with the regular way then the function is never going to
    get called, we will get an RuntimeWarning telling us that the function "never awaited".

`Event Loop`
    - Just by passing the `await` keyword doesn't mean that the function is going to be called.
        In order to do so, we need to create an "event loop".
    - We can craete an event loop with the `asyncio.run` method with argument to asychronous
        function we want to call (takes as parameter a coroutine object)

The `await` keyword can only be used inside an asynchronous function.

`Tasks`
    - By just creating coroutines and setting an event loop we cannot perfrorm the asynchronous
        notion we want. In order to achieve that we need to craete "tasks".
    - Those tasks, allow other part of code to be executed and when the function of the task
        finish executing it returns the output in a variable.
    - To wait until a specific task is finished we use the keyword `await` on the task variable.
        This way we can block the program for continue executing.
    - We can get the return of a task (the return value of a function that has being declared as 
        task) using future, a place-holder for that exaclty variable. To get that variable we assign
        a variable when awaiting for the task to complete.
"""

import asyncio
from timeit import default_timer as timer


### Example 1
async def main():
    task = asyncio.create_task(foo("PJF"))
    print("PJ")
    await task

    print("Task Finished")


async def foo(text):
    print(text)
    await asyncio.sleep(1)

# asyncio.run(main())


## Example 2: `main doesn't need to wait for foo to finish execution so main finish execution is 1 sec`
async def main():
    print("PJ")
    task = asyncio.create_task(foo("PJF"))
    await asyncio.sleep(1)
    print("Task Finished")


async def foo(text):
    print(text)
    await asyncio.sleep(10)

# asyncio.run(main())


## Example 3: Running two coroutines at the same time
# Coroutine 1
async def fetch_data():
    print("[INFO] Start fetching...")
    await asyncio.sleep(2)
    print("[INFO] Done fetching...")

    return {"data": 1}

# Coroutine 2
async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

# Event Loop
async def main():
    # Starting Asynchronously the Tasks (the second task starts execution when the inside the first task we await)
    task_1 = asyncio.create_task(fetch_data())
    task_2 = asyncio.create_task(print_numbers())

    # Waiting for the first task to be completed in order to continue
    value = await task_1
    print(value)

    # Waiting for the second task to finish in order to continue
    await task_2

# asyncio.run(main())


## Example 3: using `gather`

async def f1(n):
    await asyncio.sleep(0.5)
    return n

async def f2():
    for i in range(10):
        yield i

async def f3():
    start = timer()
    results = await asyncio.gather(*[f1(i) for i in range(10)])
    print(results)
    print(f"Took, {timer() - start}")

    start = timer()
    results = [await f1(i) async for i in f2()]
    print(results)
    print(f"Took, {timer() - start}")


asyncio.run(f3())
