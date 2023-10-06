from datetime import time, datetime

def main():
    now = datetime.now()
    back = datetime.fromtimestamp(0)
    seconds_left = (now - back).total_seconds()

    print("Seconds since", "{}:".format(back.strftime("%B %-d, %Y")), "{:,.4f}".format(seconds_left), "or {:.2e}".format(seconds_left), "in scientific notation")
    print("{}".format(now.strftime("%b %-d %Y")))

if __name__ == "__main__":
    main()
