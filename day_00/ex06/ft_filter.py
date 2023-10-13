def ft_filter(function, iterable):
    """ft_filter(function or None, iterable) --> filter object

    Returns:
        Return an iterator yielding those items of iterable for which
        function(item) is true.
        If function is None, return the items that are true.
    """
    if function:
        return [x for x in iterable if function(x)].__iter__()
    return [x for x in iterable if x].__iter__()
