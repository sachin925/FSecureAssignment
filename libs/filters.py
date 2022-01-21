from config import *


def filter_url(filter_str, url):
    if url.endswith('/'):
        url = url[:-1]
    address_end = url[url.rfind('/') + 1:]
    if filter_str in address_end:
        return True
    else:
        return False


def apply_filters(response_object):
    filter_str = filter_strs
    content_requirement = contents_req
    if filter_str and not content_requirement:
        if not filter_url(filter_str, response_object.url):
            return 0
        else:
            return 1
    elif content_requirement:
        if content_requirement in response_object.text:
            return 1
        else:
            return 0
    return 1
