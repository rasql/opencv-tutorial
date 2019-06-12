Widgets
=======

A widget is a control element in a graphial user interface.
The trackbar is the only native widget OpenCV has. In this section we
are going to add:

* Text
* Button
* Listbox
* Entry
* Spinbox


Trackbar
--------

The only GUI element OpenCV provides is a trackbar. This is an example
to add a trackbar to the Window and call the trackbar callback function::

    class Demo(App):
        def __init__(self):
            super().__init__()

            Window()
            Text('Trackbar')
            cv.createTrackbar('x', App.win.win, 50, 100, self.trackbar)
                
        def trackbar(self, pos):
            print(pos)

.. image:: widget1.*

Text
----

Displaying text is important.  OpenCV uses the Hershey fonts::

    class Text(Node):
        options = dict(fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=GREEN,
                    thickness=2,
                    lineType=cv.LINE_8,
                    bottomLeftOrigin=False)

        def __init__(self, text='Text', **options):
            super().__init__(**options)
            self.set_class_options(options)
            self.text = text
            (w, h), b = self.get_size()
            self.size = np.array((w, h+b))

Font scale
^^^^^^^^^^

The size of the font is given to the text as the ``fontScale`` argument.
In the example below we display 4 different scales::

    for scale in (0.5, 1, 2, 3):
        text = 'fontScale={}'.format(scale)
        Text(text, fontScale=scale, thickness=1, color=YELLOW)

.. image:: text1.*

Font type
^^^^^^^^^

OpenCV uses the **Hershey fonts** which are a collection of fonts developped in 1967 
by Dr. Allen Vincent Herschey at the Naval Weapons Laboratory, to be rendered on 
early cathod ray tube displays [#]_.

.. [#] https://en.wikipedia.org/wiki/Hershey_fonts


.. autoclass:: text2.Demo

.. image:: text2.*

Font thickness
^^^^^^^^^^^^^^

The following code displays different thickness for the font::

        for t in (1, 2, 4, 8):
            text = 'thickness={}'.format(t)
            Text(text, thickness=t, color=YELLOW)

        Text('ABC', pos=(250, 20), fontScale=6, thickness=1, 
            fontFace=cv.FONT_HERSHEY_DUPLEX)

.. autoclass:: text3.Demo

.. image:: text3.*

Placing text inside a Node
^^^^^^^^^^^^^^^^^^^^^^^^^^

Text can be placed and grouped inside a node. The elements inside the 
encloser move together. In the exemple below we have two groups with 
3 text fields inside::

        Node()
        Text(level=1)
        Text()
        Text()

        Node(level=-1, pos=(200, 20))
        Text(level=1)
        Text()
        Text().parent.enclose_children()

.. autoclass:: text4.Demo

.. image:: text4.*

Button
------

Entry
-----

Combobox
--------

Listbox
-------



