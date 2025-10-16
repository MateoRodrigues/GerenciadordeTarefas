import json
from pathlib import Path

class FileJson:
    def __init__(self, filepath = Path(__file__).parent.parent.parent / 'storage'/ 'data' / 'tarefas.json'):
        self.filepath = filepath
    def read(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
        