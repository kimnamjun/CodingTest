def remove_sym(s):
    idx = 1
    while idx < len(s):
        if s[idx] == '#':
            s = s[:idx - 1] + s[idx - 1].lower() + s[idx + 1:]
        else:
            idx += 1
    return s


def solution(m, musicinfos):
    m = remove_sym(m)

    playlist = list()
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        playtime = int(end[0:2]) * 60 + int(end[3:5]) - int(start[0:2]) * 60 - int(start[3:5])
        melody = remove_sym(melody)

        play = melody * ((playtime + len(melody) - 1) // len(melody))
        playlist.append([play[:playtime], title])

    music = list()
    for play, title in playlist:
        if play.find(m) != -1:
            music.append([play, title])
    music.sort(key=lambda x: -len(x[0]))

    return music[0][1] if music else '(None)'