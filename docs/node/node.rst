Nodes
=====

Nodes are the elements of the window which are used as the base class
to create widgets and shapes. Nodes are the elements of a tree graph.
Each window is a root of the tree and can have multiple nodes as children.
Nodes can have children of their own.

Widgets are user control items such as text fields, buttons, comboboxes, 
entry fields, and listboxes. 

Shapes are the geometrical formes such as markers, lines, arrows, 
rectangles, circles, ellipses and polygones.

.. autoclass:: node1.Demo

.. image:: node1.*

Node options
------------

Each node has 4 attributes (options):

* position
* size
* gap between objects
* direction towards the next object

The Node options are reset at the creation of a new window. They
are in the format of **numpy** int64 arrays. The advantage of using 
numpy arrays is that we can do vector addition. For example the 
lower right corner is simply::

    p1 = pos + size

The node options are stored as a dictionary inside the Window class::

    class Window:
        """Create a window for the app."""
        node_options = dict(pos=np.array((20, 20)),
                            size=np.array((100, 20)),
                            gap=np.array((10, 10)),
                            dir=np.array((0, 1)),
                            )

When creating a new window, the initial node options are reassigned::

    Node.options = Window.node_options.copy()

Parents and children
--------------------

The window is the parent of the first-level children. At window creation an empty
children list is created::

        self.children = []  # children

At that point the window is the parent of the children to add. Parents are stored
in a stack. Initialy the window is the parent for the first-level children. So at
window creation, the window itself is added to the parent stack::

        self.stack = [self]  #  parent stack

At that point no node exists, so the active node is set to None::

        self.node = None  # currently selected node

The attribute *level* decides the point of attachement of the new node:

level = 0
    The last parent remains the parent and a new sibling to the last
    is created.

level = 1
    The level is increased and the last child becames the new parent.
    The new child is a great-child of the previos parent.

level = -1
    The level is decreased and the grand-parent becomes the new parent.
    The new child is a sibling to the previous parent

Enclosing nodes
---------------

The following exemple shows a first node, folloed by 3 nodes at a child 
level, then 4 nodes at the parent level, with a change of direction::

    class Demo(App):
        def __init__(self):
            super().__init__()

            Node()
            Node(level=1)
            Node()
            Node()
            Node(level=-1, dir=(1, 0))
            Node()
            Node()
            Node()

.. autoclass:: node2.Demo

.. image:: node2.*

In the next example node 6 increases level again, and changes
direction to vertical. The parent of the last nodes is forced to 
enclcose its children::

        Node()
        Node(level=1)
        Node()
        Node()
        Node(level=-1, dir=(1, 0))
        Node(level=1, dir=(0, 1))
        Node()
        Node()
        Node().parent.enclose_children()

Embedded nodes
--------------

Nodes can be embedded in other nodes. In the example below node 1 is
embedded in node 0, node 3 and 4 is embedded in node 2. This is the code::

    Node()
    Node(level=1)
    Node()
    Node(level=1)
    Node()
    Node(level=-1)
    Node()
    Node(level=-1)
    Node()

.. autoclass:: node4.Demo

.. image:: node4.*

In the following example, we go down 3 levels: 

* node 1 is embedded in node 0
* node 2 is embedded in node 1
* node 3 is embedded in node 2

This is the code::

        Node()
        Node(level=1)
        Node(level=1)
        Node(level=1)
        Node(level=-1)
        Node(level=-1)
        Node(level=-1)

.. autoclass:: node5.Demo

.. image:: node5.*


Decrease multiple levels
------------------------

While we can go down at most one level, it is possible to go up multiple levels
at once. If level is negative we repeat this:

* enclose the children of the current parent
* make the grand-parent the current parent

This is the code::

    for i in range(-level):
        self.win.current_parent.enclose_children()
        self.parent = self.win.current_parent.parent
        self.win.current_parent = self.parent

Here is the previous example where we go up 3 levels at once, instead of one by one::

    Node()
    Node(level=1)
    Node(level=1)
    Node(level=1)
    Node(level=-3)
    Node()
    Node()

.. autoclass:: node6.Demo

.. image:: node6.*


Changing the direction of node placement
----------------------------------------

New nodes are placed according to the direction `dir` vector. This can be:

* vertical (0, 1)
* horizontal (1, 0)
* diagonal (1, 1)

Here is an example of 5 nodes placed in vertical, horizontal and two 
diagonal directions::

    for i in range(5):
        Node(dir=(1, 0), size=(20, 20))

    for i in range(5):
        Node(dir=(0, 1))

    for i in range(5):
        Node(dir=(1, -1))

    for i in range(5):
        Node(dir=(1, 1))

.. autoclass:: node7.Demo

.. image:: node7.*