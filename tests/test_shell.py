"""Prototype command parsing, argument validation and REPL behavior."""

import contextlib
import io
import unittest
from unittest.mock import patch

from shell import Shell, parse


class ShellTests(unittest.TestCase):
    """Check actual command results, not just command registration."""

    def test_parser(self):
        """Whitespace is split; quotes and variables stay literal."""
        self.assertEqual(parse('  ls  $HOME "a b" '),
                         ["ls", "$HOME", '"a', 'b"'])

    def test_prompt(self):
        """Username and hostname come from the host OS."""
        with patch("shell.getpass.getuser", return_value="student"):
            with patch("shell.socket.gethostname", return_value="host"):
                self.assertEqual(Shell().prompt(), "student@host:~$ ")

    def test_stub(self):
        """The first-stage stub shows command name and arguments."""
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertTrue(Shell().execute("ls /tmp"))
        self.assertEqual(output.getvalue(), "ls: ['/tmp']\n")

    def test_unknown_and_arguments(self):
        """Errors return failure and do not crash the session."""
        shell = Shell()
        with contextlib.redirect_stdout(io.StringIO()):
            for command in ("bad", "ls a b", "cd -z", "exit a"):
                self.assertFalse(shell.execute(command))
        self.assertTrue(shell.running)

    def test_exit_and_blank(self):
        """Empty input is harmless; exit terminates."""
        shell = Shell()
        self.assertTrue(shell.execute(" "))
        self.assertTrue(shell.execute("exit"))
        self.assertFalse(shell.running)

    def test_repl(self):
        """The interactive loop accepts commands and stops after exit."""
        shell = Shell()
        with patch("builtins.input", side_effect=["ls", "exit"]):
            with contextlib.redirect_stdout(io.StringIO()):
                shell.repl()
        self.assertFalse(shell.running)
