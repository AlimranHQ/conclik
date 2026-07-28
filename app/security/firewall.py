"""
Conclik Pilot AI
Version : 5.4.0
Module : Firewall
"""


class Firewall:

    BLOCKED_PATTERNS = [
        "rm -rf",
        "sudo ",
        "wget ",
        "curl ",
        "os.system",
        "subprocess",
        "__import__",
        "eval(",
        "exec(",
        "<script",
        "DROP TABLE",
        "DELETE FROM",
    ]

    def inspect(self, prompt: str) -> bool:

        text = prompt.lower()

        for pattern in self.BLOCKED_PATTERNS:
            if pattern.lower() in text:
                return False

        return True


firewall = Firewall()
