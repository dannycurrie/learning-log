#!/usr/bin/env python3
import datetime
import argparse

parser = argparse.ArgumentParser('learn')
parser.add_argument(
    '--thisweek', help='Review logs for the current week', action='store_true')

parser.add_argument('--tags', help='Show logs with a specific tag')

args = parser.parse_args()

tags = args.tags

today = datetime.datetime.today()
today_str = today.strftime('%x')
beginning_of_week = today - \
    datetime.timedelta(
        days=today.isoweekday() % 7)


def process_log(log_text):
    log_msg, *tags = log_text.split('#')
    tag_str = ''
    for tag in tags:
        tag_str += f' {tag.strip()},'
    tag_str = tag_str[:-1]
    return f'\nlog:{log_msg}|date:{today_str}|tags:{tag_str}'


def add_log():
    f = open("logfile.txt", "a")
    log_text = input("Enter log: ")
    processed_log = process_log(log_text)
    f.write(processed_log)
    f.close()


def parse_log(strlog):
    log = {}
    for piece in strlog.split('|'):
        [k, v] = piece.split(':')
        if(k == 'tags'):
            tags = v.split(',')
            v = []
            for tag in tags:
                v.append(tag.strip())
        log[k] = v
    return log


def parse_logs(file):
    line_list = [line.rstrip('\n') for line in file]
    output = []
    for line in line_list:
        if(line != ''):
            log = parse_log(line)
            output.append(log)
    return output


def log_is_newer_than_date(log, date):
    return datetime.datetime.strptime(log['date'], '%x') > date


def filter_logs_by_date(logs, date):
    output = []
    for log in logs:
        if(log_is_newer_than_date, date):
            output.append(log)
    return output


def filter_logs_by_tag(logs, tag):
    output = []
    for log in logs:
        if tag in log['tags']:
            output.append(log)
    return output


def print_logs(logs):
    for log in logs:
        print(log['log'])


def display_logs(period='all', tags=''):
    f = open("logfile.txt", "r")
    if period == 'all':
        if tags == '':
            print(f.read())
        else:
            print(f'logs tagged: {tags}')
            logs = parse_logs(f)
            filtered_logs = filter_logs_by_tag(logs, tags)
            print_logs(filtered_logs)
    elif period == 'this_week':
        print('this weeks logs!')
        logs = parse_logs(f)
        filtered_logs = filter_logs_by_date(logs, beginning_of_week)
        print_logs(filtered_logs)
    f.close()


if args.thisweek:
    display_logs('this_week')
elif tags:
    display_logs('all', tags)
else:
    add_log()
    display_logs()
