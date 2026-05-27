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


def complexity_report(obj):

    if isinstance(obj, type):   # checks if obj is a class, use it
        cls = obj
    else:                       # if object is an instance, get its class
        cls = type(obj)

    title = f"Complexity Report: {cls.__name__}"
    print(f"\n{title}")
    print("="*len(title))

    found = False

    for name in dir(cls):
        
        # omit dunder methods
        if name.startswith("__") and name.endswith("__"):
            continue

        method = getattr(cls, name, None)   # get attribute or None if it doesn't exist

        if callable(method) and hasattr(method, '_complexity'):
            info = method._complexity

            print(f"\n  {name}()")
            print(f"\tTime\t:\t{info.time}")
            print(f"\tSpace\t:\t{info.time}")
            if info.note:
                print(f"\tNote\t:\t{info.note}")
            
            found = True
        
        if not found:
            print("No complexity decorators found.")
        
        print()