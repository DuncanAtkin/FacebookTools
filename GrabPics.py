#!/usr/bin/python
from urllib import urlretrieve
import imp
urlretrieve('https://raw.github.com/facebook/fbconsole/master/src/fbconsole.py', '.fbconsole.py')
fbconsole = imp.load_source('fb', '.fbconsole.py')


profile_pic = fbconsole.get('/zuck/picture', {"type":"large"})
urlretrieve(profile_pic, 'duncan.jpg')

#profile_pic = graph_url('/zuck/picture', {"type":"large"})
#urlretrieve(profile_pic, 'duncan.jpg')
