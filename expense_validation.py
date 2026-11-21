"""Pure input validation for expense entries."""
from datetime import datetime
import math


def validate_expense(date_text, amount_text):
    """Return (ISO date, positive finite amount) or raise ValueError."""
    date_text = date_text.strip()
    try:
        parsed = datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("Enter a valid date in YYYY-MM-DD format.") from exc
    if parsed.strftime("%Y-%m-%d") != date_text:
        raise ValueError("Enter a valid date in YYYY-MM-DD format.")

    try:
        amount = float(amount_text)
    except (ValueError, TypeError) as exc:
        raise ValueError("Enter a valid positive expense amount.") from exc
    if not math.isfinite(amount) or amount <= 0:
        raise ValueError("Expense amount must be positive and finite.")
    return date_text, amount
