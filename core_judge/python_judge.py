import os, subprocess, datetime, time
import signal
import sys



sys.path.append('/home/aswin/Documents/Aptana Studios Workspace')
os.environ['DJANGO_SETTINGS_MODULE'] = 'judge.settings'

from users.models import OjUser
from problems.models import Problem, Submission

sub_list = Submission.objects.filter(status='waiting',language='py')

for a in sub_list: 
	infile = str(a.sid)+'.py'
	cmd = 'python '+infile
	print cmd
	f = open('out.txt','w')
	p = subprocess.Popen([cmd],stdin=None,stdout=f,shell=True,stderr=f)
	start = datetime.datetime.now()
	time_taken = 0
	while p.poll() is None:
		time.sleep(0.1)
		now = datetime.datetime.now()
		if (now-start).seconds >= 3:
			
			os.kill(p.pid,signal.SIGKILL)
			os.waitpid(-1,os.WNOHANG)
			os.remove('out.txt')
			print "Timed out"
			break
		
		
			









