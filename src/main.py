#import flet as ft
#from views.pages.pagemain import main
import json
from repository.filejson import FileJson
from pathlib import Path
fljson = FileJson()
data = fljson.read()
for item in data:
    for key,value in item.items():
        print(f'{key}: {value}')
    print('-'*30)

#ft.app(target=main)
