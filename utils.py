from datetime import datetime


def today():

    return datetime.now().strftime("%Y-%m-%d")


def progress(done, total):

    if total == 0:
        return 0

    return round(done / total * 100, 1)


def separator():

    print("-" * 40)
