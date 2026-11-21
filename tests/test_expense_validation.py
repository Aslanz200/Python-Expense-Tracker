"""Targeted tests for the two verified input defects."""
import unittest

from expense_validation import validate_expense


class ExpenseValidationTests(unittest.TestCase):
    def test_valid_expense(self):
        self.assertEqual(validate_expense("2026-11-21", "100"), ("2026-11-21", 100.0))

    def test_negative_expense_rejected(self):
        with self.assertRaises(ValueError):
            validate_expense("2026-11-21", "-500")

    def test_zero_expense_rejected(self):
        with self.assertRaises(ValueError):
            validate_expense("2026-11-21", "0")

    def test_nonfinite_expenses_rejected(self):
        for amount in ("nan", "inf", "-inf"):
            with self.subTest(amount=amount), self.assertRaises(ValueError):
                validate_expense("2026-11-21", amount)

    def test_impossible_date_rejected(self):
        with self.assertRaises(ValueError):
            validate_expense("2026-99-99", "50")

    def test_invalid_calendar_day_rejected(self):
        with self.assertRaises(ValueError):
            validate_expense("2026-02-29", "50")

    def test_valid_leap_day(self):
        self.assertEqual(validate_expense("2024-02-29", "50"), ("2024-02-29", 50.0))

    def test_date_format_rejected(self):
        with self.assertRaises(ValueError):
            validate_expense("2026-1-2", "50")


if __name__ == "__main__":
    unittest.main()
