import os
import re
import urllib

# Work on files in the Jekyll posts dir
# Expects to be run from the _script dir
rootdir = '../_posts/'

# Dictionary to store previously matched titles and nodes
titlesByNode = {}

# Test if a specified node number applies to the given title
# The test consists of pulling the HTML for the permalink of this node and comparing the page's title to the title that was passed in
def testNodeNumber(nodeNum, title):
    if len(titlesByNode) > nodeNum and titlesByNode[nodeNum]:
        return title == titlesByNode[nodeNum]

    link = "http://telliott.io/node/" + str(nodeNum)
    f = urllib.urlopen(link)
    match = re.search("<title>(.+) \|", f.read())
    if match:
        titlesByNode[nodeNum] = match.groups()[0].replace('&amp;',"&").replace("&#8217;","'").replace("&#8211;","-").replace("&#8221;","\"").replace("&#8220;","\"").replace("&#8230;","...").strip()
    print link + ": " + titlesByNode[nodeNum]
    return title == titlesByNode[nodeNum]

# Process the content of a given post and add a permalink
def processPost(file):

    # Extract the title from this post if available
    print file
    title = None
    for i, line in enumerate(open(file)):
    	for match in re.finditer("published: false", line):
            # Skip this post
            print "Skipping post as not published"
            return
        for match in re.finditer("title: (.*)", line):
            title = match.groups()[0].replace("''","'").strip("'")
    if not title:
        print "Skipping post as lacking a title"
        return

    # Test against stored nodes and live nodes on the web to identify the actual node number of this post
    # WARNING: If there is no live URL matching the title, this will run forever
    i = 0
    while not testNodeNumber(i,title):
    	i = i + 1

    # Create a permalink from the identified node number
    link = "http://www.telliott.io/node/" + str(i)
    print link

    # Add the permalink to this post
    allLines = open(file).read()
    allLines = allLines.replace("published: true", "published: true\npermalink: /node/" + str(i))
    out = open(file, 'w')
    out.write(allLines)
    out.close()

# Iterate over all post files (assume there are only posts in the rootdir)
# Process each post in turn to add a permalink
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        processPost(os.path.join(subdir, file))
        