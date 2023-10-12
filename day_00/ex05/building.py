import sys
import string
sys.tracebacklimit = 0

def count_characters(s: str) -> dict:
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    res = {
        "upper_letters": 0,
        "lower_letters": 0,
        "punctuations": 0,
        "spaces": 0,
        "digits": 0,
    }
    for c in s:n
        if c.isupper():
            res["upper_letters"] += 1
        elif c.islower():
            res["lower_letters"] += 1
        elif c.isdigit():
            res["digits"] += 1
        elif c.isspace():
            res["spaces"] += 1
        elif c in punctuations:
            res["punctuations"] += 1
    return res
        

def main():
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    res = count_characters(sys.argv[1])
    print(f"The text contains {len(sys.argv[1])} characters:")
    print(f"{res['upper_letters']} upper letters")
    print(f"{res['lower_letters']} lower letters")
    print(f"{res['punctuations']} punctuation marks")
    print(f"{res['spaces']} spaces")
    print(f"{res['digits']} digits")

if __name__ == "__main__":
    main()