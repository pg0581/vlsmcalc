#!/usr/bin/python3

from ipaddress import ip_address, summarize_address_range

first = ip_address(u'<enter_starting_IP_here')
last = ip_address(u'enter_ending_IP_here')


print list(summarize_address_range(first, last))
