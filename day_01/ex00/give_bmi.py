import numpy

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    res = []
    if len(height) != len(weight):
        raise AssertionError("Lists should be the same size")
    for idx, elem in enumerate(height):
        res.append((weight[idx] / (height[idx] / 100)**2) / 10000)
    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [False if x < limit else True for x in bmi]
