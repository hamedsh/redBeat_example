import os
import sys
import requests
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import celeryConfig
import time

from celery import Celery
from datetime import datetime, time

app = Celery('celeryExample')
app.config_from_object(celeryConfig)


@app.task
def heartBeat():
    print('-------- inside heartbeat')
    return datetime.now()


@app.task
def urlSpeed(url, method, timeout):
    try:
        st = time.time()
        res = requests.request(method.upper(), url, timeout=timeout)
        load_time = time.time() - st
        load_time = round(load_time, 1)
        res.raise_for_status()
    except requests.exceptions.Timeout as e:
        return 408, "timeout exception"
    except requests.HTTPError as e:
        return -1, "Failed to get fund status from MFR API: {}".format(str(e.errno))
    except Exception as e:
        return -2, e.args[0]
    return 200,load_time

