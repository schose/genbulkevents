#!/usr/bin/python

import time
import random
import base64

start = time.time()

run = 1

while time.time() < start + 10:
    t = time.strftime('%Y-%m-%dT%H:%M:%S')
    timezone = time.strftime('%z')
    millis = "%.3d" % (time.time() % 1 * 1000)

    level = random.sample(['DEBUG', 'INFO', 'WARN', 'ERROR'], 1)[0]
    message = random.sample(['Don\'t worry, be happy.',
                             'error, ERROR, Error!',
                             'Nothing happened. This is worthless. \
Don\'t log this.'], 1)[0]

    logger = random.sample(['FooClass',
                            'BarClass',
                            'AuthClass',
                            'LogoutClass',
                            'BarClass',
                            'BarClass',
                            'BarClass',
                            'BarClass'], 1)[0]

    user = random.sample(['user01',
                          'user02',
                          'user03',
                          'user04',
                          'user01'], 1)[0]

    ip = random.sample(['193.28.153.192',
                        '193.99.144.85',
                        '88.215.213.26',
                        '31.192.116.24',
                        '173.194.32.238',
                        '8.8.8.8'], 1)[0]

    req_time = str(int(abs(random.normalvariate(0, 1)) * 1000))
    session_length = str(random.randrange(1, 12240))
    session_id = base64.b64encode(str(random.randrange(1000000, 1000000000)))
    extra = random.sample(['network=qa',
                           'network=prod',
                           'session_length=' + session_length,
                           'session_id="' + session_id + '"',
                           'user=extrauser'], 1)[0]

    fields = []
    fields.append('logger=' + logger)
    fields.append('user=' + user)
    fields.append('ip=' + ip)
    fields.append('req_time=' + req_time)
    fields.append(extra)

    fields.pop(random.randrange(0, len(fields)))

    print "%s.%s%s %s %s [%s]" % (t, millis, timezone, level, message, ", ".join(fields))

    run = run + 1
    # short break every 10 loops 
    mod = run % 7
    if (mod == 0):
         time.sleep(0.01)


