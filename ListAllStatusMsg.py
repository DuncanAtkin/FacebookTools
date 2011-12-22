#!/usr/bin/python

import fbconsole
fbconsole.APP_ID = '177876045644347'
fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access']
fbconsole.authenticate()
me = fbconsole.get('/me')
my_id = me['id']


#status = fbconsole.post('/me/feed', {'message':'T2'})
#print "THIS IS THE FUCKING ID RIGHT HERE %s" % status['id']




#status = fbconsole.post('/me/feed', {'message':'Test from remote'})

statuses = fbconsole.fql("SELECT status_id,message FROM status WHERE uid=me()")
for status in statuses:
    s = fbconsole.get('/%s' % status['status_id'])
    print my_id+'_'+s['id']
    print s['message'] 
    print('#######################################################################################')
