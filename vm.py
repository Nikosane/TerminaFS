import os
from file_system import FileSystem
from state_manager import StateManager
from commands import CommandHandler

def main():
    state_file = "vm_state.json"
    state_manager = StateManager(state_file)
    file_system = state_manager.load_state() or FileSystem()
    command_handler = CommandHandler(file_system)

    print("Welcome to the VM! Type 'help' for a list of commands.")
    while True:
        try:
            command = input(f"{file_system.current_path}> ").strip()
            if command == "exit":
                state_manager.save_state(file_system)
                print("VM state saved. Goodbye!")
                break
            command_handler.handle(command)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
