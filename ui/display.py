class Display:

    def show(

        self,

        habits,

        stats

    ):

        print()

        print("Habit Tracker\n")

        for habit in habits:

            mark = "✔" if habit["completed"] else "✖"

            print(

                f"{mark} {habit['name']}"

            )

        print()

        print(

            f"Completed: {stats['completed']}"

        )

        print(

            f"Total: {stats['total']}"

        )

        print(

            f"Success Rate: {stats['percentage']}%"

        )
