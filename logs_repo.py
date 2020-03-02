from git import Repo
import config
import datetime

repo = Repo(config.path_to_log_repo)


def sync_local_logfile():
    try:
        print(repo.git.pull('origin'))
    except:
        print('Unable to sync local logfile')


def commit_local_logfile():
    repo.git.add(update=True)
    print(repo.index.commit(
        f'learning logs updated {datetime.datetime.now()}'))


def sync_remote_logfile():
    try:
        repo.git.push('origin')
        print('Sync complete')
    except:
        print('Unable to sync remote logfile')
