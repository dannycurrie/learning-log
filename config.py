import datetime

path_to_logfile = '/Users/dannycurrie/Documents/code projects/learning/learning_log_db/logfile.txt'
path_to_log_repo = '/Users/dannycurrie/Documents/code projects/learning/learning_log_db/.git'

tag_separator = '#'
field_separator = ';'
date_fmt = '%xS'

today = datetime.datetime.today()
today_str = today.strftime(date_fmt)
beginning_of_week = today - \
    datetime.timedelta(
        days=today.isoweekday() % 7)
# set to midnight
beginning_of_week = datetime.datetime(
    beginning_of_week.year, beginning_of_week.month, beginning_of_week.day)
