#!/usr/bin/env python3
""" Async comprhension Task0"""
import Async, random


async def async_generator():
    """ coroutine called async_generator that takes no arguments.
        The coroutine will loop 10 times, each time asynchronously
        wait 1 second, then yield a random number between 0 and 10.
    """
    for i in range(10):
        await async.sleep(1)
        yield random.uniform(0, 10)

