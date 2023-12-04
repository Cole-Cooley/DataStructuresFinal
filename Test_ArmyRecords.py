import unittest
from ArmyRecords import ArmyRecords
from CalculateBMI import CalculateBMI

class TestArmyRecords(unittest.TestCase):
    def setUp(self):
        self.army_records = ArmyRecords()

    def test_add_record(self):
        self.army_records.add_record("Private", "Doe", "John", 25, 72, 180, "20231201")
        records = self.army_records.get_records()
        self.assertEqual(len(records), 1)

    def test_print_by_last_name(self):
        self.army_records.add_record("Sergeant", "Smith", "Alice", 30, 68, 150, "20230515")
        self.army_records.add_record("Private", "Doe", "John", 25, 72, 180, "20231201")

        expected_result = [
            'Using Quick Sort to sort by Last Name',
            'Rank: Private, Last Name: Doe, First Name: John, Age: 25, Height: 72, Weight: 180, ETS: 20231201, BMI: 24.41',
            'Rank: Sergeant, Last Name: Smith, First Name: Alice, Age: 30, Height: 68, Weight: 150, ETS: 20230515, BMI: 22.80'
        ]

        self.assertPrintsByFunction(self.army_records.print_records_by_last_name, expected_result)

    def test_print_by_ets(self):
        self.army_records.add_record("Sergeant", "Smith", "Alice", 30, 68, 150, "20230515")
        self.army_records.add_record("Private", "Doe", "John", 25, 72, 180, "20231201")

        expected_result = [
            'Using Priority Queue to print by ETS Date',
            'Rank: Sergeant, Last Name: Smith, First Name: Alice, Age: 30, Height: 68, Weight: 150, ETS: 20230515, BMI: 22.80',
            'Rank: Private, Last Name: Doe, First Name: John, Age: 25, Height: 72, Weight: 180, ETS: 20231201, BMI: 24.41'
        ]

        self.assertPrintsByFunction(self.army_records.print_records_by_ets, expected_result)

    def assertPrintsByFunction(self, func, expected_output):
        import io
        from contextlib import redirect_stdout

        with io.StringIO() as buffer, redirect_stdout(buffer):
            func()

            output = buffer.getvalue().strip().split('\n')
            expected_output = [line.strip() for line in expected_output]

            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
