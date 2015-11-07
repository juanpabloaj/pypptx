#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from pptx.util import Cm

from pypptx import slides_from_yaml
from pypptx import picture_arguments


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


class TestPictureArguments(unittest.TestCase):

    def setUp(self):
        self.picture = {'left': 10, 'top': 20, 'path': 'some/path'}

    def test_empty_picture_dict(self):
        picture_list, picture_dict = picture_arguments({})
        self.assertEqual(picture_list, [])
        self.assertDictEqual(picture_dict, {})

    def test_return_list(self):

        expected_list = ['some/path', Cm(10), Cm(20)]
        picture_list, picture_dict = picture_arguments(self.picture)

        self.assertEqual(picture_list, expected_list)
        self.assertDictEqual(picture_dict, {})

    def test_with_width(self):
        picture = self.picture
        picture['width'] = 30
        picture['height'] = 40

        expected_dict = {'width': Cm(30), 'height': Cm(40)}
        picture_list, picture_dict = picture_arguments(picture)

        self.assertDictEqual(picture_dict, expected_dict)

    def test_ignore_fake_key(self):
        picture = self.picture
        picture['fake'] = 30

        picture_list, picture_dict = picture_arguments(picture)

        self.assertDictEqual(picture_dict, {})
