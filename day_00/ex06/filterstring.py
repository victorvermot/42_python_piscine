import sys
from ft_filter import ft_filter
sys.tracebacklimit = 0


def main():
    if len(sys.argv) != 3:
        raise AssertionError("The arguments are bad")
    try:
        res = ft_filter(lambda f: len(f) > int(sys.argv[2]),
                        sys.argv[1].split())
    except ValueError:
        raise AssertionError("The arguments are bad") from None
    print(res)


if __name__ == "__main__":
    main()
