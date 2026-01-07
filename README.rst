.. image:: https://badge.fury.io/py/skosify.svg
   :target: https://badge.fury.io/py/skosify.svg    
.. image:: https://github.com/NatLibFi/Skosify/workflows/CI/badge.svg
   :target: https://github.com/NatLibFi/Skosify/actions
.. image:: https://readthedocs.org/projects/skosify/badge/?version=latest
   :target: http://skosify.rtfd.io/ 
.. image:: https://codecov.io/gh/NatLibFi/Skosify/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/NatLibFi/Skosify

Python script for converting to `SKOS <http://www.w3.org/2004/02/skos/>`_.

This program accepts a thesaurus-like vocabulary expressed as RDFS, OWL or
SKOS as input. It produces a clean SKOS representation, which attempts to
represent the input data losslessly using SKOS best practices. When given
SKOS as input, it will be cleaned up, validated and enriched to follow
the SKOS specification and related best practices.

Installation
============

Skosify requires Python 3.9+.

If you only want to use the command line interface it is suggested to install
with `uv tool <https://docs.astral.sh/uv/concepts/tools/>`_ 
or `pipx <https://pypa.github.io/pipx/>`_. 
Both simplify installing and managing python command line applications.

.. code-block:: console

    uv tool install skosify


or

.. code-block:: console

    pipx install skosify


Of course you also use pip to install as for any other Python package.

.. code-block:: console

    pip install --upgrade skosify


To help testing locally with multiple Python versions, a 
`tox <https://tox.wiki/>`_ configuration file is provided (tox.ini).

.. code-block:: console

    uv tool install tox

Execute `tox` in the root of the repo to run the full set of tests.
Optionally just run specific environments, for example only Python 3.12:

.. code-block:: console

    tox -e py312

The package can be built locally with any PEP517-conform build tool, for example 
`build <https://pypi.org/project/build/>`_, 
`uv build <https://docs.astral.sh/uv/concepts/build-backend/>`_
or `hatch <https://pypi.org/project/hatch/>`_.
Of course, you need to have the build tool installed. 
For example, to use hatch as in gh-actions, run:

.. code-block:: console

    uvx hatch build

This command uses `uvx <https://docs.astral.sh/uv/guides/tools/>`_
to run hatch with out installing it permanently.

Usage
=====

As command line script:

.. code-block:: console

    skosify myvoc.owl -o myvoc-skos.ttl --label "My Ontology"

This will read the file ``myvoc.owl`` in RDF/XML format and write SKOS file ``myvoc-skos.ttl`` in Turtle format, setting the name of the Concept Scheme to ``My Ontology``.

Run ``skosify --help`` for more usage information.

As Python library:

.. code-block:: python

    import skosify  # contains skosify, config, and infer

    voc = skosify.skosify('myontology.owl', label='My Ontology')
    voc.serialize(destination='myontology-skos.rdf', format='xml')

    rdf = Graph()
    rdf.parse('myontology.owl')
    config = skosify.config('owl2skos.cfg')
    voc = skosify.skosify(rdf, **config)

    skosify.infer.skos_related(rdf)
    skosify.infer.skos_topConcept(rdf):
    skosify.infer.skos_hierarchical(rdf, narrower=True)
    skosify.infer.skos_transitive(rdf, narrower=True)

    skosify.infer.rdfs_classes(rdf)
    skosify.infer.rdfs_properties(rdf)

See `the API Reference <http://skosify.readthedocs.io/en/latest/api.html>`_ for documentation of the public API of this module. Everything not listed there might change in a future version.

Additional documentation can be found `in the GitHub project wiki <https://github.com/NatLibFi/Skosify/wiki>`_


Additional scripts
==================

The `scripts` directory contains two additional scripts to be used together with Skosify:

* `skosify.cgi` a web application to use Skosify
* `sparqldump.py` a command line client to download RDF via a SPARQL endpoint

Author and Contributors
=======================

-  Osma Suominen
-  Jakob Voß
-  Dan Michael O. Heggø
-  Alex Kourijoki
-  David Linke

See also
========

See `background` for history, related works, publications etc.

.. background: docs/background.rst


