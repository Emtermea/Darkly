import subprocess as cmd
import re


url = "http://10.11.200.194/.hidden/"


regex = 'href\=\"([^\.*].+)\"'

def cmd_output(com):
    pipe = cmd.Popen(com, stdout=cmd.PIPE, stderr=cmd.PIPE)
    output, errput = pipe.communicate()
    return output , errput

# print(cmd_output(com)[0])

def search (url):
	com = ["curl", url]
	links = []
	subLinks = []
	for match in re.finditer(regex, cmd_output(com)[0]):
		link = match.group(1)
		links.append(link)
	# on recupere tous les premiers liens a check
	# on les formatte pour cmd_output
	for elem in links:
		elemUrl = ["curl", com[1] + elem]
		# print elemUrl
		#  cmd_output(elemUrl)[0]
		for subMatch in re.finditer(regex, cmd_output(elemUrl)[0]):
	 		subLink = elemUrl[1] + subMatch.group(1)
			print subLink


search(url)
