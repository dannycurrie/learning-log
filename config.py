import datetime

path_to_logfile = '/Users/curried/documents/projects/learning-logs/logfile.txt'
path_to_log_repo = '/Users/curried/documents/projects/learning-logs/.git'

tag_separator = '#'
field_separator = ';'
date_fmt = '%xS'

today = datetime.datetime.today()
today_str = today.strftime(date_fmt)
beginning_of_week = today - \
    datetime.timedelta(
        days=today.isoweekday() % 7)
