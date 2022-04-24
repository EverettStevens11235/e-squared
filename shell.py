from src.main import *
from json import load as jread
data = jread(open('src/settings/settings.json','r'))
print(data['TopText'])
while True:
    b = str(input(data['Prefix']))
    main(b)