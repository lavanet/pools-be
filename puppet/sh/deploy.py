from argparse import ArgumentParser
from datetime import datetime
from subprocess import check_output, check_call, DEVNULL, Popen, CalledProcessError
from time import time

BRANCH = 'master'


def check_call_quiet(args, show_time=True, **kwargs):
    starttime = time()
    check_call(args, stdout=DEVNULL, **kwargs)
    if show_time:
        print(args, f'finished: {round(time() - starttime, 2)}s')


class _Popen(Popen):
    def __init__(self, *args, **kwargs):
        self.starttime = time()
        super().__init__(*args, stdout=DEVNULL, **kwargs)

    def join(self, timeout=None):
        try:
            if retcode := self.wait(timeout=timeout):
                raise CalledProcessError(retcode, self.args)
        except:
            self.kill()
            self.wait()
            raise
        finally:
            print(self.args, f'{round(time() - self.starttime, 2)}s')


def get_pid(filepath):
    with open(filepath) as f:
        return f.read()


def get_current_commit():
    output = check_output(['git', 'rev-parse', 'HEAD'])
    commit = output.decode().strip()
    return commit


def checkout_commit(commit=BRANCH):
    check_call_quiet(['git', 'fetch'])
    check_call_quiet(['git', 'checkout', '--force', commit])
    return get_current_commit()


def pip_install():
    _Popen(['pip', 'install', '-r', 'requirements.txt']).join()


def django_manage():
    [p.join() for p in (
        _Popen(['python', 'manage.py', 'migrate', '--noinput']),
        _Popen(['python', 'manage.py', 'collectstatic', '--noinput']),
        _Popen(['python', 'manage.py', 'clear_cache']),
    )]


def restart_apps():
    """
    kill -HUP $(cat ~/uwsgi.pid)
    kill -HUP $(cat $celery_beat_pid)
    kill -HUP $(cat $celery_worker_pid)

    pkill -HUP daphne; true
    pkill -INT -f close_auctions_service

    """

    [p.join() for p in (
        _Popen(['kill', '-HUP', get_pid('~/uwsgi.pid')]),
        # _Popen(['kill', '-HUP', get_pid('/vagrant/uwsgi/celery/worker.pid')]),
        # _Popen(['kill', '-HUP', get_pid('/vagrant/uwsgi/celery/beat.pid')]),
    )]


def deploy():
    initial_commit = get_current_commit()
    latest_commit = checkout_commit()
    if initial_commit != latest_commit:
        try:
            print('New commit.')
            # pip_install()
            # django_manage()
            # restart_apps()
        except Exception as e:
            print(type(e).__name__, e)
            if input('Rollback? [y/N], Abort [Ctrl+C]: ').lower() == 'y':
                checkout_commit(initial_commit)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('command', nargs='?', default='deploy')
    parser.add_argument('-f', '--force', action='store_true')
    args = parser.parse_args()
    print(f'\n--- TIME: {datetime.now()} ---'
          f'\n--- COMMAND: {args.command} ---\n')
    try:
        globals()[args.command]()
    except KeyError:
        print(f'Unknown command: {args.command}')
    except KeyboardInterrupt:
        print('Aborted.')
    except Exception as e:
        print(type(e).__name__, e)
    print()


if __name__ == '__main__':
    parse_args()
