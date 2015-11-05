#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import yaml
from pptx import Presentation


def slides_from_yaml(document):

    load_yaml = yaml.load(document)
    if 'slides' in load_yaml.keys():
        return load_yaml['slides']


def generate_presentation(slides):

    prs = Presentation()
    bullet_slide_layout = prs.slide_layouts[1]

    for slide_info in slides:

        slide = prs.slides.add_slide(bullet_slide_layout)
        shapes = slide.shapes

        title_shape = shapes.title
        body_shape = shapes.placeholders[1]

        title_shape.text = slide_info['title']

        tf = body_shape.text_frame
        tf.text = slide_info['text']

    return prs


def main():

    if len(sys.argv) > 1:

        file_name = sys.argv[1]

        if file_name.endswith('.yml') or file_name.endswith('.yaml'):

            file_content = open(file_name).read()
            file_name = os.path.splitext(file_name)[0]
            slides = slides_from_yaml(file_content)

            pptx_name = '{}.pptx'.format(file_name)
            generate_presentation(slides).save(pptx_name)


if __name__ == '__main__':
    main()