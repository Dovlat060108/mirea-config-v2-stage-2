"""Entry point for the shell emulator."""
import sys
from shell import Shell


def main():
    """Initialize and run the current stage."""
    shell = Shell()
    success = True
    shell.repl()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
