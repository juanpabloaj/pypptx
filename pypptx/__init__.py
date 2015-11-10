#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import yaml
import argparse
import numbers
from pptx import Presentation
from pptx.util import Cm


def is_number(number):
    if isinstance(number, numbers.Real):
        return True
    else:
        return False


def write_yaml(yaml_name, yaml_content):
    with open(yaml_name, 'w') as out_yaml:
        yaml.safe_dump(
            yaml_content, out_yaml, encoding='utf-8',
            allow_unicode=True, indent=4
        )


def yaml_from_pptx(pptx_path):

    prs = Presentation(pptx_path)

    slides = []

    for slide in prs.slides:
        slide_content = {'title': slide.shapes.title.text}
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue

            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    pass

        slides.append(slide_content)

    yaml_content = {'slides': slides}

    return yaml_content


def slides_from_yaml(document):

    load_yaml = yaml.load(document)
    if 'slides' in load_yaml.keys():
        return load_yaml['slides']


def picture_arguments(picture):
    ''' arguments to generate a picture in shapes '''
    picture_list = []
    picture_dict = {}

    keys = picture.keys()

    if 'left' in keys and 'top' in keys and 'path' in keys:
        path, left, top = [picture[k] for k in ['path', 'left', 'top']]

        if is_number(left) and is_number(top):
            picture_list = [path, Cm(left), Cm(top)]

            for k in ['width', 'height']:
                if k in keys:
                    if is_number(picture[k]):
                        picture_dict[k] = Cm(picture[k])

    return picture_list,  picture_dict


def add_images(slide, images):

    for image in images:

        picture_list, picture_dict = picture_arguments(image)
        if picture_list != []:
            slide.shapes.add_picture(*picture_list, **picture_dict)


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
        print '{} created'.format(pptx_name)

    elif file_name.endswith('.pptx'):

        yaml_content = yaml_from_pptx(file_name)

        file_name = os.path.splitext(file_name)[0]
        yaml_name = '{}_generated.yaml'.format(file_name)

        write_yaml(yaml_name, yaml_content)
        print '{} created'.format(yaml_name)


if __name__ == '__main__':
    main()
