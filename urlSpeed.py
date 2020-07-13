import argparse

import tasks
from redbeat import RedBeatSchedulerEntry as Entry

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', action='store_true')
parser.add_argument('-d', '--delete', action='store_true')
parser.add_argument('-u', '--url')
parser.add_argument('-t', '--timeout', default=5)
parser.add_argument('-r', '--repeat', default=5)
parser.add_argument('-k', '--key')


def doAction(args):
    if args.add:
        url = args.url
        key = args.key
        if key is None:
            print("require key")
            return -1
        timeout = args.timeout
        repeat = args.repeat
        if url is None:
            print('url is required')
            return -1
        entry = Entry(f'urlCheck_{key}', 'tasks.urlSpeed', repeat, args=['GET', url, timeout, key], app=tasks.app)
        entry.save()
        print(f"url added, key={entry.key}, store key for deletion")
    elif args.delete:
        key = args.key
        if key is None:
            print("require key")
            return -1
        entry = Entry.from_key(key, app=tasks.app)
        entry.delete()
        print("task deleted")


if __name__ == '__main__':
    args = parser.parse_args()
    doAction(args)
