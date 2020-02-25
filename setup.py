import argparse

parser = argparse.ArgumentParser('learn')
parser.add_argument(
    '--thisweek', help='Review logs for the current week', action='store_true')

parser.add_argument(
    '--all', help='Review all logs', action='store_true')

parser.add_argument(
    '--sync', help='Sync local logs with remote logfile', action='store_true')

parser.add_argument('--tags', help='Show logs with a specific tag')

args = parser.parse_args()
