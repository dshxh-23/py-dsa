import functools


class SolutionInfo:
    __slots__ = {
        "problem", 
        "soln_number", 
        "approach", 
        "description", 
        "note"
    }

    # -- -- -- --

    def __init__(self, problem, soln_num, approach, desc="", note=""):
        self.problem = problem
        self.soln_number = soln_num
        self.approach = approach
        self.description = desc
        self.note = note

    # -- -- -- --

    def __repr__(self):
        """TO BE IMPLEMENTED LATER"""
        ...


# ---- ---- Registry ---- ----


class SolutionRegistry:
    """DOCUMENTATION LATER"""

    # Structure:
    # {
    #     "Two Sum": {
    #         1: {"info": ..., "func": ...},
    #         2: {"info": ..., "func": ...}
    #     },
    #     "3Sum": { ... }
    # }

    _registry = {}

    # -- -- -- --

    def __new__(cls, *args, **kwargs):
        raise TypeError(
            "ProblemRegistry is a static class and cannot be instanciated."
        )

    # -- -- -- --

    def register(cls, info: SolutionInfo, func):
        prob = info.problem
        soln_num = info.soln_number

        # create nested dict for a new problem if it doesn't exist.
        if prob not in cls._registry:
            cls._registry[prob] = {}

        # raise ValueError for already used approach number
        if soln_num in cls._registry[prob]:
            raise ValueError(
                f"[REGISTRY] Solution #{soln_num} for problem '{prob}' is already registered!"
            )

        cls._registry[prob][soln_num] = {
            "info" : info,
            "func" : func,
        }

    # -- -- -- --

    # def run(cls, problem: str, soln_num: int, *args, **kwargs):
    #     """Run a specific approach for a specific problem"""

    #     if not problem_name in cls._registry:
    #         raise KeyError(
    #             f""
    #         )

    #     approaches = cls._registry[problem_name]

    #     if not number in approaches:
    #         raise KeyError(
    #             f""
    #         )

    #     return approaches[number]["func"](*args, **kwargs)



    # -- -- -- --

    def run_all(cls, problem_name: str, *args, **kwargs):
        """Run all approaches for a specific problem"""
        ...


# ---- ---- Decorator ---- ----


def solution(
    problem: str, 
    solution_number: int, 
    approach: str, 
    description: str ="", 
    note: str =""
):
    """Decorator factory to return custom decorator that attaches approach metadata to the function"""

    if not isinstance(problem, str) or problem.strip():
        raise ValueError(
            f"[APPROACH] 'problem_name' must be a string, got {problem!r}"
        )


    if not isinstance(solution_number, int) or solution_number < 1:
        raise ValueError(
            f"[APPROACH] 'solution_number' must be a positive integer, got {solution_number!r}"
        )

    if not isinstance(approach, str) or approach.strip():
        raise ValueError(
            f"[APPROACH] 'approach' must be a non-empty string, got {approach!r}"
        )

    def decorator(func):
        info = SolutionInfo(problem, solution_number, approach, description, note)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) 

        wrapper._problem_info = info

        return wrapper

    return decorator
        