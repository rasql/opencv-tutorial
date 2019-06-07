Introduction
============

In this section we look at the basic operations for displaying images in a window
and reacting to mouse and keyboard events.


Load, show and save an image
----------------------------

OpenCV is a library for doing image processing. We start this tutorial 
by opening a file, displaying it in a window and saving it with a different name.

First we import the OpenCV library ``cv2`` and give it the shortcut ``cv``::

    import cv2 as cv

Then we load an image from the current folder, and transform it to grayscale::

    # Load a color image in grayscale
    img = cv.imread('messi.jpg', cv.IMREAD_GRAYSCALE)

The function ``cv.imshow`` displays the image in a window called **image**. 
Then we save this grayscale image under the new name *messigray.png*::

    cv.imshow('image', img)
    cv.imwrite('messigray.png', img)

Without calling the ``cv.waitKey()`` no window is displayed. The parameter of this function is the number of 
miliseconds the function waits for a keypress. With a value of 0 the function waits indefinitely.
Once a key is pressed, the program advances to the last line and destroys all windows::

    cv.waitKey(0)
    cv.destroyAllWindows()

Clicking the *window close* button closes the window, but does not quit the program. 
After closing the window, a key press has no effect anymore and the only way to quit the program is by 
choosing **Quit** from the menu, or by pressing the shortcut **cmd+Q**.


Capturing live video
--------------------

To capture video we must create a ``VideoCapture`` object. 
The index 0 refers to the default camera (built-in webcam)::

    cap = cv.VideoCapture(0)

Inside a loop we read the video capture to get frames.
We then operate on the frame (convert to grayscale), then display the result,
and then loop back. The loop finishes when **q** is pressed::

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

At the end the video stream is relased and all windows are closed::

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

Write to statusbar, overlay and catch mouse events
--------------------------------------------------

The ``createTrackbar`` command adds a trackbar below the main image. 
It goes from 0 to 255 and we set the initial value to 100. 
When the trackbar is moved, it calls a callback function named ``trackbar``::

    cv.createTrackbar('x', 'image', 100, 255, trackbar)

The callback function ``trackbar`` displays the trackbar position in the overlay 
region on getTrackbarPosof the window::

    def trackbar(x):
        """Trackbar callback function."""
        text = 'Trackbar: {}'.format(x)
        cv.displayOverlay('image', text, 1000)
        cv.imshow('image', img)

The ``setMouseCallback`` function attaches a mouse callback function to the *image* window::

    cv.setMouseCallback('image', mouse)

This is the callback definition::

    def mouse(event, x, y, flags, param):
        """Mouse callback function."""
        text = 'mouse at ({}, {})'.format(x, y)
        cv.displayOverlay('image', 'Overlay: ' + text, 1000)
        cv.displayStatusBar('image', 'Statusbar: ' + text, 1000)

In the main part we read and show an image::

    img = cv.imread('messi.jpg', cv.IMREAD_COLOR)
    cv.imshow('image', img)


Object-Oriented Programming (OOP)
---------------------------------

From now on we will use object-oriented programming (OOP) techniques.


.. autoclass:: intro4.App

Patterns
--------

These are the patterns for reading, displaying and saving images::

    img = cv.imread('file', type)
    cv.imshow('win', img)
    cv.imwrite('file', img)

Interface::

    cv.namedWindow('win', type)
    cv.waitKey(ms)
    cv.destroyAllWindows()

Video capture::

    cap = cv.VideoCapture(0)
    cap.isOpened()
    cap.get(id)
    cap.set(id, val)
    ret, frame = cap.read()
    cap.release()

    img2 = cv.cvtColor(img, type)

Drawing functions::

    cv.line(img, p0, p1, col, d)
    cv.circle(img, c0, r, col, d)
    cv.ellipse(img, p0, (w, h), a
    cv.polylines(img, [pts], True, col)

    font = cv.FONT_
    cv.putText(img, str, pos, font, size, col)

Mouse callback::

    cv.setMouseCallback('img', cb)
    cb(evt, x, y, flags, param)
    
    cv.createTrackbar('name', 'win', 0, max, cb)
    cv.getTrackbarPos('name', 'win')


https://docs.quantifiedcode.com/python-anti-patterns/ 