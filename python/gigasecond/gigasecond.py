from datetime import datetime, timedelta

def add_gigasecond(bday):
    return bday + timedelta(seconds=10**9)
