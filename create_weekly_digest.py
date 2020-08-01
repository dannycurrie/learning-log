import utils
import config
import send_mail


def addLine(str, line):
    return str + "\n{}\n".format(line)


def create():
    # read in logfile
    f = open(config.path_to_logfile, "r")
    logs = utils.parse_logs(f)

    # filter to this week
    filter_this_week = utils.filter_by_date(config.beginning_of_week)
    logs = filter_this_week(logs)

    # get tags
    tags = utils.extract_sorted_tags(logs)

    # for each tag, grab matching logs
    tags_to_logs = {}
    for tag in tags:
        tags_to_logs[tag] = utils.filter_by_tags(tag)(logs)

    # write groups to email
    msg = f"""\
      Subject: Learning Log Digest
      To: danny.currie42@gmail.com
      From: danny.currie42@gmail.com
      """

    for tag in tags_to_logs.keys():
        msg = addLine(msg, '')
        msg = addLine(msg, tag)
        for log in tags_to_logs[tag]:
            msg = addLine(msg, log['log'])
    send_mail.sendMail(msg)
