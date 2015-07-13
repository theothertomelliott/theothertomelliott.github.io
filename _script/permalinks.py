import os
import re
import urllib

rootdir = '../_posts/'

titlesByNode = {}

def testNodeNumber(nodeNum, title):
    if len(titlesByNode) > nodeNum and titlesByNode[nodeNum]:
        return title == titlesByNode[nodeNum]

    link = "http://www.telliott.io/node/" + str(nodeNum)
    f = urllib.urlopen(link)
    match = re.search("<title>(.+) \|", f.read())
    if match:
        titlesByNode[nodeNum] = match.groups()[0].replace('&amp;',"&").replace("&#8217;","'").replace("&#8211;","-").replace("&#8221;","\"").replace("&#8220;","\"").replace("&#8230;","...").strip()
    return title == titlesByNode[nodeNum]

def processPost(nodeNum, file):
    print file
    for i, line in enumerate(open(file)):
    	for match in re.finditer("published: false", line):
            # Skip this post
            print "Skipping post as not published"
            return nodeNum
        for match in re.finditer("title: (.*)", line):
            title = match.groups()[0].replace("''","'").strip("'")
    if not title:
        print "NO TITLE!"


    i = 0
    while not testNodeNumber(i,title):
    	i = i + 1

    link = "http://www.telliott.io/node/" + str(i)
    print link

    allLines = open(file).read
    allLines.replace("published: true", "published: true\npermalink: /node/" + str(i))
    out = open(file, 'w')
    out.write(allLines)   

    if i < nodeNum:
    	return nodeNum + 1
    else:
    	return i + 1

for subdir, dirs, files in os.walk(rootdir):
    nodeNum = 0
    for file in files:
        nodeNum = processPost(nodeNum, os.path.join(subdir, file))
        