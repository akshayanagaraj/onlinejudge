import os, subprocess, datetime, time
import signal
import sys





base_dir = '/home/aswin/Documents/Aptana/judge'
media_dir = base_dir + '/media'

sub_files = media_dir + '/submissions/'
in_files = media_dir + '/infiles/'
out_files = media_dir + '/outfiles/'

sys.path.append(base_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'judge.settings'


from problems.models import Submission

sub_list = Submission.objects.filter(status='waiting',language='py')


for a in sub_list: 
	a.status = 'Processing'
	a.save()

	code_file = sub_files+ str(a.sid)+'.py'
	cmd = 'python ' + code_file
	for i in range(1,a.prob.testfiles+1):

		in_file = in_files + a.prob.pid + str(i) + '.txt'
		inf = open(in_file,'r')
		outf = open('out.txt','w')
		errf = open('err.txt','w')
		p = subprocess.Popen([cmd],stdin=inf,stdout=outf,stderr=errf)
        time_taken = 0.0
       	while p.poll() is None:
		time.sleep(0.1)
		time_taken += 0.1
		if time_taken > a.prob.time_limit:
			os.kill(p.pid,signal.SIGKILL)
			os.waitpid(-1,os.WNOHANG)
			os.remove('out.txt')
			a.status = "Time Limit Exceeded"
			a.save()
			a.prob.total += 1
			a.prob.tle += 1
			a.prob.accuracy = a.prob.acc/a.prob.total
			a.prob.save()
			a.user.total_sub += 1
			a.user.save()
			break

	if a.status == "Time Limit Exceeded":
		continue
	out_file = out_files + a.prob.pid + str(i) + '.txt'
	errors = errf.read()
	if errors:
		a.status = "Run Time Error"
		a.save()
		a.prob.total += 1
		a.prob.rte += 1
		a.prob.accuracy = a.prob.acc/a.prob.total
		a.prob.save()
		a.user.total_sub += 1
		a.user.save()

	
	
		






