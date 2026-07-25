class Statistics:

    def build(

        self,

        habits,

        tracker

    ):

        return {

            "total": len(habits),

            "completed": tracker.completed(habits),

            "percentage": tracker.percentage(habits)

        }
