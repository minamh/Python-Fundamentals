from urllib.request import  urlopen


def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words=[]
        for line in story:
            line_words=line.split()
            for word in line_words:
              story_words.append(word.decode())

    for word in story_words:
        print(word)

print(__name__)
#fetch_words()