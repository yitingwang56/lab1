#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys
from operator import itemgetter


### mapper.py ### 
logfile = "/root/mapreduce-test/mapreduce-test-data/access.log"
f = open(logfile, 'r')
fs = f.read()

mapper_results_file = "/root/mapreduce-test/mapreduce-test-data/mapper_results.txt"
mapper_results = open(mapper_results_file, "w")

dict_ip_count = {}

pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in fs.splitlines():
    match = pat.search(line)
    if match:
    	#print '%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1)
    	
        mapper_results.write('%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1) + "\n")


mapper_results.close()

### reducer.py ###
reduc_f = open(mapper_results_file, "r")
reduc_fs = reduc_f.read()


for reduc_line in reduc_fs.splitlines():
    reduc_line = reduc_line.strip()
    ip, num = reduc_line.split('\t')
    try:
        num = int(num)

        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

    except ValueError:
        pass


sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0), reverse=True)

for ip, count in sorted_dict_ip_count[:3]:
    print '%s\t%s' % (ip, count)