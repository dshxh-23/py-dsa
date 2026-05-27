import functools

class ComplexityInfo:
    __slots__ = {'time', 'space', 'note'}

    def __init__(self, time, space, note):
        self.time = time
        self.space = space
        self.note = note

    def __repr__(self):
        base = f"ComplexityInfo(time = '{self.time}', space = '{self.space}'"
        if self.note:
            return base + f", note = '{self.note}')"
        return base + ")"



def complexity(time, space, note=None):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
            
        wrapper._complexity = ComplexityInfo(time=time, space=space, note=note)

        return wrapper
    return decorator