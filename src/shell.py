"""Interactive UNIX-like shell with a deliberately simple space parser."""

import getpass
import socket


def parse(line):
    """Split a command by whitespace, without quotes or expansion."""
    return line.split()


class Shell:
    """Run commands and report user errors without leaving the REPL."""

    def __init__(self, vfs=None):
        """Register the commands provided by the current stage."""
        self.vfs = vfs
        self.cwd = "/"
        self.running = True
        self.commands = {"ls": self.stub, "cd": self.stub,
                         "exit": self.exit}
        self.active_command = ""

    def prompt(self):
        """Use the actual OS username and hostname in the prompt."""
        path = "~" if self.cwd == "/" else self.cwd
        return f"{getpass.getuser()}@{socket.gethostname()}:{path}$ "

    def execute(self, line):
        """Return success; display errors and keep the session usable."""
        words = parse(line)
        if not words:
            return True
        command, *args = words
        self.active_command = command
        try:
            if command not in self.commands:
                raise ValueError(f"неизвестная команда: {command}")
            result = self.commands[command](args)
            if result:
                print(result)
            return True
        except (ValueError, OSError, UnicodeError) as error:
            print(f"Ошибка: {error}")
            return False

    def stub(self, args):
        """Validate prototype ls/cd arguments and show their values."""
        if len(args) > 1 or any(arg.startswith("-") for arg in args):
            raise ValueError(f"использование: {self.active_command} [путь]")
        return f"{self.active_command}: {args}"

    def exit(self, args):
        """Stop the current shell; exit accepts no arguments."""
        if args:
            raise ValueError("использование: exit")
        self.running = False

    def repl(self):
        """Read commands until exit, EOF or keyboard interrupt."""
        while self.running:
            try:
                self.execute(input(self.prompt()))
            except (EOFError, KeyboardInterrupt):
                print()
                break
