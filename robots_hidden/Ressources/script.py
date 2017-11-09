import subprocess as cmd
import re


url = "http://10.13.0.205/.hidden/"
regex = 'href\=\"([^\.*].+)\"'
readTab = []

def cmd_output(com):
    pipe = cmd.Popen(com, stdout=cmd.PIPE, stderr=cmd.PIPE)
    output, errput = pipe.communicate()
    return output , errput

def search (url):
	com = ["curl", url]
	links = []
	subLinks = []
	for match in re.finditer(regex, cmd_output(com)[0]):
		link = match.group(1)
		links.append(link)
	for elem in links:
		if elem == "README":
			retCMD = cmd_output(["curl", com[1] + elem])[0]
			readTab.append(retCMD)
			# if len(readTab) % 100 == 0:
			# 	print len(readTab)
			if re.match("\d+", retCMD):
				print com[1] + elem, " : ", retCMD
		else:
			search(com[1] + elem)

search(url)
print len(readTab)
