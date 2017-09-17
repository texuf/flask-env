
import os

ENV_PRODUCTION = 'production'
ENV_FILENAME = '.env'
ENV_LOCK_FILENAME = '.env.lock'

def _verify():
    if os.environ.get('ENVIRONMENT') != ENV_PRODUCTION and not os.path.isfile(ENV_FILENAME):
        raise Exception('file [%s] not found, please create from [%s] and add your private keys' % (ENV_FILENAME, ENV_LOCK_FILENAME))

def _get_dict(filename):
    retval = {}
    if os.path.isfile(filename):
        with open(filename) as f:
            content = f.read()
            for line in content.splitlines():
                kv = line.split('=')
                retval[kv[0]] = kv[1]
    return retval

def load():
    _verify()
    env = _get_dict(ENV_FILENAME)
    for k,v in env.items():
        os.environ[k] = v

def freeze():
    env = _get_dict(ENV_FILENAME)
    with open(ENV_LOCK_FILENAME, 'w') as f:
        for key in env.keys():
            f.write(key + '=xxxxxxxx\n')


if __name__ == '__main__':
    freeze()