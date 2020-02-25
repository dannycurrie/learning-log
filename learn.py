#!/usr/bin/env python3
import datetime
import setup
import config
import utils
import logs_repo as logfile

args = setup.args

logfile.sync_local_logfile()

if args.thisweek:
    filter_this_week = utils.filter_by_date(config.beginning_of_week)
    utils.display_logs(filter_this_week, 'All logs from this week: ')
elif args.tags:
    filter_by_tag = utils.filter_by_tags(args.tags)
    utils.display_logs(filter_by_tag, f'All logs tagged with: {args.tags}')
elif args.all:
    utils.display_logs(utils.return_all, 'All logs:')
elif args.sync:
    logfile.sync_remote_logfile()
else:
    utils.add_log()
    logfile.commit_local_logfile()
    utils.display_logs()
