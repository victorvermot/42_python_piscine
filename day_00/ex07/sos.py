import sys
sys.tracebacklimit = 0


def convert_to_morse(s: str) -> str:
    MORSE_CODE_DICT = {
        'A': '.- ', 'B': '-... ',
        'C': '-.-. ', 'D': '-.. ', 'E': '. ',
        'F': '..-. ', 'G': '--. ', 'H': '.... ',
        'I': '.. ', 'J': '.--- ', 'K': '-.- ',
        'L': '.-.. ', 'M': '-- ', 'N': '-. ',
        'O': '--- ', 'P': '.--. ', 'Q': '--.- ',
        'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ',
        'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ',
        '1': '.---- ', '2': '..--- ', '3': '...-- ',
        '4': '....- ', '5': '..... ', '6': '-.... ',
        '7': '--... ', '8': '---.. ', '9': '----. ',
        '0': '----- ', ' ': '/ '
    }
    res = ""
    for char in s:
        res += MORSE_CODE_DICT[char.upper()]
    return res


def check_arg(s: str):
    for char in s:
        if not (char.isalnum() or char.isspace()):
            raise AssertionError("The arguments are bad")


def main():
    if len(sys.argv) != 2:
        raise AssertionError("The arguments are bad")
    try:
        check_arg(sys.argv[1])
    except AssertionError as e:
        print(f"{e}")
        return
    print(convert_to_morse(sys.argv[1]))


if __name__ == "__main__":
    main()
