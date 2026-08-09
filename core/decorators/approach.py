import functools


class ProblemInfo:
    __slots__ = {"approach_number", "approach_name", "description", "note"}

    # -- -- -- --

    def __init__(self, num, name, desc="", note=""):
        self.approach_number = num
        self.approach_name = name
        self.description = desc
        self.note = note

    # -- -- -- --

    def __repr__(self):
        """TO BE IMPLEMENTED LATER"""
        ...


# ---- ---- Registry ---- ----


class ProblemRegistry:
    """TO BE IMPLEMENTED LATER"""
    ... 


# ---- ---- Decorator ---- ----

def approach(number: int, name: str, desc: str ="", note: str =""):
    if not isinstance(number, int) or number < 1:
        raise ValueError(
            f"[APPROACH] 'approach_number' must be a positive integer, got {number!r}"
        )

    if not isinstance(name, str):
        raise ValueError(
            f"[APPROACH] 'name' must be a string, got {name!r}"
        )

    def decorator(func):
        info = ProblemInfo(number, name, desc, note)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) 

        wrapper._problem_info = info

        return wrapper

    return decorator
        