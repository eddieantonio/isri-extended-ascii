***********************************************
extended_ascii - convert UTF-8 → Extended ASCII
***********************************************

**DEPRECATED!** Use `isri-ocr-evauation-tools 6.0`__ with built-in support for UTF-8.

.. __: https://github.com/eddieantonio/isri-ocr-evaluation-tools

Converts UTF-8 text to extended ASCII and back again.

------------------
Install (Homebrew)
------------------

.. code-block:: bash

    $ brew tap eddieantonio/eddieantonio
    $ brew install extended_ascii

-------------
Install (pip)
-------------

.. code-block:: bash

    $ [sudo] pip install extended_ascii

============================
Converting to Extended ASCII
============================

.. code-block:: bash

    $ extended_ascii < input > output

==============================
Converting from Extended ASCII
==============================

.. code-block:: bash

    $ to_utf8 < input > output


=======
License
=======

© 2015 Eddie Antonio Santos. MIT Licensed.
