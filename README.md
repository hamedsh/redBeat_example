# redBeat_example
redbeat periodic task with mongodb result backend

apt install redis-server mongodb-server

pip3 install celery-redbeat pymongo 

run:
terminal 1:
celery -A tasks worker -l debug

terminal 2:
celery -A tasks beat -l debug

-> should see the heartbeat task execution in terminal 1

terminal 3:
python3 urlSpeed.py -a -u www.google.com
