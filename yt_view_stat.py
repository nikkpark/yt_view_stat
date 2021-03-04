import csv


with open ("titles.dump", "r") as title_list:
    titles = title_list.read()

with open("playlist_info.dump", "r") as yt:
    data  = yt.read()

title_set = titles.split('\n')
data_set = data.split(',')
cleared_data_set = []

for word in data_set:
    if "view_count" in word:
        cleared_data_set.append(word[15:])

result = 0
for i in cleared_data_set:
    result += int(i)

csv_arr = []
for item in range(len(cleared_data_set)):
    csv_arr.append([title_set[item], cleared_data_set[item]])

# cp1251 for windows, utf-8 for other oses
with open ('youtubchik_epta.csv', 'w', encoding='cp1251') as w_file:
    file_writer = csv.writer(w_file, delimiter = ';')
    file_writer.writerows(csv_arr)


# debug
#for num in range(len(cleared_data_set)):
#   print(num+1, " ", title_set[num], " : ", cleared_data_set[num])
#
#for i in csv_arr:
#    print(i)
#
#
#print(result)
