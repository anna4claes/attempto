import unittest

from core.statistics import Statistics


class StatisticsTests(unittest.TestCase):

    def test_completion(self):

        stats = Statistics()

        stats.add(True)
        stats.add(True)
        stats.add(False)

        self.assertEqual(
            stats.completed,
            2,
        )

    def test_percentage(self):

        stats = Statistics()

        stats.add(True)
        stats.add(False)

        self.assertEqual(
            stats.percentage(),
            50,
        )


if __name__ == "__main__":
    unittest.main()
