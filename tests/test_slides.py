#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import pypptx


class TestSlides(unittest.TestCase):

    def test_slides(self):
        yaml = (
            'slides:\n'
            '    - title: Title one\n'
            '      text: first text\n'
            '    - title: Title two\n'
            '      text: second text\n'
        )
        ps = pypptx.PySlides(yaml)
        prs = ps.generate()
        results = [ s.shapes.title.text for s in prs.slides ]
        self.failUnlessEqual(results, [u'Title one', u'Title two'])

    def test_example_yaml(self):
        expectedResults = [u'Foo', u'Bar', u'Baz', u'Line Chart', u'Bar Chart', u'Pie Chart', u'An Image']
        with open('test.yaml', 'r') as h:
            yaml = h.read()
        ps = pypptx.PySlides(yaml)
        prs = ps.generate()
        results = [ s.shapes.title.text for s in prs.slides ]
        self.failUnlessEqual(results, expectedResults)


if __name__ == "__main__":
    unittest.main()
