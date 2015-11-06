pypptx
======

.. image:: https://travis-ci.org/juanpabloaj/pypptx.svg?branch=master
    :target: https://travis-ci.org/juanpabloaj/pypptx

Create a pptx from a yaml file.

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
        - title: second title
          text: more text
          images:
            - path: images/blue.jpg
              top: 7
              left: 4
              height: 5
            - path: images/blue.jpg
              top: 5
              left: 10

This repository have a yaml file called example.yaml with a example of the input syntax.

Why?
----

Some people prefer usage a pptx, in this case I prefer write a plain text to generate the pptx.
