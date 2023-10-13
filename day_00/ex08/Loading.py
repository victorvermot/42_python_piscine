def ft_tqdm(lst: range) -> None:
    count = 0
    bar_length = 105
    total = len(lst)

    for i in lst:
        count += 1
        yield
        filled_up_length = int(round(bar_length * count / float(total)))
        percentage = round(100.0 * count/float(total), 1)
        bar = '=' * filled_up_length + ' ' * (bar_length - filled_up_length)
        if count == total:
            bar = bar + '>'
        print(f"\r{int(percentage)}%|[{bar}]| {count}/{len(lst)}", end="")
