from datetime import datetime


class History:

    def __init__(self):

        self.records = []

    def add(self, habit, completed):

        self.records.append({

            "habit": habit,

            "completed": completed,

            "timestamp": datetime.now()

        })

    def total(self):

        return len(self.records)

    def completed(self):

        return sum(
            1 for item in self.records
            if item["completed"]
        )

    def completion_rate(self):

        if not self.records:
            return 0

        return round(
            self.completed() /
            self.total() * 100,
            1,
        )
