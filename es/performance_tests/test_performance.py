#!/usr/bin/env python
# -*- coding: utf-8 -*-

# elapsed
# The amount of time elapsed between sending the request and the arrival of the response (as a timedelta).
# This property specifically measures the time taken between sending the first byte of the request and
# finishing parsing the headers. It is therefore unaffected by consuming the response content or the value of
# the stream keyword argument.

import re
import json
import requests
import progressbar

time_sum = 0
time_min = None
time_max = None

runs_count = 10
times = []

url_to_test = 'http://10.2.22.52:5000/reload'


json_payload = {"checkbox":{"Brand.raw":"BMW i"},"date":{"created_on_start":"09.05.2016","created_on_end":"09.08.2016"},"sort":{"sort_type":"Date"},"search_query":""}
expected_results_cnt = 25204

re_expected_results_cnt = re.compile('(\d+) results')

print(json.dumps(json_payload))

with progressbar.ProgressBar(max_value=runs_count) as progress:
    requests.post(url_to_test, json=json_payload)

    for i in range(0, runs_count):
        response = requests.post(url_to_test, json=json_payload)
        time = response.elapsed.total_seconds() * 1000.0
        time_sum += time

        times.append(time)

        if time_min is None or time < time_min:
            time_min = time

        if time_max is None or time > time_max:
            time_max = time

        # http status code "ok?"
        if not response.ok:
            raise RuntimeError(response.text)

        # does expected results count match
        found_results_cnt = re_expected_results_cnt.findall(response.text)
        if not found_results_cnt or found_results_cnt[0] != str(expected_results_cnt):
            raise RuntimeError('Found results count differs. Found: {}'.format(found_results_cnt))

        progress.update(i)

print('{}: {} runs in {} ms'.format(url_to_test, runs_count, time_sum))
print('mean(ms): {}'.format(time_sum / runs_count))
print('min(ms): {}'.format(time_min))
print('max(ms): {}'.format(time_max))

print('-----------------------------------------------')
print('\n'.join([str(t) for t in times]))
