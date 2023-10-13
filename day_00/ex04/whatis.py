import sys
sys.tracebacklimit = 0

if len(sys.argv) != 2:
    raise AssertionError("more than one argument is provided")

try:
    int(sys.argv[1])
except ValueError:
    raise AssertionError("argument is not an integer") from None

if int(sys.argv[1]) % 2:
    print("I'm odd")
else:
    print("I'm even")
