# TerminaFS

## Overview
TerminaFS is a terminal-based virtual machine (VM) that simulates a file system. Users can create, manage, and navigate files and directories within an isolated environment. The state of the VM, including all files and folders, is saved upon exiting and restored when restarted, ensuring seamless continuity.

## Features
- **Terminal Interface**: Interact with the VM using terminal commands like `ls`, `cd`, `mkdir`, `touch`, `cat`, and `exit`.
- **In-Memory File System**: Simulates a hierarchical file structure stored in memory.
- **State Persistence**: Saves the file system state to disk on exit and reloads it on startup.
- **Isolation**: Files and directories created within the VM are only accessible from within the VM.

## How It Works
1. **File System**: The VM uses an in-memory representation of the file system, implemented as a tree structure.
2. **State Management**: On exit, the VM serializes its file system and saves it to a file. On startup, it deserializes the saved state.
3. **Command Handling**: A command handler interprets user input and executes corresponding file system operations.

## Requirements
- Python 3.8+

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Nikosane/terminafs.git
   cd terminafs
   ```
2. Install any required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the VM:
   ```bash
   python vm.py
   ```
2. Use the following commands to interact with the VM:

   | Command       | Description                                      |
   |---------------|--------------------------------------------------|
   | `ls`         | List files and directories in the current folder |
   | `cd <dir>`   | Change the current directory                     |
   | `mkdir <dir>`| Create a new directory                           |
   | `touch <file>`| Create a new file                                |
   | `cat <file>` | Display the contents of a file                   |
   | `rm <name>`  | Remove a file or directory                       |
   | `exit`       | Exit the VM and save its state                   |

3. Example interaction:
   ```plaintext
   Welcome to TerminaFS! Type 'help' for a list of commands.
   vm:/> mkdir docs
   vm:/> touch hello.txt
   vm:/> ls
   docs
   hello.txt
   vm:/> exit
   VM state saved. Goodbye!
   ```

## Roadmap
- Implement file content editing commands (e.g., `edit`).
- Add support for file permissions.
- Enhance error handling for invalid commands.
- Introduce user authentication for multi-user support.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Inspired by the need for lightweight, terminal-based file system simulations for learning and experimentation.

---

Enjoy using **TerminaFS**! If you encounter any issues or have suggestions for improvement, feel free to open an issue in the repository.
