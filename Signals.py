#!/usr/bin/env python

import signal
def ctrl_handler(signum, frm) :
	print " You can't cannot kill me"

print "Installing signal handler..."
signal.signal(signal.SIGINT, ctrl_handler)
print "done"

while True :
	pass
