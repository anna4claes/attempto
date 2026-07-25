class Exporter:

    def save(

        self,

        habits,

        stats,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                "Habit Report\n\n"

            )

            for habit in habits:

                mark = "[x]" if habit["completed"] else "[ ]"

                file.write(

                    f"{mark} {habit['name']}\n"

                )

            file.write("\n")

            file.write(

                f"Completed: {stats['completed']}\n"

            )

            file.write(

                f"Total: {stats['total']}\n"

            )

            file.write(

                f"Rate: {stats['percentage']}%\n"

            )
