# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/13 21:56
# @File   : time_tools.py
import time
import datetime as dt


class TimeTools:

    format_d_t = "%Y-%m-%d %H:%M:%S"
    format_d = "%Y-%m-%d"

    @classmethod
    def get_format_time(cls, date, format_s: str = None) -> str:
        """
        获取格式化后的时间（exp：2018-06-13 21:55:55）
        :param date: 需格式化的时间
        :param format_s: 时间格式
        :return:
        """
        try:

            format_s = cls.format_d_t if format_s is None else format_s
            date_t = None

            if isinstance(date, dt.datetime) or isinstance(date, dt.date):
                date_t = date.timetuple()
            elif (isinstance(date, float) or isinstance(date, int)) and len(str(int(date))) == 10:
                date_t = time.localtime(date)
            elif (isinstance(date, float) or isinstance(date, int)) and len(str(int(date))) == 13:
                date_t = time.localtime(date / 1000)

            return time.strftime(format_s, date_t)

        except TypeError:
            pass
        except Exception as e:
            print(e)

    @classmethod
    def get_until_time(cls, date, format_s: str = None) -> dt.datetime:
        """
        获取指定时间的datetime对象
        :param date: 时间，可为时间戳或者字符串时间
        :param format_s: 时间为字符串时需添加格式
        :return:
        """
        try:

            format_s = cls.format_d_t if format_s is None else format_s
            date_t = None

            if isinstance(date, str):
                date_t = time.strptime(date, format_s)
                # print(date_t)
            elif (isinstance(date, int) or isinstance(date, float)) and len(str(int(date))) == 10:
                date_t = time.localtime(date)
            elif (isinstance(date, int) or isinstance(date, float)) and len(str(int(date))) == 13:
                date_t = time.localtime(date / 1000)

            return dt.datetime(date_t.tm_year,
                               date_t.tm_mon,
                               date_t.tm_mday,
                               date_t.tm_hour,
                               date_t.tm_min,
                               date_t.tm_sec)

        except AttributeError:
            pass
        except Exception as e:
            print(e)

    @classmethod
    def get_seconds(cls, date, format_s: str = None) -> float:
        """
        获取指定时间的时间戳
        :param date:时间，可为时间戳或者字符串时间
        :param format_s: 时间为字符串时需添加格式
        :return:
        """
        try:
            format_s = cls.format_d_t if format_s is None else format_s
            date_t = None

            if isinstance(date, str):
                date_t = time.strptime(date, format_s)
            if isinstance(date, dt.datetime) or isinstance(date, dt.date):
                date_t = date.timetuple()

            return time.mktime(date_t)

        except TypeError:
            pass
        except Exception as e:
            print(e)

    @classmethod
    def begin_of_day_mills(cls, day=None):
        """
        获取一天开始时的毫秒时间戳，默认为当天
        :param day: 指定时间
        :return:
        """
        try:
            day_u = dt.date.today() if day in (None, "") else cls.get_until_time(day)

            return cls.get_seconds(dt.date(day_u.year, day_u.month, day_u.day)) * 1000

        except AttributeError:
            pass
        except Exception as e:
            print(e)

    @classmethod
    def end_of_day_mills(cls, day=None):
        """
        获取一天的结束时间的毫秒时间戳， 默认为当天
        :param day: 指定时间
        :return:
        """
        try:

            return cls.begin_of_day_mills(day) + 24 * 60 * 60 * 1000 - 1

        except TypeError:
            pass
        except Exception as e:
            print(e)

    @staticmethod
    def get_month_end_day(year: int, month: int) -> int:
        """
        获取某年某月的最后一天
        :param year: 某年
        :param month: 某月
        :return:
        """
        days = 31
        while days:
            try:
                datetime.date(year=year, month=month, day=days)
                return days
            except ValueError:
                days -= 1

    @staticmethod
    def begin_of_month_day(month, year=dt.date.today().year):
        """
        获取某月的第一天
        :param month:
        :param year:
        :return:
        """
        try:

            return dt.date(year, month, 1)

        except ValueError:
            pass

    @classmethod
    def end_of_month_day(cls, month, year=dt.date.today().year):
        """
        获取某月的最后一天
        :param month:
        :param year:
        :return:
        """
        try:

            return dt.date(year, month, cls.get_month_end_day(year, month))

        except ValueError:
            pass

    @classmethod
    def get_interval_day_by_day(cls, interval: int, date=None):
        """
        获取某日（默认今天）相隔几天的日期
        :param interval:正数为日期往前添加天数，负数为日期减去天数
        :param date:指定日期
        :return:
        """
        try:

            date = dt.date.today() if date is None else date
            date = date if isinstance(date, dt.date) else cls.get_until_time(date, cls.format_d)
            time_del = dt.timedelta(days=interval)

            return date + time_del

        except Exception as e:
            print(e)

    @classmethod
    def different_days(cls, date1: str, date2: str):
        """
        获取两个日期之间相差几天
        :param date1: 指定日期1，格式为（2018-05-22）
        :param date2: 指定日期2，格式为（2018-06-15）
        :return:
        """
        try:

            date1_u = cls.get_until_time(date1, cls.format_d)
            date2_u = cls.get_until_time(date2, cls.format_d)

            return (date1_u - date2_u).days

        except Exception as e:
            print(e)


