from unittest import TestCase
from quantities.length import to_millimeters
from quantities.length import from_millimeters


class ToMillimetersTest(TestCase):

    def test_should_convert_to_millimeters_based_on_factor(self):
        assert to_millimeters(8, 10) == 80


class FromMillimetersTest(TestCase):

    def test_should_convert_from_100_millimeters_given_conversion_factor_of_10(self):
        assert from_millimeters(100, 10.0) == 10.0

    def test_should_convert_from_100_millimeters_given_conversion_factor_of_1000(self):
        assert from_millimeters(100, 1000.0) == 0.1
