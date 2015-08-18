from unittest import TestCase
from quantities.length import to_millimeters


class ToMillimetersTest(TestCase):

    def test_should_convert_to_millimeters_based_on_factor(self):
        assert to_millimeters(8, 10) == 80
