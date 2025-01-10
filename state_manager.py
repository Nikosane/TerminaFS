import json

class StateManager:
    def __init__(self, state_file):
        self.state_file = state_file

    def save_state(self, file_system):
        with open(self.state_file, "w") as f:
            json.dump(file_system.root, f)

    def load_state(self):
        try:
            with open(self.state_file, "r") as f:
                return FileSystem.from_dict(json.load(f))
        except FileNotFoundError:
            return None
