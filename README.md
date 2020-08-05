# redBeat_example
redbeat periodic task with mongodb result backend

`apt install redis-server mongodb-server`

`pip3 install requirements.txt` or activate the venv

run:
terminal 1:
`celery -A tasks worker -l debug`

terminal 2:
`celery -A tasks beat -l debug`

-> should see the heartbeat task execution in terminal 1

terminal 3:

- add task:
`python3 urlSpeed.py -a -u www.google.com -k [key]`
-delete task: `python3 urlSpeed.py -a -k [key]`
