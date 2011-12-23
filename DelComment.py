#!/usr/bin/python
import sys
import fbconsole
fbconsole.APP_ID = '177876045644347'
fbconsole.AUTH_SCOPE = ['offline_access', 'publish_stream', 'read_stream']
fbconsole.authenticate()
id = sys.argv[1]
print('Deleting ID '+id)
fbconsole.delete('/'+id)



