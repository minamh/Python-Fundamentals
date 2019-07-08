

from urllib.request import  urlopen
import sys


def fetch_words(url):
    with urlopen(url) as story:
        story_words=[]
        for line in story:
            line_words=line.split()
            for word in line_words:
              story_words.append(word.decode())
    return story_words


def print_items(story_words):
    for word in story_words:
        print(word)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__=='__main__':
     main(sys.argv[1])