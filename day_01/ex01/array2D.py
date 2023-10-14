import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if type(family).__name__ != 'list':
        raise AssertionError("First argument needs to be a list")
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    try:
        res = np.array(family)[start:end]
        if len(res):
            print(f"My new shape is : ({len(res)}, {len(res[0])})")
        else:
            print(print(f"My new shape is : ({len(res)}, {len(res)})"))
    except ValueError:
        raise AssertionError(
            "List element should be of the same size"
        ) from None
    return res
