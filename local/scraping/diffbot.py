import requests

DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = '549f0747ef81c43f60aa6f95b5a5933a'

def get_article(article_url):
    # set request params for API request
    params = { 'token': DIFFBOT_DEV_TOKEN,
               'url': article_url,
               'discussion': 'false' }

    res = requests.get(DIFFBOT_API_URL, params) # hit the Diffbot API
    res_obj = res.json()['objects'][0]          # parse the response object

    return res_obj['text']                      # pull out the text

if __name__ == '__main__':
    import sys
    urls_file = open(sys.argv[1])
    output_file = open('corpus.txt', 'w')

    corpus = ''

    count = 0
    for line in urls_file:
        url = line.strip() # remove leading/trailing whitespace
        article = get_article(url)
        count += 1
        print(count)

        corpus += article

    output_file.write(corpus)
    print('Corpus saved to {}'.format(output_file.name))
