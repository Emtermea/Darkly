import subprocess as cmd
import re

com = ["curl", "http://10.12.1.106/.hidden/"]


def cmd_output(com):
    pipe = cmd.Popen(com, stdout=cmd.PIPE, stderr=cmd.PIPE)
    output, errput = pipe.communicate()
    return output , errput


print(cmd_output(com)[0])
for elem in cmd_output(com)[0]:
	link = re.search("\".+\"", elem)
