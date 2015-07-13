import os
import re
import urllib

rootdir = '../_posts/'

def processCaption(caption):

    print caption

    alignment = "aligncenter"
    match = re.search("align=\"(.+?)\"",caption)
    if match and len(match.groups()) > 0:
        alignment = match.groups()[0]
    
    captionText = ""
    match = re.search("(<a.+?</a>)",caption)
    if match and len(match.groups()) > 0:
        image = match.groups()[0]
        match = re.search("</a> (.+?)\[/caption\]",caption)
        if match and len(match.groups()) > 0:
            captionText = match.groups()[0]        
    else:
        match = re.search("(<img .+?/>)",caption)
        if match and len(match.groups()) > 0:
            image = match.groups()[0]
        match = re.search("/> (.+?)\[/caption\]",caption)
        if match and len(match.groups()) > 0:
            captionText = match.groups()[0]

    out = ""
    out = out + "<div class=\"" + alignment + " panel panel-default\">"
    out = out + "<div class=\"panel-body text-center\">"
    out = out + image
    out = out + "</div>"
    if len(captionText) > 0:
        out = out + "<div class=\"panel-footer text-center\">"
        out = out + captionText
        out = out + "</div>"
    out = out + "</div>"

    print ""
    print out
    print "======"

    return out

def processPost(file):
    #print file
    allLines = open(file).read()

    match = re.search("(\[caption.+\[/caption\])", allLines)
    if match and len(match.groups()) > 0:
        caption = match.groups()[0]
        allLines = allLines.replace(caption, processCaption(caption))
    
    out = open(file, 'w')
    out.write(allLines)
    out.close()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        processPost(os.path.join(subdir, file))
        