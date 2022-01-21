#!/usr/bin/python3
import schedule, time
from config import *
from libs.request import send_requests


def monitor_apps():
    try:
        if checking_period > 0:
            schedule.every(checking_period).seconds.do(send_requests)
            while True:
                schedule.run_pending()
                time.sleep(1)
        else:
            send_requests()
    except KeyboardInterrupt:
        print(' Abort Command Received From User')
    print('Requests Completed Successfully!!! Logs are located at logs/monitor_log' + endc)


if __name__ == '__main__':
    monitor_apps()