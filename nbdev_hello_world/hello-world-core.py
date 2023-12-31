# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_hello_world_core.ipynb.

# %% auto 0
__all__ = ['say_hello', 'foo', 'HelloSayer']

# %% ../nbs/00_hello_world_core.ipynb 2
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'

# %% ../nbs/00_hello_world_core.ipynb 10
def foo(): pass

# %% ../nbs/00_hello_world_core.ipynb 11
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): self.to = to
        
    def say(self):
        "Do the saying"
        return say_hello(self.to)
