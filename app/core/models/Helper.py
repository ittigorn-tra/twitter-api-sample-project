import sys
import os
import inspect
import pytz
import datetime
import pprint as ppp
import dateutil.parser
import pickle
import gzip

if __name__ == "__main__":
    inc_path = os.path.realpath(os.path.abspath(os.path.dirname(
        os.path.split(inspect.getfile(inspect.currentframe()))[0])))
    for i in range(10):
        if os.path.split(inc_path)[1].lower() == 'app':
            inc_path = os.path.dirname(inc_path)
            break
        else:
            inc_path = os.path.dirname(inc_path)
    else:
        raise Exception('Cannot find the project root path')
    if inc_path not in sys.path:
        sys.path.append(inc_path)

from app.core.settings import Settings


class Helper:
    _settings = Settings()

    @staticmethod
    def format_decimals(amount, decimals: int = 2, comma: bool = True):
        decimals = str(decimals)
        comma = ',' or ''
        pattern = "{0:" + comma + '.' + decimals + "f}"
        return pattern.format(amount)

    @classmethod
    def format_whole_numbers(cls, amount=None):
        return cls.format_decimals(amount, decimals=0, comma=True) if amount is not None else '-'

    @staticmethod
    def human_format(num):
        num = float('{:.3g}'.format(num))
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', ' K', ' M', ' B', ' T'][magnitude])

    @classmethod
    def parse_datetime(cls, dt, tz=None, **kwargs):
        fmt = kwargs['fmt'] if 'fmt' in kwargs else '%Y-%m-%d %H:%M:%S.%f'
        if tz is None:
            tz = pytz.timezone(cls._settings.default_timezone)
        result = datetime.datetime.strptime(dt, fmt)
        if tz is not False:
            result = result.astimezone(tz)
        return result

    @classmethod
    def get_datetime(cls, dt_obj=None, fmt=None, tz=None, **kwargs):
        if 'dt_obj' in kwargs:
            dt_obj = kwargs['dt_obj']
        if 'fmt' in kwargs:
            fmt = kwargs['fmt']
        if 'tz' in kwargs:
            tz = kwargs['tz']
        return_obj = kwargs['return_obj'] if 'return_obj' in kwargs else False
        if fmt is None:
            if 'fmt' in kwargs:
                fmt = kwargs['fmt']
        if tz is None:
            tz = cls._settings.default_timezone
        if dt_obj is None:
            dt_obj = pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None)
            if tz is not False:
                dt_obj = dt_obj.astimezone(pytz.timezone(tz))
        if return_obj:
            return dt_obj
        else:
            if fmt is None:
                fmt = '%Y-%m-%d %H:%M:%S.%f'
            return dt_obj.strftime(fmt)

    @classmethod
    def get_iso_datetime(cls, dt_obj=None, tz=None, **kwargs):
        if 'dt_obj' in kwargs:
            dt_obj = kwargs['dt_obj']
        if 'tz' in kwargs:
            tz = kwargs['tz']
        return_obj = kwargs['return_obj'] if 'return_obj' in kwargs else False
        if tz is None:
            tz = cls._settings.default_timezone
        if dt_obj is None:
            dt_obj = pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None)
            if tz is not False:
                dt_obj = dt_obj.astimezone(pytz.timezone(tz))
        return dt_obj.isoformat()

    @staticmethod
    def get_utc(return_obj=False):
        result = datetime.datetime.utcnow()
        if not return_obj:
            result = result.strftime('%Y-%m-%d %H:%M:%S.%f')
        return result

    @classmethod
    def localize_utc(cls, dt_obj, tz=None):
        utc = pytz.utc
        dt_obj = utc.localize(dt_obj)
        if tz is None:
            tz = cls._settings.default_timezone
        return dt_obj.astimezone(pytz.timezone(tz))

    @classmethod
    def localize_utc_timestamp(cls, ts, return_obj=False):
        result = pytz.utc.localize(datetime.datetime.strptime(
            ts, '%Y-%m-%d %H:%M:%S.%f')).astimezone(pytz.timezone(cls._settings.default_timezone))
        if not return_obj:
            return result.strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            return result

    @classmethod
    def localize_iso8601_utc_timestamp(cls, ts, return_obj=False):
        result = dateutil.parser.parse(ts).astimezone(
            pytz.timezone(cls._settings.default_timezone))
        if not return_obj:
            return result.strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            return result

    @staticmethod
    def pprint(x):
        pp = ppp.PrettyPrinter(indent=2)
        pp.pprint(x)

    @classmethod
    def save_pickle(cls, obj, name: str, protocol: int = None):
        protocol = protocol or cls._settings.pickle_protocol
        zipped = True if name.lower().endswith('.gz') else False
        if zipped:
            b = pickle.dumps(obj, protocol)
            with gzip.open(name, 'wb') as zf:
                zf.write(b)
        else:
            with open(name, 'wb') as f:
                pickle.dump(obj, f, protocol)

    @staticmethod
    def load_pickle(name: str):
        zipped = True if name.lower().endswith('.gz') else False
        if zipped:
            with gzip.open(name, 'rb') as zf:
                buffer = b""
                while True:
                    data = zf.read()
                    if data == b"":
                        break
                    buffer += data
                return pickle.loads(buffer)
        else:
            with open(name, 'rb') as f:
                return pickle.load(f)

    # @staticmethod
    # def print_me():
    #   if AppConfig.log_level > 0:
    #     k = 'Petch'
    #     x = ('Z\x06\x15\x12\tp\x06\x15\x04\x10p\x06\x15\x04\t|o\x15\x04\t'
    #       'pETCH0ETCHZ\x06T\x04\x180bTCH0EqCEpE~\x04\tp\r'
    #       '#\x04Ep\x06\x15\x13\t~\r'
    #       '~\x04\tp\x06\x15\x0b'
    #       '\x17-\x06$\x12\x10Z\x06\x15\x04\tp\x06\x15\x0b'
    #       '\x17wo')
    #     msg = []
    #     for i, c in enumerate(x):
    #       key_c = ord(k[i % len(k)])
    #       enc_c = ord(c)
    #       msg.append(chr((enc_c - key_c) % 127))
    #     print( ''.join(msg) )

    # @classmethod
    # def print_log(cls, *args, **kwargs):
    #   this_log_level = kwargs.get('log_level', AppConfig.default_log_level)
    #   if AppConfig.log_level > 0:
    #     if AppConfig.log_level >= this_log_level:
    #       if AppConfig.log_to_stdout:
    #         print(cls.get_datetime(), *args)
    #       if AppConfig.log_to_file:
    #         with open(AppConfig.log_file_path, "a+") as f:
    #           print(cls.get_datetime(), *args, file=f)

    # @staticmethod
    # def remove_log_file():
    #   if os.path.exists(AppConfig.log_file_path):
    #     os.remove(AppConfig.log_file_path)

    # @staticmethod
    # def get_last_month_end():
    #   now = datetime.datetime.now()
    #   res = datetime.datetime(now.year, now.month, now.day) + pd.tseries.offsets.MonthEnd(-1)
    #   return res

    # @classmethod
    # def get_last_month_begin(cls):
    #   return cls.get_last_month_end() + pd.tseries.offsets.MonthBegin(-1)

    # @classmethod
    # def get_this_month_begin(cls):
    #   return cls.get_last_month_end() + pd.Timedelta(days=1)


if __name__ == '__main__':
    pass
