import os, requests
from config import endc
from datetime import datetime
from data.site_list import *
from libs.log_writer import log_response, log_timeout, log_too_many_redirects
from libs.response import get_response_obj
from libs.filters import apply_filters
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def request_loop(response_log,  url):
    print('Sending request to ' + url + endc)
    date_time_str = str(datetime.now())
    try:
        response = requests.get(url, allow_redirects=True, verify=False, timeout=5)
    except requests.exceptions.Timeout:
        log_timeout(date_time_str, response_log, url)
        return
    except requests.exceptions.TooManyRedirects:
        log_too_many_redirects(date_time_str, response_log, url)
        return
    except requests.exceptions.RequestException as e:
        print('Ohh No!! Major Issues Found' + endc)
        raise SystemExit(e)
    if str(site_content_and_requirements[url]) not in str(response.content):
        print('Anomaly in content:', response.content,)
    if response.status_code is not 200:
        print('Anomaly in status codes:', response.status_code, response.reason + endc)
    response_object = get_response_obj(date_time_str, response, url)
    if apply_filters(response_object) is 0:
        return
    log_response(response_log, response_object)


def send_requests():
    if not os.path.isdir('../logs/'):
        print('Creating logs/' + endc)
        os.mkdir('../logs')
    try:
        file_name = os.path.join('../logs/', 'monitor_log')
        response_log = open(file_name, 'a')
    except OSError:
        raise SystemExit('Could not open file: ' + file_name + endc)
    print('Initiating requests: ' + str(datetime.now()) + endc)

    for url in site_content_and_requirements.keys():
        request_loop(response_log, url)
    response_log.close
