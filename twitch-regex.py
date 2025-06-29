import re
import json

ch = []

textfile = open('test.txt', 'r', encoding='utf8')
file_contents = textfile
#print(file_contents)

print('check is string number only\n----------------------------------------')
for line in file_contents:
    tempstring = re.findall('alt="(\S+)"\ssrc', line)
    #print(tempstring)

for _ch in tempstring:
    print(_ch.ljust(25), not _ch.isdigit())
    if not _ch.isdigit():
        ch.append(_ch)
        #print(ch)

#print('----------------------------------------')
#print(ch)
#print('----------------------------------------')
#for x in ch:
#    print(x)

textfile.close()




#with open("file.json", "w") as f:
#    json.dump([{"f_name": f_name, "l_name": l_name}], f)




toLongText = ""
for _ch in tempstring:
    if toLongText == "":
        toLongText = f'"{_ch}"'
    else:
        toLongText = f'{toLongText},"{_ch}"'

toLongText = (f'[{toLongText}]')

with open("Unwanted_list.txt", "w", encoding="utf-8") as outfile:
    outfile.write(toLongText)






#input('----------------------------------------\nPress Enter to continue...')

#alt="(\S+)"\ssrc