Histograms
==========

Histograms are

Grayscale histogram
-------------------

The ``calcHist`` function takes these arguments::

    cv.calcHist([img], channels, mask, bins, ranges)

* image list
* channel list
* mask
* the number of **bins**
* ranges, typically [0, 255]

.. image:: histogram1.png

.. literalinclude:: histogram1.py

:download:`histogram1.py<histogram1.py>`


Color histogram
---------------
.. image:: lego.png

Here is the histogram

.. image:: histogram2.png

.. literalinclude:: histogram2.py

:download:`histogram2.py<histogram2.py>`


Blurring
--------

.. image:: blur1.png

.. literalinclude:: blur1.py

:download:`blur1.py<blur1.py>`
