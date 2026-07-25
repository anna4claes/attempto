class Tracker:

    def completed(

        self,

        habits

    ):

        return sum(

            habit["completed"]

            for habit in habits

        )

    def percentage(

        self,

        habits

    ):

        if not habits:

            return 0

        return round(

            self.completed(habits)

            / len(habits)

            * 100

        )
