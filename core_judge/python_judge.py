import os, subprocess, datetime, time
import signal
import sys
import filecmp





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
        i = 0
        while i < a.prob.testfiles:
                i += 1

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
			a.prob.details.total += 1
			a.prob.details.tle += 1
			a.prob.details.accuracy = a.prob.acc/a.prob.total
			a.prob.details.save()
			a.user.tot_sub += 1
			a.user.save()
			break

	        if a.status == "Time Limit Exceeded":
                    os.remove('out.txt')
                    os.remove('error.txt')
	            break
	        errors = errf.read()
	        if errors:
		    a.status = "Run Time Error"
		    a.save()
		    a.prob.details.total += 1
		    a.prob.details.rte += 1
		    a.prob.details.accuracy = a.prob.details.acc/a.prob.details.total
		    a.prob.details.save()
		    a.user.tot_sub += 1
		    a.user.save()
                    os.remove('out.txt')
                    os.remove('error.txt')
                    break
	        out_file = out_files + a.prob.pid + str(i) + '.txt'
        
                if filecmp.cmp('out.txt',out_file):
                    os.remove('out.txt')
                    os.remove('error.txt')
                    continue
                else:
                    os.remove('out.txt')
                    os.remove('error.txt')
                    a.status = "Wrong Answer"
                    a.save()
                    a.prob.details.total += 1
                    a.prob.details.wa += 1
                    a.prob.details.accuracy = a.prob.details.acc/a.prob.details.total
                    a.prob.save()
                    a.user.tot_sub += 1
                    a.user.save()
                    break
        if i == a.prob.testfiles:
                a.prob.details.total += 1
                a.prob.details.acc += 1
                a.prob.details.accuracy = a.prob.details.acc/a.prob.details.total
                a.prob.details.save()
                x = Submission.objects.filter(user = a.user,status = "Accepted")
                if not x:
                    a.user.points += 1

                a.user.tot_sub += 1
                a.user.points += 1
                a.user.succ_sub += 1
                a.user.save()
                a.status = "Accepted"
                a.save()
                continue

       


	
	
		






