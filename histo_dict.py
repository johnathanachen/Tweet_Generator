import bs4 as bs
from urllib.request import urlopen
import re

def get_transcript_html():
    transcript_url = 'http://rickandmorty.wikia.com/wiki/Pilot/Transcript'
    transcript_url_request = urlopen(transcript_url)
    transcript_html = transcript_url_request.read()
    transcript_html = transcript_html.decode('utf-8')
    transcript_list = bs.BeautifulSoup(transcript_html, "lxml").find_all('div', attrs={"class":"poem"})
    dialouge_list = re.findall( '<b>Morty:</b>(.*?)<br/>', str(transcript_list), re.DOTALL)
    return dialouge_list

source_text = get_transcript_html()

def _get_words(source_text):
    word_list = []
    for sentence in source_text:
        word_list.append(sentence.split(' '))
    combined_word_list = [inner for outer in word_list for inner in outer]
    remove_unicode = [word.strip('\xa0') for word in combined_word_list]
    for word in remove_unicode:
        if "</i>" in word:
            remove_unicode.remove(word)
    for word in remove_unicode:
        if "<i>" in word:
            remove_unicode.remove(word)
    return remove_unicode

only_words = _get_words(source_text)

def histrogram(only_words):
    word_count = {}
    for word in only_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

histo_dict = histrogram(only_words)

def sort_histogram(histo_dict):
    value_list = histo_dict.values()
    list_values = list(value_list)
    list_values.sort()
    sorted_values = sorted(histo_dict, key=lambda x: histo_dict[x])
    for k in sorted_values:
        answer = "{} : {}".format(k, histo_dict[k])



sort_histogram(histo_dict)




get_transcript_html()
