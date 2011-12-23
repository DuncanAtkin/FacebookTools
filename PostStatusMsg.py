#!/usr/bin/python
import sys
import fbconsole
fbconsole.APP_ID = '177876045644347'
fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access']
fbconsole.authenticate()
message = sys.argv[1]
status = fbconsole.post('/me/feed', {'message': message})
print "Status posted, ID %s" % status['id']
