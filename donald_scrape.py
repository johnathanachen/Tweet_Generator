import bs4 as bs
import re
from urllib.request import urlopen
from string import punctuation
from pathlib import Path

class Scrape():

    def __init__(self):
        self = self.scrape()

    def _get_transcript_html(self):
        """ Scrape site for transcript and returns all speech sections in a list """
        transcript_url = 'http://time.com/4912055/donald-trump-phoenix-arizona-transcript/'
        transcript_url_request = urlopen(transcript_url)
        transcript_html = transcript_url_request.read()
        transcript_html = transcript_html.decode('utf-8')
        transcript_list = bs.BeautifulSoup(transcript_html, "lxml").find_all('figure', attrs={"class":"blockquote"})
        dialouge_list = re.findall( '<p>TRUMP: (.*?)</p>', str(transcript_list), re.DOTALL)
        return dialouge_list

    def _write_to_text_file(self, dialouge_list):
        scraped_file = Path("transcript.txt")
        if scraped_file.is_file():
            f = open("transcript.txt","a+")
            for sentence in dialouge_list:
                f.write(sentence)
        else:
            f = open("transcript.txt","w+")
            for sentence in dialouge_list:
                f.write(sentence)

    def scrape(self):
        dialouge_list = self._get_transcript_html()
        self._write_to_text_file(dialouge_list)

Scrape()
