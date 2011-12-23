#!/usr/bin/python
import sys
import fbconsole
fbconsole.APP_ID = '177876045644347'
fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access']
fbconsole.authenticate()
uri = sys.argv[1]
picture = fbconsole.post('/me/photos', {'source':open(uri)})
print "Picture posted, ID %s" % picture['id']

