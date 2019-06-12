Creating widgets
================

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

Displaying text is important.  OpenCV uses the Hershey fonts


class Text(Node):
    options = dict(fontFace=cv.FONT_HERSHEY_SIMPLEX,
                   fontScale=1,
                   color=GREEN,
                   thickness=2,
                   lineType=cv.LINE_8,)

    def __init__(self, text='TextNode', **options):
        super().__init__(**options)
        self.set_class_options(options)
        self.text = text
        (w, h), b = self.get_size()
        self.size = np.array((w, h+b))
