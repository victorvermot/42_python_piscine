import sys
sys.tracebacklimit = 0

def count_characters(s: str) -> dict:
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    res = {
        "upper_letters": [str.isupper, 0],
        "lower_letters": [str.islower, 0],
        "punctuations": [lambda f: f in punctuations, 0],
        "spaces": [str.isspace, 0],
        "digits": [str.isdigit, 0],
    }
    for letter in s:
        for x in res.values():
            if x[0](letter):
                x[1] += 1
    return res
        

def main():
    if len(sys.argv) != 2:
        raise AssertionError("Please provide one argument only")
    res = count_characters(sys.argv[1])
    print(f"The text contains {len(sys.argv[1])} characters:")
    print(f"{res['upper_letters'][1]} upper letters")
    print(f"{res['lower_letters'][1]} lower letters")
    print(f"{res['punctuations'][1]} punctuation marks")
    print(f"{res['spaces'][1]} spaces")
    print(f"{res['digits'][1]} digits")

if __name__ == "__main__":
    main()
