 # Copyright (c) 2016 {UPRC}.
 # All rights reserved. This program and the accompanying materials
 # are made available under the terms of the The MIT License (MIT).
 # which accompanies this distribution, and is available at
 # http://opensource.org/licenses/MIT

 # Contributors:
 #    {Constantinos Patsakis} {UPRC}
 # Initially developed in the context of OPERANDO EU project www.operando.eu

import urllib
import urllib2

url = 'http://localhost:8888/log'
params = urllib.urlencode({
                          'RequestingComponent': "component",
                          'RequestID': "7",
                          'IP': "10.0.0.1",
                          'mac': "00:11:22:33:44:55",
                          'RequestedURL': "/url/url",
                          'RequestedData': "data",
                          'Action': 1,
                          'ClientTypeID': 0
                          })
response = urllib2.urlopen(url, params).read()
