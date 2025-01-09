import time

class FileSystem:
    def __init__(self):
        self.root = {"type": "directory", "name": "/", "children": []}
        self.current_directory = self.root
        self.current_path = "/"

    def mkdir(self, name):
        for child in self.current_directory["children"]:
            if child["type"] == "directory" and child["name"] == name:
                raise ValueError(f"Directory '{name}' already exists.")
        self.current_directory["children"].append({"type": "directory", "name": name, "children": []})

    def touch(self, name):
        for child in self.current_directory["children"]:
            if child["type"] == "file" and child["name"] == name:
                raise ValueError(f"File '{name}' already exists.")
        self.current_directory["children"].append({"type": "file", "name": name, "content": "", "timestamp": time.time()})

    # More methods: ls, cd, rm, cat...
