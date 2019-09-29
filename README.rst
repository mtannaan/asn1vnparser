============
asn1vnparser
============


.. image:: https://img.shields.io/pypi/v/asn1vnparser.svg
        :target: https://pypi.python.org/pypi/asn1vnparser

.. image:: https://img.shields.io/travis/mtannaan/asn1vnparser.svg
        :target: https://travis-ci.org/mtannaan/asn1vnparser

.. image:: https://readthedocs.org/projects/asn1vnparser/badge/?version=latest
        :target: https://asn1vnparser.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Parses ASN.1 value notation into a Python object or JSON without requiring its ASN.1 schema.


* Free software: MIT license
* Documentation: https://asn1vnparser.readthedocs.io.


Features
--------

* Parsing ASN.1 value notation into a Python object, or a JSON string
* No ASN.1 Schema Required

Limitations
-----------

* Since Knowledge of schema is not used, misdetection of ASN.1 types can occur; see Translations section.
* Some ASN.1 types and grammars are not supported; see grammar.py.

Translations
------------

Performs the following type translations:

==========  ===========  =========
ASN.1 Type  Python Type  JSON Type
==========  ===========  =========
xx          yy           zz
==========  ===========  =========

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
