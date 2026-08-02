import json
from pathlib import Path


class EventLog:

    def __init__(self):

        self.path = Path("storage/event_logs/events.jsonl")

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    async def append(self, event):

        with open(
            self.path,
            "a",
            encoding="utf-8",
        ) as f:

            f.write(
                json.dumps(
                    event,
                    ensure_ascii=False,
                )
            )

            f.write("\n")

    async def read(self):

        if not self.path.exists():
            return []

        records = []

        with open(
            self.path,
            "r",
            encoding="utf-8",
        ) as f:

            for line in f:
                records.append(
                    json.loads(line)
                )

        return records

    async def clear(self):

        self.path.write_text(
            "",
            encoding="utf-8",
        )


event_log = EventLog()
