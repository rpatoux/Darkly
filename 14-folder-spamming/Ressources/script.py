import requests
import re
import sys

start = 'http://e1r10p8:8080/.hidden/'

def attack_dir(start):
    data = requests.get(start)
    readme = start + "README"
    readme = requests.get(readme)
    test = re.findall('\d+\w+', readme.content.decode('utf-8'))
    if test:
        print(test)
        print("url", start ,"flag:", readme.content.decode('utf-8'))
        sys.exit()
    else:
        print("[-]", readme.content.decode('utf-8'))
        all_files = re.findall(r'\w+/</a>', data.content.decode('utf-8'))
        for elem in all_files:
            attack_dir(start + elem.replace('</a>', ''))

if __name__ == "__main__":
    attack_dir(start)