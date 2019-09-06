=============
text-replace
=============

-----------
Description
-----------
A command line tool that goes to a specified path and recuresilvey replaces specified text with a different text to all files of a specified extension.

Installation
============

Clone the project 

.. code-block:: bash

    $ git clone https://github.com/SageHourihan/textreplace.git

Navigate to parent folder

.. code-block:: bash

    $ cd textreplace

Install setup.py with Python

.. code-block:: bash
    
    $ python setup.py install

Usage
=====

After installation run the program.

.. code-block:: bash

    $ text-replace
    $ File directory path:
    $ > Enter path name here
    $ Extension you are looking for (include period):
    $ > Enter extension here
    $ Text to search for:
    $ > Enter text here
    $ Text to replace it with:
    $ > Enter text here

After running your file(s) will be changed.

.. note:: 
    
    Text to search for and Text to replace is case sensitive.

.. warning:: 
    
    It is highly recommended to make a back up of your file(s) and store them in a different location. Program may mess up some rows of data if the file is a giant csv file (bigger than 5,000 rows).

License
=======

MIT 
