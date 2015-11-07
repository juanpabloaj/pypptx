#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import yaml
import argparse
from pptx import Presentation
from pptx.util import Cm


def slides_from_yaml(document):

    load_yaml = yaml.load(document)
    if 'slides' in load_yaml.keys():
        return load_yaml['slides']


def add_images(slide, images):

    for image in images:

        keys = image.keys()
        if 'left' in keys and 'top' in keys and 'path' in keys:

            left = Cm(float(image['left']))
            top = Cm(float(image['top']))
            img_path = image['path']

            if 'height' in keys:

                height = Cm(float(image['height']))
                slide.shapes.add_picture(
                    img_path, left, top, height=height
                )
            else:
                slide.shapes.add_picture(img_path, left, top)


def generate_presentation(slides):

    prs = Presentation()
    use_layout = 1
    slide_layout = prs.slide_layouts[use_layout]

    for slide_info in slides:

        if 'layout' in slide_info.keys():
            use_layout = int(slide_info['layout'])

            if use_layout < len(prs.slide_layouts):
                slide_layout = prs.slide_layouts[use_layout]

        slide = prs.slides.add_slide(slide_layout)
        shapes = slide.shapes

        title_shape = shapes.title
        body_shape = shapes.placeholders[1]

        if 'title' in slide_info.keys():
            title_shape.text = slide_info['title']

        if 'text' in slide_info.keys():
            tf = body_shape.text_frame
            tf.text = slide_info['text']

        if 'images' in slide_info.keys():

            add_images(slide, slide_info['images'])

    return prs


def show_layouts():
    prs = Presentation()
    for i, layout in enumerate(prs.slide_layouts):
        print i, layout.name


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?', help='yaml file')
    parser.add_argument(
        '-l', '--layouts', help='List layouts ids', action='store_true'
    )

    args = parser.parse_args()

    if args.layouts:
        show_layouts()
        exit()

    file_name = args.file
    if not file_name:
        parser.print_help()
        exit()

    if file_name.endswith('.yml') or file_name.endswith('.yaml'):

        file_content = open(file_name).read()
        file_name = os.path.splitext(file_name)[0]
        slides = slides_from_yaml(file_content)

        pptx_name = '{}.pptx'.format(file_name)
        generate_presentation(slides).save(pptx_name)


if __name__ == '__main__':
    main()
