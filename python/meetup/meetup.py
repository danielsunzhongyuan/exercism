from calendar import Calendar
def meetup_day(year, month, day_of_week, sequence):
    candidates = [
        date for date in Calendar().itermonthdates(year, month) if date.month == month if date.strftime('%A') == day_of_week
    ]
    if sequence == 'teenth':
        return next(d for d in candidates if 13 <= d.day <= 19)
    idx = -1 if (sequence == 'last') else (int(sequence[0]) - 1)
    return candidates[idx]
