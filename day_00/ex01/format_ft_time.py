from datetime import time, datetime

def main():
    now = datetime.now()
    back = datetime.fromtimestamp(0)
    print("Seconds since January 1, 1970: " "{:,.4f}".format((now-back).total_seconds()))
    print(f"{now.month}")

if __name__ == "__main__":
    main()
