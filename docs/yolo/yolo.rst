YOLO - object detection
=======================

YOLO — You Only Look Once — is an extremely fast multi object detection algorithm 
which uses convolutional neural network (CNN) to detect and identify objects.

The neural network has this network architecture.

.. image:: yolo1_net.png

Source: https://arxiv.org/pdf/1506.02640.pdf


This is our input image: 

.. image:: images/horse.jpg
:download:`horse.jpg <images/horse.jpg>`

Load the YOLO network
---------------------

In order to run the network you will have to download the pre-trained 
YOLO weight file (237 MB).
https://pjreddie.com/media/files/yolov3.weights

Also download the the YOLO configuration file.

:download:`yolov3.cfg <yolov3.cfg>`

You can now load the YOLO network model from the harddisk into OpenCV::

    net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)

The YOLO neural network has 254 components.
You can print them to the console with::

    ln = net.getLayerNames()
    print(len(ln), ln)

The 254 elements consist of convolutional layers (``conv``), 
rectifier linear units (``relu``) etc.::

    254 ['conv_0', 'bn_0', 'relu_0', 'conv_1', 'bn_1', 'relu_1', 'conv_2', 'bn_2',
    'relu_2', 'conv_3', 'bn_3', 'relu_3', 'shortcut_4', 'conv_5', 'bn_5', 'relu_5',
    'conv_6', 'bn_6', 'relu_6', 'conv_7', 'bn_7', 'relu_7', 'shortcut_8', 'conv_9',
    'bn_9', 'relu_9', 'conv_10', 'bn_10', 'relu_10', 'shortcut_11', 'conv_12', 'bn_12',
    ...


Create a blob
-------------

The input to the network is a so-called **blob** object.
The function ``cv.dnn.blobFromImage(img, scale, size, mean)`` transforms the image into a blob::

    blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

It has the following parameters:

* the **image** to transform
* the **scale** factor (1/255 to scale the pixel values to [0..1])
* the **size**, here a 416x416 square image
* the **mean** value (default=0)
* the option **swapRB=True** (since OpenCV uses BGR)

A blob is a 4D numpy array object (images, channels, width, height).
The image below shows the red channel of the blob.
You notice the brightness of the red jacket in the background.

.. image:: yolo1_blob.png

.. literalinclude:: yolo1.py

The blob object is given as input to the network::

    net.setInput(blob)
    t0 = time.time()
    outputs = net.forward(ln)
    t = time.time()

The forward propagation takes about 2 seconds on an MacAir 2012
(1,7 GHz Intel Core i5).

:download:`yolo1.py <yolo1.py>`


And the 80 COCO class names.

:download:`coco.names<coco.names>`

Identifiy objects
-----------------

These two instructions calculate the network response::

    net.setInput(blob)
    outputs = net.forward(ln)

The ``outputs`` object are vectors of lenght 85

* 4x the bounding box (centerx, centery, width, height)
* 1x box confidence
* 80x class confidence

We add a slider to select the BoundingBox confidence level from 0 to 1.

.. image:: yolo2_blob.png

The final image is this:

.. image:: yolo2.png

.. literalinclude:: yolo2.py
:download:`yolo2.py <yolo2.py>`


3 Scales for handling different sizes
-------------------------------------

The YOLO network has 3 outputs:

* 507 (13 x 13 x 3) for large objects
* 2028 (26 x 26 x 3) for medium objects
* 8112 (52 x 52 x 3) for small objects

Detecting objects
-----------------

In this program example we are going to detect objects in multiple imgages.

.. image:: yolo3.png

.. image:: yolo3_zoo.png

.. image:: yolo3_tennis.png

.. literalinclude:: yolo3.py
:download:`yolo3.py <yolo3.py>`

Sources
-------
* https://arxiv.org/pdf/1506.02640.pdf 
* https://en.wikipedia.org/wiki/Object_detection
* https://github.com/StefanPetersTM/TM 
* https://www.cyberailab.com/home/a-closer-look-at-yolov3

Tutorials:

* https://www.pyimagesearch.com/2017/08/21/deep-learning-with-opencv/
* https://www.learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/
