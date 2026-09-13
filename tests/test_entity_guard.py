import unittest

from demo.entity_guard import inspect


class EntityGuardTests(unittest.TestCase):
    def test_critical_amount_requires_confirmation(self):
        self.assertEqual(inspect("墊底費係三萬蚊").action, "CONFIRM_ENTITIES")

    def test_coverage_polarity_requires_clarification(self):
        self.assertEqual(inspect("保障定唔保障").action, "ASK_CLARIFICATION")

    def test_unknown_content_fails_closed(self):
        self.assertEqual(inspect("背景聲太大").action, "ASK_CLARIFICATION")

    def test_input_is_not_rewritten(self):
        text = "共同保險係百分之二十"
        inspect(text)
        self.assertEqual(text, "共同保險係百分之二十")


if __name__ == "__main__":
    unittest.main()
