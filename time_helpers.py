import os
import time
import calendar
from datetime import datetime


def mkdir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except Exception as e:
        raise e


def utc_to_ts(dt):
    return calendar.timegm(dt.utctimetuple())


def dt_to_ts(dt):
    return time.mktime(dt.timetuple())


def ts_to_utc(ts):
    try:
        return datetime.utcfromtimestamp(float(ts))
    except:
        return None


def ts_to_dt(ts):
    try:
        return datetime.fromtimestamp(float(ts))
    except:
        return None


