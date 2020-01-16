Basic shapes
============

In this section we going create classes to add basic shapes to an image:

* Marker
* Line
* Arrow
* Rectangle
* Circle
* Ellipse
* Polygon

Finding OpenCV attributes
-------------------------

OpenCV has 1912 attributes, which can be verified with the following command:

>>> len(dir(cv))
2190

We define a small function for matching this large attribute list
with a regular expression::

    def cv_dir(regex):
        atts = dir(cv)
        return [s for s in atts if re.match(regex, s)]

We use it to find the markers

>>> cv_dir('MARKER.*')
['MARKER_CROSS',
 'MARKER_DIAMOND',
 'MARKER_SQUARE',
 'MARKER_STAR',
 'MARKER_TILTED_CROSS',
 'MARKER_TRIANGLE_DOWN',
 'MARKER_TRIANGLE_UP']


Marker
------

We base the Marker class on the Node class. At first we set the options as 
class attribute of the Marker class::

    class Marker(Node):
        options = dict( color=GREEN,
                        markerType=cv.MARKER_CROSS,
                        markerSize=20,
                        thickness=1,
                        line_type=8)

Then we define the :meth:`__init__` method, which only has options. Four of them
(pos, size, gap, dir) are applied to Node, and the rest are specific to the Marker
class (color, markerType, markerSize, thickness, line_type). The method
:meth:`set_class_options` sets these options::

    def __init__(self, **options):
        super().__init__(**options)
        self.set_class_options(options)

We set the size to 20x20 which is the size of the markers. To better see the 
markers, we do not display the frame::

        self.size = np.array((20, 20))
        self.frame = False
        cv.imshow(self.win.win, self.img)

Finally we create the :meth:`draw` method::

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        x, y = pos + self.pos + (10, 10)
        cv.drawMarker(self.img, (x, y), **self.options)

.. image:: shape1.png

.. literalinclude:: shape1.py


https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html
