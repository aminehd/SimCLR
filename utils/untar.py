#!/usr/bin/python
import subprocess
import sys
import shlex


print("*" * 30)
print("untaring {}.tar:".format(sys.argv[2]))
command = "/bin/tar -xvf {}{}.tar -C {}".format(sys.argv[1], sys.argv[2],sys.argv[1][:-1])
print("command: ", command)

p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout:
    sys.stdout.write("\r%s" % line.decode("utf-8").rstrip())
    sys.stdout.write("\b")
    sys.stdout.flush()
    # if i >= 100:
    #     break
    # print(line.decode("utf-8").rstrip(), sep=' ', end='', flush=True)
    
print("")
print("Done untaring {}.tar".format(sys.argv[2]))
p.wait()
status = p.poll()

# untar("train")
# untar("validation")
# untar("test")