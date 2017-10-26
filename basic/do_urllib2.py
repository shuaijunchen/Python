#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

request = urllib2.Request('https://github.com')
response = urllib2.urlopen(request)
print response.read()
