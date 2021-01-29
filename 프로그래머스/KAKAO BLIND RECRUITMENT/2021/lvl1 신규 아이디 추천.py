import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^\\w\\-_.]', '', new_id)
    new_id = re.sub('\\.+', '.', new_id)
    new_id = re.sub('^\\.', '', new_id)
    new_id = re.sub('\\.$', '', new_id)
    new_id = new_id if new_id else 'a'
    new_id = new_id[:15]
    new_id = new_id if new_id[-1] != '.' else new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id