from git import Repo
import config
import datetime

repo = Repo(config.path_to_log_repo)


def sync_local_logfile():
    repo.git.pull('origin')


def commit_local_logfile():
    repo.git.add(update=True)
    repo.index.commit(f'learning logs updated {datetime.datetime.now()}')

def sync_remote_logfile():
    origin = repo.remote(name='origin')
    origin.push()
