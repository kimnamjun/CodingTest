import re

def solution(word, pages):
    word = word.lower()

    table = dict()
    for page in pages:
        page = page.replace('\n', ' ').lower()
        x0 = re.search('<meta property="og:url" content="https://([^"]*)"/>', page).groups()[0]
        x1 = re.search('<body>(.*)</body>', page).groups()[0]
        x2 = re.split('<[^>]*>', x1)
        x3 = re.split('[^a-z]', ' '.join(x2))
        x4 = sum([1 for x in x3 if x == word])
        x5 = re.findall('<a href="https://([^"]*)">', page)
        table[x0] = {'url': x0, 'base_score': x4, 'external_links': x5, 'link_score': 0}

    for key in table:
        for url in table[key]['external_links']:
            if url in table:
                table[url]['link_score'] += table[key]['base_score'] / len(table[key]['external_links'])

    max_matching_score_index = 0
    max_matching_score = 0
    for idx, key in enumerate(table):
        table[key]['matching_score'] = table[key]['base_score'] + table[key]['link_score']
        if table[key]['matching_score'] > max_matching_score:
            max_matching_score_index = idx
            max_matching_score = table[key]['matching_score']

    return max_matching_score_index