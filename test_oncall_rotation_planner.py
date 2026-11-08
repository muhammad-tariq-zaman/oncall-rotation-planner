import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import plan

from datetime import date
def row(p, start):
    return {"person": p, "week_start": start}

class TestOnCall(unittest.TestCase):
    def test_on_call(self):
        on_call, _ = plan([row("Ali", "2026-11-02"), row("Sara", "2026-11-09")], date(2026, 11, 5), 2)
        self.assertEqual(on_call, "Ali")
    def test_second_week(self):
        on_call, _ = plan([row("Ali", "2026-11-02"), row("Sara", "2026-11-09")], date(2026, 11, 10), 2)
        self.assertEqual(on_call, "Sara")
    def test_no_match(self):
        on_call, _ = plan([row("Ali", "2026-11-02")], date(2026, 12, 25), 2)
        self.assertIsNone(on_call)
    def test_upcoming_lists_weeks(self):
        _, upcoming = plan([row("Ali", "2026-11-02"), row("Sara", "2026-11-09")], date(2026, 11, 5), 2)
        self.assertEqual(len(upcoming), 2)
