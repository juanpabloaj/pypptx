#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from pypptx import slides_from_yaml

class TestSlides(unittest.TestCase):

    def test_slides_from_yaml(self):
        yaml = (
            'slides:\n'
            '    - title: Title one\n'
            '      text: first text\n'
            '    - title: Title two\n'
            '      text: second text\n'
        )
        expected_list = [
            {'text': 'first text', 'title': 'Title one'},
            {'text': 'second text', 'title': 'Title two'}
        ]

        self.assertEqual(expected_list, slides_from_yaml(yaml))
