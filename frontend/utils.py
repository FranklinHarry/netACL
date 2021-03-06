import os


def url_join(*parts):
    if len(parts) > 0:
        return ('/' if parts[0].startswith('/') else '') \
               + '/'.join(s.strip('/') for s in parts) \
               + ('/' if parts[-1].endswith('/') else '')
    return None


def query_join(query_dict):
    return '?' + '&'.join('&'.join([k + '=' + val for val in v])
                          for k, v in query_dict.items()) \
        if len(query_dict) > 0 \
        else ''


def mkdir(*dirs):
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)


def mkfile(path):
    mkdir(os.path.dirname(path))
    touch(path)