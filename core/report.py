from pathlib import Path


class Report:

    def save(self, history, filename):

        file = Path(filename)

        with file.open(
            "w",
            encoding="utf8"
        ) as f:

            f.write("Habit Report\n")
            f.write("=================\n\n")

            for item in history.records:

                status = "Done" if item["completed"] else "Missed"

                f.write(
                    f"{item['habit']} - {status}\n"
                )

            f.write("\n")

            f.write(
                f"Completion: {history.completion_rate()}%"
            )
