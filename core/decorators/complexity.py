import functools


# ---- ---- Schema ---- ----


class ComplexityInfo:
    """Container for a function's complexity metadata."""

    __slots__ = ("time", "space", "note")

    def __init__(self, time, space, note):
        self.time = time
        self.space = space
        self.note = note

    def __repr__(self):
        base = f"ComplexityInfo(time = '{self.time}', space = '{self.space}'"
        if self.note:
            return base + f", note = '{self.note}')"
        return base + ")"


# ---- ---- Decorator ---- ----


def complexity(time, space, note=None):

    # DECORATOR: returns wrapped function with complexity info attached to function object.
    def decorator(func):

        # The wrapper function that replaces func
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)    # NO change needed in the functions behavior

        # add complxity info to the function object
        wrapper._complexity = ComplexityInfo(time, space, note)

        return wrapper
    return decorator        
        

# ---- ---- Function ---- ----


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

        if callable(method) and hasattr(method, "_complexity"):
            info = method._complexity

            print(f"\n  {name}()")
            print(f"\tTime\t:\t{info.time}")
            print(f"\tSpace\t:\t{info.space}")
            if info.note:
                print(f"\tNote\t:\t{info.note}")
            
            found = True

    if not found:
        print("\nNo complexity decorators found.")

    print()