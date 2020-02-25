import datetime
import setup
import config


def process_log(log_text):
    log_msg, *tags = log_text.split(config.tag_separator)
    tag_str = ' '
    for tag in tags:
        tag_str += f' {tag.strip()},'
    tag_str = tag_str[:-1].strip()
    return f'\nlog:{log_msg}{config.field_separator}date:{config.today_str}{config.field_separator}tags:{tag_str}'


def add_log():
    f = open(config.path_to_logfile, "a")
    log_text = input("Enter log: ")
    processed_log = process_log(log_text)
    f.write(processed_log)
    f.close()


def parse_log(strlog):
    log = {}
    for piece in strlog.split(config.field_separator):
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
    return datetime.datetime.strptime(log['date'], config.date_fmt) > date


def print_logs(logs):
    for log in logs:
        print(log['log'])


def filter_by_tags(tag):
    def f(logs):
        output = []
        for log in logs:
            if tag in log['tags']:
                output.append(log)
        return output
    return f


def filter_by_date(date):
    def f(logs):
        output = []
        for log in logs:
            if(log_is_newer_than_date, date):
                output.append(log)
        return output
    return f


def return_all(logs):
    return logs


def display_logs(filter_fn=return_all, msg=''):
    f = open(config.path_to_logfile, "r")
    logs = parse_logs(f)
    print(msg)
    filtered_logs = filter_fn(logs)
    print_logs(filtered_logs)
    f.close()
