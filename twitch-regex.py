import re
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
print('----------------------------------------')
print(ch)
print('----------------------------------------')
for x in ch:
    print(x)

textfile.close()
input('----------------------------------------\nPress Enter to continue...')

#alt="(\S+)"\ssrc