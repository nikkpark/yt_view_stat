import csv
import sys

import youtube_dl


def get_playlist_info(url):
    ydl_options = {}
    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        dump = ydl.extract_info(url, False)
    return dump


def get_views(data):
    data_set = []

    for i in range(len(data['entries'])):
        data_set.append([
            (data['entries'][i]['title']).replace('\xc2', ' '),
            data['entries'][i]['view_count'],
            'https://youtube.com/watch?v=' + data['entries'][i]['id']
        ])

    # cp1251 for windows, utf-8 for other oses
    filename = data['title'] + '.csv'
    with open(filename, 'w', encoding='cp1251') as w_file:
        file_writer = csv.writer(w_file, delimiter=';')
        # csv.field_size_limit(120)
        file_writer.writerows(data_set)


if __name__ == "__main__":
    url = sys.argv[1]
    get_views(get_playlist_info(url))
