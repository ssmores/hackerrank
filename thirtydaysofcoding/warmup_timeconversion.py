"""Warmup questions from HackerRank.


Staircase
by vatsalchanana

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Input Format

A single string containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 01 <= hh <= 12 and 00 <= mm,ss <= 59.

Output Format

Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

Sample Input

07:05:45PM

Sample Output

19:05:45

**************
Featured solutions 
Python 2

s = raw_input()
zn = s[-2:]
if zn == "PM" and s[:2] != "12":
    s = str(12 + int(s[:2])) + s[2:]
if zn == "AM" and s[:2] == "12":
    s = "00" + s[2:]
print s[:-2]


**************
"""
#!/bin/python

import sys

time = raw_input().strip()

if time[-2] == 'A' and time[0:2] == '12':
    print '00' + time[2:-2]
elif time[-2] == 'A':
    print time[:-2]
elif time[-2] == 'P' and time[0:2] == '12':
    print time[:-2]
else:
    hours = int(time[0:2])
    hours += 12
    conv = str(hours) + time[2:-2]
    print conv

