import re
import urllib.request
import random
from time import sleep

# Find all links on an artist's AZLyrics page
originalLyrics = open('lyrics.txt', 'w')
url = "https://www.azlyrics.com/a/artist.html"
artistHtml = urllib.request.urlopen(url)
artistHtmlStr = str(artistHtml.read())
links = re.findall('href="([^"]+)"', artistHtmlStr)

songLinks = []
for x in links:
    if "lyrics/artist" in x:
        x = x.replace("..", "")
        x = "https://www.azlyrics.com/" + x
        songLinks.append(x)

for x in songLinks:
    songHtml = urllib.request.urlopen(x)
    songHtmlStr = str(songHtml.read())
    split = songHtmlStr.split(
        'content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->', 1)
    split_html = split[1]
    split = split_html.split('</div>', 1)
    lyrics = split[0]
    lyrics = lyrics.replace('<br>', '\n')
    lyrics = lyrics.replace('\\', '')
    lyrics = lyrics.replace('\nn', '\n')
    lyrics = lyrics.replace('<i>', '')
    lyrics = lyrics.replace('</i>', '')
    lyrics = lyrics.replace('[Chorus]', '')
    originalLyrics.write(lyrics)
    sleep(random.randint(2, 10))
originalLyrics.close()
