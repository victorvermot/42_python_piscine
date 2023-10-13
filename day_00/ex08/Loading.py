def ft_tqdm(lst: range) -> None:
    count = 0
    for i in lst:
        print("=", end="")
        yield count
        count += 1
