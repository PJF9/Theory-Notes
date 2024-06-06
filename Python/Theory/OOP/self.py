"""
In general the keyword `self` dominates in Python's Classes. We need to add it both before
every `attribute` we define and as the first `argument` on our `methods`.

We should notice that is an `object` like any other argument we pass. The `different` is that it's
actually a `reference` to the object that is calling the method, or the attribute.

So without it we would have no way to modify the object.
"""

class Empty:
    def __init__(self):
        print(self)


e = Empty()
print(e)
