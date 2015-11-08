#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from pptx.util import Cm

from pypptx import slides_from_yaml
from pypptx import picture_arguments
from pypptx import is_number


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

    @unittest.skip('skip')
    def test_yaml_dont_have_slides(self):
        self.fail()


class TestPictureArguments(unittest.TestCase):

    def setUp(self):
        self.picture = {'left': 10, 'top': 20, 'path': 'some/path'}
        self.expected_list = ['some/path', Cm(10), Cm(20)]

    def test_empty_picture_dict(self):
        picture_list, picture_dict = picture_arguments({})
        self.assertEqual(picture_list, [])
        self.assertDictEqual(picture_dict, {})

    def test_return_list(self):

        picture_list, picture_dict = picture_arguments(self.picture)

        self.assertEqual(picture_list, self.expected_list)
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

    def test_left_is_not_number(self):
        picture = self.picture
        picture['left'] = '10'

        picture_list, picture_dict = picture_arguments(picture)
        self.assertEqual(picture_list, [])
        self.assertDictEqual(picture_dict, {})

    def test_top_is_not_number(self):
        picture = self.picture
        picture['top'] = '10'

        picture_list, picture_dict = picture_arguments(picture)
        self.assertEqual(picture_list, [])
        self.assertDictEqual(picture_dict, {})

    def test_width_is_not_number(self):
        picture = self.picture
        picture['width'] = '10'

        picture_list, picture_dict = picture_arguments(picture)
        self.assertDictEqual(picture_dict, {})

    def test_height_is_not_number(self):
        picture = self.picture
        picture['height'] = '10'

        picture_list, picture_dict = picture_arguments(picture)
        self.assertDictEqual(picture_dict, {})


class TestIsNumber(unittest.TestCase):

    def test_float_is_true(self):
        self.assertTrue(is_number(10.))

    def test_int_is_true(self):
        self.assertTrue(is_number(10))

    def test_string_is_false(self):
        self.assertFalse(is_number('a string'))
