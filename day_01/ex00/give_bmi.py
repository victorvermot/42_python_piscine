def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    res = []
    if len(height) != len(weight):
        raise AssertionError(
            "Arguments provided should be of type list and have the same size"
        )
    for idx, elem in enumerate(height):
        try:
            res.append((weight[idx] / (height[idx])**2))
        except TypeError:
            raise AssertionError(
                "Values provided should be of type int | float"
            ) from None
    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [False if x < limit else True for x in bmi]
