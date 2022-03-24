"""
Iterators for datetime objects.

This work, including the source code, documentation
and related data, is placed into the public domain.

The original author is Robert Brewer, Amor Ministries.
See http://projects.amor.org/misc/wiki/Recur for more docs.

THIS SOFTWARE IS PROVIDED AS-IS, WITHOUT WARRANTY
OF ANY KIND, NOT EVEN THE IMPLIED WARRANTY OF
MERCHANTABILITY. THE AUTHOR OF THIS SOFTWARE
ASSUMES _NO_ RESPONSIBILITY FOR ANY CONSEQUENCE
RESULTING FROM THE USE, MODIFICATION, OR
REDISTRIBUTION OF THIS SOFTWARE.

Western-language descriptions of recurrence tend to fall into
two distinct types. In order to provide some mnemonic consistency,
the base functions are named differently according to these types.
However, despite the differing names, every function yields
datetime.date or datetime.datetime objects.

First, there are the declarations which define a unit of time,
and then count successive "leaps" of those units. For example,
the declaration, "every 4 days," uses a day as the unit, and adds
4 to produce each value in the series. The functions which provide
these series are named according to the whole unit, in the plural.
Examples:
    "Every 4 days" becomes: days(start, 4, [end])
    "Every 2 weeks" becomes: weeks(start, 2, [end])
    "Every 6 hours" becomes: hours(start, 6, [end])

Second, there are the declarations which define a unit of time,
and then count by subdivisions of that unit. For example, the
declaration, "the ninth day of each month," uses a month as the
whole units and a day as the subdivision. The functions which
provide these series are named according to the whole unit,
in the singular, prefixed by "each".
Examples:
    "The ninth [day] of each month" becomes: eachmonth(start, 9, [end])
    "The penultimate [day] of each month" becomes:
        eachmonth(start, -1, [end])
    "Every Thursday" becomes "The 3rd [day] of each week" [since
        datetime.weekday() returns Thursday as the value 3]
        which becomes: eachweek(start, 3, [end])
    "08:30:00 on each day" becomes:
        eachday(start, datetime.time(8, 30), [end])
Notice that, in almost every case, the subdivision is understood to be
the "next smallest component". In the example above, one might just as
well have written, "the ninth of each month," and been understood,
since months are "composed of" days (not weeks!). Therefore, our
functions do not incorporate this "smaller unit" in the function name.
"""

import datetime
import re
import threading


def sane_date(year, month, day, highzero=False):
    """Return a valid datetime.date even if parameters are out of bounds.
    
    If the month param is out of bounds, both it and the year will be
    modified relative to the first month of the given year.
    
    If the day param is out of bounds, the day, month, and possibly year
    will be modified. If the day param is zero or negative, then the
    "zeroth day" of the given month is assumed to be the last day of the
    previous month, unless highzero is True, in which case the "zeroth day"
    is the last day of the given month.
    
    Examples:
        sane_date(2003, 2, 1) = datetime.date(2003, 2, 1)
        sane_date(2003, -10, 13) = datetime.date(2002, 2, 13)
        sane_date(2003, 12, -5) = datetime.date(2003, 11, 25)
        sane_date(2003, 12, -5, highzero=True) = datetime.date(2003, 12, 26)
    """
    while month > 12:
        month -= 12
        year += 1
    while month < 1:
        month += 12
        year -= 1
    if highzero and day < 1:
        # Count backward from the first of *next* month.
        firstOfMonth = sane_date(year, month + 1, 1)
    else:
        # Count backward/forward from the first of the current month.
        firstOfMonth = datetime.date(year, month, 1)
    newDate = firstOfMonth + datetime.timedelta(day - 1)
    return newDate

def sane_time(day, hour, minute, second):
    """Return a valid (day, datetime.time) even if parameters are out of bounds.
    
    If the hour param is out of bounds, both it and the day will
    be modified. If negative, the day will be decremented.
    
    If the minute param is out of bounds, both it and the hour will
    be modified. If negative, the hour will be decremented.
    
    If the second param is out of bounds, both it and the minute will
    be modified. If negative, the minute will be decremented.
    
    Examples:
        sane_time(0, 4, 2, 1) = (0, datetime.time(4, 2, 1)
        sane_time(0, 25, 2, 1) = (1, datetime.time(1, 2, 1)
        sane_time(0, 4, 1440, 1) = (1, datetime.time(4, 2, 1)
        sane_time(0, 0, 0, -1) = (-1, datetime.time(23, 59, 59)
    """
    while second > 59:
        second -= 60
        minute += 1
    while second < 0:
        second += 60
        minute -= 1
    while minute > 59:
        minute -= 60
        hour += 1
    while minute < 0:
        minute += 60
        hour -= 1
    while hour > 23:
        hour -= 24
        day += 1
    while hour < 0:
        hour += 24
        day -= 1
    newTime = (day, datetime.time(hour, minute, second))
    return newTime

def seconds(startDate, frequency=1, endDate=None):
    """Yield a sequence of datetimes, adding 'frequency' seconds each time.
    
    For example:
        seconds(datetime.datetime(2004, 5, 4, 14, 0), 6)
    yields the sequence: 2004-05-04 14:00:00, 2004-05-04 14:00:06,
                         2004-05-04 14:00:12, ...
    
    If startDate has no time component (i.e. if it is a datetime.date),
    then the first yielded time will be midnight (0:00:00) on that date.
    
    If endDate has no time component (i.e. if it is a datetime.date),
    then the last yielded time will be the last valid time before
    midnight on that date.
    
    For example:
        seconds(datetime.datetime(2004, 5, 4), 15, datetime.datetime(2004, 5, 5))
    yields the sequence: 2004-05-04 00:00:00, 2004-05-04 00:00:15,
                         2004-05-04 00:00:30, ...
                                          ... 2004-05-05 23:59:15,
                         2004-05-05 23:59:30, 2004-05-05 23:59:45.
    """
    if not hasattr(startDate, u'time'):
        startDate = datetime.datetime.combine(startDate, datetime.time(0))
    while (endDate is None) or (startDate <= endDate):
        yield startDate
        startDate += datetime.timedelta(seconds=frequency)

def eachminute(startDate, seconds=0, endDate=None):
    """Yield the same time for each minute. Defaults to 0 seconds.
    
    Yielded values are datetime.datetime objects.
    For example:
        eachminute(datetime.date(2004, 5, 4, 23, 55), 15)
    yields the sequence: 2004-05-04 23:55:15, 2004-05-04 23:56:15,
                         2004-05-04 23:57:15, ...
    
    If startDate has no time component (i.e. if it is a datetime.date),
    then the first yielded time will be the first valid time after
    midnight (0:00:00) on that date.
    
    If endDate has no time component (i.e. if it is a datetime.date),
    then the last yielded time will be the last valid time before
    midnight on that date.
    """
    seconds = int(seconds)
    
    if hasattr(startDate, u'time'):
        days, zerotime = sane_time(0, startDate.hour,
                                   startDate.minute, seconds)
        if days < 0 or zerotime < startDate.time():
            days, zerotime = sane_time(0, startDate.hour,
                                      startDate.minute + 1, seconds)
    else:
        days, zerotime = sane_time(0, 0, 0, seconds)
    startDate = sane_date(startDate.year, startDate.month,
                          startDate.day + days)
    startDate = datetime.datetime.combine(startDate, zerotime)
    
    while (endDate is None) or (startDate <= endDate):
        yield startDate
        startDate += datetime.timedelta(minutes=1)

def minutes(startDate, frequency=1, endDate=None):
    """Yield a sequence of datetimes, adding 'frequency' minutes each time.
    
    For example:
        minutes(datetime.datetime(2004, 5, 4, 14), 30)
    yields the sequence: 2004-05-04 14:00:00, 2004-05-04 14:30:00,
                         2004-05-04 15:00:00, ...
    
    If startDate has no time component (i.e. if it is a datetime.date),
    then the first yielded time will be midnight (0:00:00) on that date.
    
    If endDate has no time component (i.e. if it is a datetime.date),
    then the last yielded time will be the last valid time before
    midnight on that date.
    
    For example:
        minutes(datetime.datetime(2004, 5, 4), 15, datetime.datetime(2004, 5, 5))
    yields the sequence: 2004-05-04 00:00:00, 2004-05-04 00:15:00,
                         2004-05-04 00:30:00, ...
                                          ... 2004-05-05 23:15:00,
                         2004-05-05 23:30:00, 2004-05-05 23:45:00.
    """
    if not hasattr(startDate, u'time'):
        startDate = datetime.datetime.combine(startDate, datetime.time(0))
    while (endDate is None) or (startDate <= endDate):
        yield startDate
        startDate += datetime.timedelta(minutes=frequency)

def eachhour(startDate, minutes=0, seconds=0, endDate=None):
    """Yield the same time for each hour. Defaults to 00:00.
    
    Yielded values are datetime.datetime objects.
    For example:
        eachhour(datetime.date(2004, 5, 4, 6), 15)
    yields the sequence: 2004-05-04 06:15:00, 2004-05-04 07:15:00,
                         2004-05-04 08:15:00, ...
    
    If startDate has no time component (i.e. if it is a datetime.date),
    then the first yielded time will be the first valid time after
    midnight (0:00:00) on that date.
    
    If endDate has no time component (i.e. if it is a datetime.date),
    then the last yielded time will be the last valid time before
    midnight on that date.
    """
    minutes = int(minutes)
    seconds = int(seconds)
    
    if hasattr(startDate, u'time'):
        zerotime = datetime.time(startDate.hour, minutes, seconds)
        if zerotime < startDate.time():
            if zerotime.hour < 23:
                zerotime = datetime.time(zerotime.hour + 1, minutes, seconds)
            else:
                zerotime = datetime.time(0, minutes, seconds)
                startDate = sane_date(startDate.year, startDate.month,
                                      startDate.day + 1)
    else:
        zerotime = datetime.time(0, minutes, seconds)
    startDate = datetime.datetime.combine(startDate, zerotime)
    
    while (endDate is None) or (startDate <= endDate):
        yield startDate
        startDate += datetime.timedelta(hours=1)

def hours(startDate, frequency=1, endDate=None):
    """Yield a sequence of datetimes, adding 'frequency' hours each time.
    
    For example:
        hours(datetime.datetime(2004, 5, 4, 14), 6)
    yields the sequence: 2004-05-04 14:00:00, 2004-05-04 20:00:00,
                         2004-05-05 2:00:00, ...
    
    If startDate has no time component (i.e. if it is a datetime.date),
    then the first yielded time will be midnight (0:00:00) on that date.
    
    If endDate has no time component (i.e. if it is a datetime.date),
    then the last yielded time will be the last valid time before
    midnight on that date.
    
    For example:
        hours(datetime.datetime(2004, 5, 4), 8, datetime.datetime(2004, 5, 5))
    yields the sequence: 2004-05-04 00:00:00, 2004-05-04 08:00:00,
                         2004-05-04 16:00:00, 2004-05-05 00:00:00,
                         2004-05-05 08:00:00, 2004-05-05 16:00:00.
    """
    if not hasattr(startDate, "time"):
        startDate = datetime.datetime.combine(startDate, datetime.time(0))
    if endDate and not hasattr(endDate, "time"):
        endDate = datetime.datetime.combine(endDate, datetime.time(23, 59, 59))
    while (endDate is None) or (startDate <= endDate):
        yield startDate
        startDate += datetime.timedelta(hours=frequency)

def time_from_str(timeofday):
    atoms = timeofday.split(u":")
    def pop_or_zero():
        try:
            return int(atoms.pop(0))
        except TypeError:
            raise ValueError("The supplied time '%s' could not be parsed."
                             % timeofday)
        except IndexError:
            return 0
    hour = pop_or_zero()
    minute = pop_or_zero()
    second = pop_or_zero()
    return datetime.time(hour, minute, second)

def eachday(startDate, timeofday=None, endDate=None):
    """Yield the same time-of-day for each day. Defaults to midnight.
    
    Yielded values are datetime.datetime objects.
    For example:
        eachday(datetime.date(2004, 5, 4), datetime.time(14, 3, 0))
    yields the sequence: 2004-05-04 14:03:00, 2004-05-05 14:03:00,
                         2004-05-06 14:03:00, ...
    
    timeofday may be a datetime.time, as in the above example, or it
    may be a string, of the form "hour:min:sec". Seconds and minutes
    may be omitted if their colon ":" separator is also omitted. So
    the example above could be rewritten:
        eachday(datetime.date(2004, 5, 4), "14:03")
    """
    if timeofday is None:
        timeofday = datetime.time(0)
    elif isinstance(timeofday, (str, unicode)):
        timeofday = time_from_str(timeofday)
    
    # If the timeofday is less than the time of startDate,
    # don't include the startDate in the results.
    try:
        if timeofday < startDate.time():
            startDate = sane_date(startDate.year, startDate.month,
                                  startDate.day + 1)
    except AttributeError:
        # startDate is a datetime.date, and has no time() attribute
        pass
    startDate = datetime.datetime.combine(startDate, timeofday)
    # Now that we've coerced our startDate to a datetime, we need to
    # do the same thing to endDate so we can compare them.
    if endDate and not hasattr(endDate, "time"):
        endDate = datetime.datetime.combine(endDate, timeofday)
    
    while (endDate is None) or (startDate <= endDate):
        yield startDate
        startDate += datetime.timedelta(1)

def eachweekday(startDate, weekday, timeofday=None, endDate=None):
    """Yield the same time-of-day each week for the given day. The time-of-day
    defaults to midnight.
    
    Yielded values are datetime.datetime objects.
    For example:
        eachweekday(datetime.date(2006, 8, 10), 3, datetime.time(14, 3, 0))
    yields the sequence: 2006-08-11 14:03:00, 2006-08-18 14:03:00,
                         2006-08-25 14:03:00, ...
    
    timeofday may be a datetime.time, as in the above example, or it
    may be a string, of the form "hour:min:sec". Seconds and minutes
    may be omitted if their colon ":" separator is also omitted. So
    the example above could be rewritten:
        eachday(datetime.date(2004, 5, 4), "14:03")
    """
    if timeofday is None:
        timeofday = datetime.time(0)
    elif isinstance(timeofday, (str, unicode)):
        timeofday = time_from_str(timeofday)

    # get the given start time or datetime.time(0,0)
    startTime = getattr(startDate, 'time', datetime.time)()
    
    if startDate.weekday() > weekday or startTime > timeofday:
        offset = (7 + weekday) - startDate.weekday()
        while offset > 6:
            offset -= 7
        while offset <= 0:
            offset += 7
        startDate += datetime.timedelta(offset)
    
    startDate = datetime.datetime.combine(startDate, timeofday)
    
    # Now that we've coerced our startDate to a datetime, we need to
    # do the same thing to endDate so we can compare them.
    if endDate and not hasattr(endDate, "time"):
        endDate = datetime.datetime.combine(endDate, timeofday)
    
    end = getattr(endDate, 'date', lambda: None)()
    day_iter = eachweek(startDate.date(), weekday, end)
    startDate = datetime.datetime.combine(day_iter.next(), timeofday)
    
    while (endDate is None) or (startDate <= endDate):
        yield startDate
        startDate = datetime.datetime.combine(day_iter.next(), timeofday)

def days(startDate, frequency=1, endDate=None):
    """Yield a sequence of dates, adding 'frequency' days each time.
    
    For example:
        days(datetime.date(2004, 5, 4), 7)
    yields the sequence: 2004-5-4, 2004-5-11, 2004-5-18, ...
    """
    while (endDate is None) or (startDate <= endDate):
        yield startDate
        startDate += datetime.timedelta(frequency)

def eachweek(startDate, weekday=0, endDate=None):
    """Yield the same day-of-the-week for each week. Defaults to Monday.
    
    Yielded values are datetime.date objects.
    
    Weekday follows the same days of the week as datetime.weekday().
    For example:
        mon, tue, wed, thu, fri, sat, sun = range(7)
        eachweek(datetime.date(2004, 5, 4), thu)
    yields the sequence: 2004-5-6, 2004-5-13, 2004-5-20, ...
    
    If weekday is out of bounds (0-6), it will be brought in bounds.
    """
    if hasattr(startDate, 'time'):
        startDate = startDate.date()
    weekday = int(weekday)
    offset = (7 + weekday) - startDate.weekday()
    while offset > 6:
        offset -= 7
    while offset < 0:
        offset += 7
    startDate += datetime.timedelta(offset)
    return days(startDate, 7, endDate)

def weeks(startDate, frequency=1, endDate=None):
    """Yield a sequence of dates, adding 'frequency' weeks each time.
    
    For example:
        weeks(datetime.date(2004, 5, 4), 2)
    yields the sequence: 2004-5-4, 2004-5-18, 2004-6-1, ...
    """
    while (endDate is None) or (startDate <= endDate):
        yield startDate
        startDate += datetime.timedelta(frequency * 7)

def eachmonth(startDate, day=1, endDate=None):
    """Yield the same day of each month. Defaults to the first day.
    
    Yielded values are datetime.date objects.
    
    If day is a positive number, return that date for each month,
    starting with startDate. For example:
        eachmonth(datetime.date(2004, 5, 4), 15)
    yields the sequence: 2004-5-15, 2004-6-15, 2004-7-15, ...
    
    If day is zero or negative, return the same date counting
    backwards from the end of the month. For example:
        eachmonth(datetime.date(2004, 5, 4), -5)
    yields the sequence: 2004-5-26, 2004-6-25, 2004-7-26, ...
    
    If day specifies a day which does not appear in every month,
    then the closest valid date within that month will be used instead.
    For example:
        eachmonth(datetime.date(2004, 5, 4), 31)
    yields the sequence: 2004-5-31, 2004-6-30, 2004-7-31, ...
    
    If startDate is greater than what would otherwise be the first date
    in the sequence, that first item is not yielded; instead, the next
    item becomes the first item yielded.
    
    If endDate is less than what would otherwise be the last date in the
    sequence, that last item is not yielded, and the sequence ends.
    """
    if hasattr(startDate, 'time'):
        startDate = startDate.date()
    day = int(day)
    highzero = (day < 1)
    index = 0
    while True:
        firstDate = sane_date(startDate.year, startDate.month + index, day, highzero)
        if firstDate >= startDate:
            break
        index += 1
    startDate = firstDate
    
    while (endDate is None) or (startDate <= endDate):
        yield startDate
        startDate = sane_date(startDate.year, startDate.month + 1, day, highzero)

def months(startDate, frequency=1, endDate=None):
    """Yield a sequence of dates, adding 'frequency' months each time.
    
    For example:
        months(datetime.date(2004, 5, 4), 3)
    yields the sequence: 2004-5-4, 2004-8-4, 2004-11-4, ...
    
    If the specified startDate contains a day which does not appear
    in every month, then the corresponding day from the next month
    will be used instead.
    For example:
        months(datetime.date(2004, 5, 31), 3)
    yields the sequence: 2004-5-31, 2004-8-31, 2004-12-1, ...
    
    If the frequency parameter is negative, the sequence descends.
    """
    day = startDate.day
    month = startDate.month
    year = startDate.year
    while True:
        if endDate is not None:
            if frequency < 0:
                if startDate < endDate: break
            else:
                if startDate > endDate: break
        
        yield startDate
        month += frequency
        startDate = sane_date(year, month, day)

def eachyear(startDate, month=1, day=1, endDate=None):
    """Yield the same day of the year for each year. Defaults to 1/1.
    
    Yielded values are datetime.date objects.
    
    If day and month are positive numbers, return that day/month for each
    year, starting with startDate. For example:
        eachyear(datetime.date(2004, 5, 4), 8, 15)
    yields the sequence: 2004-8-15, 2005-8-15, 2006-8-15, ...
    
    If month is zero or negative, return the same date counting months
    backwards from the end of the year. For example:
        eachyear(datetime.date(2004, 5, 4), -2, 15)
    yields the sequence: 2004-10-15, 2005-10-15, 2006-10-15, ...
    
    If day is zero or negative, return the same date counting days
    backwards from the end of the month. For example:
        eachyear(datetime.date(2004, 5, 4), -2, -1)
    yields the sequence: 2004-10-30, 2005-10-30, 2006-10-30, ...
    
    If day specifies a day which does not appear in the given month,
    then the corresponding day from the next month will be used instead.
    For example:
        eachyear(datetime.date(2004, 5, 4), 5, 31)
    yields the sequence: 2004-6-1, 2005-6-1, 2006-6-1, ...
    
    If startDate is greater than what would otherwise be the first date
    in the sequence, that first item is not yielded; instead, the next
    item becomes the first item yielded.
    
    If endDate is less than what would otherwise be the last date in the
    sequence, that last item is not yielded, and the sequence ends.
    """
    if hasattr(startDate, 'time'):
        startDate = startDate.date()
    month = int(month)
    day = int(day)
    
    index = 0
    while True:
        curDate = sane_date(startDate.year + index, month, day, True)
        if curDate >= startDate:
            break
        index += 1
    
    while (endDate is None) or (curDate <= endDate):
        yield curDate
        index += 1
        curDate = sane_date(startDate.year + index, month, day, True)

def years(startDate, frequency=1, endDate=None):
    """Yield a sequence of dates, adding 'frequency' years each time.
    
    For example:
        years(datetime.date(2004, 5, 4), 3)
    yields the sequence: 2004-5-4, 2007-5-4, 2010-5-4, ...
    
    If the specified startDate contains a day which does not appear
    in every year (i.e. leap years), then the corresponding day from
    the next month will be used instead.
    
    For example:
        years(datetime.date(2004, 2, 29), 3)
    yields the sequence: 2004-2-29, 2007-3-1, 2010-3-1, ...
    
    If the frequency parameter is negative, the sequence descends.
    """
    day = startDate.day
    month = startDate.month
    year = startDate.year
    while True:
        if endDate is not None:
            if frequency < 0:
                if startDate < endDate: break
            else:
                if startDate > endDate: break
        
        yield startDate
        year += frequency
        startDate = sane_date(year, month, day)

def byunits(startDate, whichUnit, frequency=1, endDate=None):
    """Dispatch to the appropriate unit handler.
    
    This really just exists to help out Locale series.
    """
    frequency = int(frequency)
    unithandler = (seconds, minutes, hours, days, weeks, months, years)
    return unithandler[whichUnit](startDate, frequency, endDate)

def singledate(startDate, year, month=1, day=1, endDate=None):
    """Yield a single datetime.date if y/m/d occurs between start and end."""
    year = int(year)
    month = int(month)
    day = int(day)
    
    curDate = sane_date(year, month, day)
    if curDate < startDate:
        raise StopIteration
    
    if (endDate is None) or (curDate <= endDate):
        yield curDate


class Locale(object):
    """Language-specific expression matching.
    
    To use a language other than English with Recurrence objects,
    either subclass Locale and override the "patterns" dictionary,
    or write some other callable that takes a description string
    and returns a recurrence function and its "inner" args.
    """
    
    patterns = {byunits: [r"([0-9]+) sec",
                          r"([0-9]+) min",
                          r"([0-9]+) hour",
                          r"([0-9]+) day",
                          r"([0-9]+) week",
                          r"([0-9]+) month",
                          r"([0-9]+) year",
                          ],
                # \S is any non-whitespace character.
                eachday: r"([\S]+) (?:every|each) day",
                eachweekday: [# don't match "month"
                              r"([\S]+) (?:every|each) mon(?!th)",
                              r"([\S]+) (?:every|each) tue",
                              r"([\S]+) (?:every|each) wed",
                              r"([\S]+) (?:every|each) thu",
                              r"([\S]+) (?:every|each) fri",
                              r"([\S]+) (?:every|each) sat",
                              r"([\S]+) (?:every|each) sun",
                              ],
                eachweek: [r"mon", r"tue", r"wed", r"thu", r"fri", r"sat", r"sun"],
                eachmonth: r"(-?\d+) (?:every|each) month",
                # Lookbehind for a digit and separator so we don't
                # screw up singledate, below.
                eachyear: [r"^(dummy entry to line up indexing)$",
                           r"(?<!\d\d[/ \-])(?:jan(?:uary)?|0?1)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:febr?(?:uary)?|0?2)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:mar(?:ch)?|0?3)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:apr(?:il)?|0?4)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:may|0?5)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:june?|0?6)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:july?|0?7)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:aug(?:ust)?|0?8)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:sept?(?:ember)?|0?9)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:oct(?:ober)?|10)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:nov(?:ember)?|11)[/ \-]([0-9]+)",
                           r"(?<!\d\d[/ \-])(?:dec(?:ember)?|12)[/ \-]([0-9]+)",
                           ],
                # ISO format (relaxed: 1-digit month and day OK,
                # slash or space OK)
                singledate: r"(\d\d\d\d)[/ \-]([01]?\d)[/ \-]([0123]?\d)",
                }
    regexes = {}
    
    def __init__(self):
        for key, regSet in self.patterns.items():
            if isinstance(regSet, list):
                self.regexes[key] = [re.compile(x, re.IGNORECASE)
                                     for x in regSet]
            else:
                self.regexes[key] = re.compile(regSet, re.IGNORECASE)
    
    def __call__(self, description):
        for rule, regSet in self.regexes.items():
            if isinstance(regSet, list):
                for index, regex in enumerate(regSet):
                    matches = regex.match(description)
                    if matches:
                        return rule, (index,) + matches.groups()
            else:
                matches = regSet.match(description)
                if matches:
                    return rule, matches.groups()
        
        raise ValueError(u"The supplied description ('%s') "
                         u"could not be parsed." % description)

localeEnglish = Locale()


class Recurrence(object):
    """A recurrence pattern and its iterator.
    
    The Recurrence class provides natural-language hooks for common recur
    operations. The "description" parameter should be a set of keywords in
    a natural language, which is then looked up in self.locale.regexes.
    
    Usage:
    
    import datetime, recur
    
    firstDate = datetime.date(2004, 1, 7)
    lastDate = datetime.date(2004, 2, 11)
    for eachDate in recur.Recurrence(firstDate, "Saturday", lastDate):
        print eachDate
    
    2004-01-10
    2004-01-17
    2004-01-24
    2004-01-31
    2004-02-07
    """
    
    def __init__(self, startDate=None, description="", endDate=None,
                 locale=localeEnglish):
        """
        If startDate is None (not supplied), then it will be set
        to the current date and time.
        
        Leading and trailing whitespace will be stripped from the
        description parameter.
        """
        if startDate is None:
            startDate = datetime.datetime.now()
        description = description.strip()
        
        self.startDate = startDate
        self.description = description
        self.endDate = endDate
        self.locale = locale
        self.function, args = locale(description)
        self.args = (startDate,) + args + (endDate,)
        # Form an initial generator, if for no other reason than to test args early.
        self.reset()
    
    def reset(self):
        try:
            self.generator = self.function(*self.args)
        except TypeError, x:
            x.args += self.args
            raise
    
    def __iter__(self):
        self.reset()
        return self
    
    def next(self):
        return self.generator.next()


deltazero = datetime.timedelta(0)

class Worker(object):
    """Perform work on a schedule.
    
    You must override work(), which is called at each interval.
    """
    
    def __init__(self, recurrence):
        if isinstance(recurrence, basestring):
            if recurrence:
                recurrence = Recurrence(None, recurrence)
            else:
                recurrence = None
        self.recurrence = recurrence
        
        self.createdate = datetime.datetime.now()
        self.lastrun = None
        self.nextrun = None
        self.curthread = None
        self.active = True
    
    def interval(self, next):
        """Return a timedelta (next - now).
        
        if next is None, return None.
        If next < now, return datetime.timedelta(0).
        """
        if next is None:
            return None
        
        # next can be either a datetime.datetime or a datetime.date;
        # get the correct representation of "now" from either one.
        now = getattr(next, 'now', getattr(next, 'today'))()
        return max(next - now, deltazero)
    
    def advance(self):
        """Advance self.recurrence and set self.nextrun.
        
        This function ignores dates which are in the past.
        If the recurrence series is exhausted, self.nextrun will be None.
        """
        if not self.recurrence:
            self.nextrun = None
            return
        
        try:
            next = self.recurrence.next()
        except StopIteration:
            # The recurrence series was exhausted immediately.
            self.nextrun = None
            return
        
        # next can be either a datetime.datetime or a datetime.date;
        # get the correct representation of "now" from either one.
        now = getattr(next, 'now', getattr(next, 'today'))()
        while True:
            if next >= now:
                self.nextrun = next
                break
            
            try:
                next = self.recurrence.next()
            except StopIteration:
                # The recurrence series was exhausted.
                self.nextrun = None
                break
    
    def start(self, secs=0):
        """Call self.run in a new thread."""
        if self.active:
            self.curthread = threading.Timer(secs, self.run)
            self.curthread.start()
    
    def run(self):
        """Prepare for work."""
        if self.active:
            self.work()
            self.lastrun = datetime.datetime.now()
    
    def work(self):
        """Perform the actual work. Must be overridden."""
        raise NotImplementedError
    
    def stop(self):
        """Stop work."""
        self.active = False
        if self.curthread:
            self.curthread.cancel()


class Scheduler(object):
    """Collection of Workers governed by a single scheduler thread.
    
    paused: a boolean flag indicating whether or not each Worker's start()
        method should be executed at each interval. Notice that, even if
        paused is True, the scheduler thread will still cycle, but Workers
        will not be run at each interval.
    
    terminated: a boolean flag indicating whether or not the Worker should
        continue to cycle. If terminated is True, recurring Workers will
        not schedule new threads.
    """
    
    def __init__(self, workers=None):
        if workers is None:
            workers = {}
        self.workers = workers
        self.curthread = None
        self.paused = False
        self.terminated = False
    
    def start(self):
        """Start a new recurring thread for all workers.
        
        This sets self.terminated to False, but doesn't set self.paused.
        """
        # Set nextrun for all workers
        for worker in self.workers.values():
            worker.advance()
        self.terminated = False
        self._cycle()
    
    def _cycle(self):
        """Start a new Timer for the next worker."""
        if self.terminated:
            return
        
        ivs = []
        for w in self.workers.values():
            next = w.nextrun
            if next is not None:
                ivs.append((w.interval(next), w))
        
        if ivs:
            ivs.sort()
            iv, nextworker = ivs[0]
            iv = (iv.days * 86400) + iv.seconds + (iv.microseconds / 1000000.0)
            nextworker.advance()
            self.curthread = threading.Timer(iv, self.run, (nextworker,))
            self.curthread.start()
    
    def run(self, worker):
        """Run the worker, then cycle again."""
        if not self.paused and not self.terminated:
            worker.start()
        self._cycle()
    
    def stop(self):
        self.terminated = True
        if self.curthread:
            self.curthread.cancel()
        for w in self.workers.values():
            w.stop()

