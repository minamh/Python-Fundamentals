
#from urllib.request import urlopen
import urllib.request
with urllib.request.urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words=[]
    for line in story:
        line_words=line.split()
        for word in line_words:
            story_words.append(word.decode())

print(story_words)