# -*- coding: utf-8 -*-
"""
Money class unittests
"""
import unittest

from money import Money
from . import mixins


class TestMoneyInstantiation(mixins.InstantiationMixin, unittest.TestCase):
    def setUp(self):
        self.MoneyClass = Money


class TestMoneyClass(mixins.ClassMixin, unittest.TestCase):
    def setUp(self):
        self.money = Money('2.99', 'XXX')


class TestMoneyRepresentations(mixins.RepresentationsMixin, unittest.TestCase):
    def setUp(self):
        self.money = Money('1234.567', 'XXX')


class TestMoneyFormatting(mixins.FormattingMixin, unittest.TestCase):
    def setUp(self):
        self.money = Money('-1234.567', 'USD')


class TestMoneyParser(mixins.ParserMixin, unittest.TestCase):
    def setUp(self):
        self.MoneyClass = Money


class TestMoneyNumericOperations(mixins.NumericOperationsMixin, unittest.TestCase):
    def setUp(self):
        self.MoneyClass = Money


class TestMoneyUnaryOperationsReturnNew(mixins.UnaryOperationsReturnNewMixin, unittest.TestCase):
    def setUp(self):
        self.money = Money('2.99', 'XXX')


class TestMoneyLeftmostTypePrevails(mixins.LeftmostTypePrevailsMixin, unittest.TestCase):
    def setUp(self):
        self.MoneyClass = Money
        self.money = self.MoneyClass('2.99', 'XXX')
        self.MoneySubclass = type('MoneySubclass', (self.MoneyClass,), {})
        self.other_money = self.MoneySubclass('2.99', 'XXX')


class TestMoneySplit(unittest.TestCase):
    def test_split(self):
        self.assertEqual(Money('10.00', 'USD').split(3), [Money('3.34', 'USD'), Money('3.33', 'USD'), Money('3.33', 'USD')])
        self.assertEqual(Money('9.9999999999', 'USD'), sum(Money('9.9999999999', 'USD').split(7)))
