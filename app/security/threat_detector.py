"""
Conclik Pilot AI
Version : 5.4.1
Module : Threat Detector
"""


class ThreatDetector:

    THREATS = [

        "ignore previous instructions",
        "ignore all instructions",

        "system prompt",
        "reveal prompt",
        "show prompt",
        "hidden prompt",
        "show hidden prompt",
        "show system prompt",
        "internal prompt",
        "secret prompt",

        "developer mode",
        "jailbreak",
        "bypass security",
        "forget previous",
        "disable firewall",
        "act as root",

    ]

    def detect(self, prompt: str) -> bool:

        text = prompt.lower()

        for threat in self.THREATS:
            if threat in text:
                return False

        return True


threat_detector = ThreatDetector()
