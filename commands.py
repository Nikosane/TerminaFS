class CommandHandler:
    def __init__(self, file_system):
        self.file_system = file_system

    def handle(self, command):
        parts = command.split()
        cmd, args = parts[0], parts[1:]

        if cmd == "mkdir":
            self.file_system.mkdir(args[0])
        elif cmd == "touch":
            self.file_system.touch(args[0])
        elif cmd == "ls":
            self.file_system.ls()
        elif cmd == "cd":
            self.file_system.cd(args[0])
        # More commands...
        else:
            print(f"Unknown command: {cmd}")
