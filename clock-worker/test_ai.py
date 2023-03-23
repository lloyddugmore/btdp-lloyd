import unittest
import moment

from ai import AI

class TestAIClass(unittest.TestCase):
    def test_ai_class(self):
        class MyClassMock(AI):
            def get_now(self):
                return moment.utc("2023-03-19")

        mocked_out = MyClassMock()
        # results = mocked_out.get_tomorrow_day(self);
        # self.assertEqual('According to AI, tomorrow is Monday', results)