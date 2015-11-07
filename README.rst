pypptx
======

.. image:: https://travis-ci.org/juanpabloaj/pypptx.svg?branch=master
    :target: https://travis-ci.org/juanpabloaj/pypptx

Create a pptx from a `yaml <http://www.yaml.org/spec/1.2/spec.html#Preview>`_ file.

Install
-------

.. code-block:: bash

    pip install pypptx

Usage:
------

To generate the pptx from a yaml file

.. code-block:: bash

    pptx file.yaml

Input yaml example

.. code-block:: yaml

    slides:
        - title: first title
          text: some text
          layout: 0
        - title: second title
          text: more text
          layout: 1
          images:
            - path: images/blue.jpg
              top: 7
              left: 4
              height: 5
            - path: images/blue.jpg
              top: 5
              left: 10
        - title: third slide
          text: with the previous layout

This repository have a yaml file called example.yaml with a example of the input syntax.

List the layouts ids to use in yaml file

.. code-block:: bash

    pptx -l
    0 Title Slide
    1 Title and Content
    ...


With the layout id select which use

.. code-block:: yaml

    ...
    - title: title
      text: subtitle
      layout: 0
    - title: Other slide
      text: with other layout
      layout: 1
    ...


Why?
----

Some people prefer usage a pptx, in this case I prefer write a plain text to generate the pptx.

Particularly, set the position of a set of pictures in a lot of slides is very tedious with the mouse.

Contributing
------------

1. Fork the `repository <https://github.com/juanpabloaj/pypptx>`_ on GitHub.
2. Make a branch off of master and commit your changes to it.
3. Run the tests with ``tox``
4. Submit a Pull Request to the master branch on GitHub.
