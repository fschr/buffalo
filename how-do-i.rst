How Do I?
=========

This page contains solutions and templates to common *how do I _____?* questions. It's probably a good idea to read this if you haven't used Buffalo before.

How do I make a button?
-----------------------

Making a button is pretty easy. Inside the constructor of an object that extends ``Scene``, make a button and add it to ``self.buttons``. For example,
::
    class SomeScene(Scene):
        def __init__(self):
            hello_button = Button( utils.SCREEN_M, "Hello" )
            self.buttons.add( exit_button )

will create a button in the middle of the screen (hence, passing ``utils.SCREEN_M`` as the ``pos`` argument) with text "Hello".

How do I make a button that does something?
-------------------------------------------

Making a button do something is pretty easy, too. Just pass a function as the ``func`` keyword argument to a ``Button`` constructor. For example,
::

    exit_button = Button( utils.SCREEN_M, "Exit", func=sys.exit )

will create a button that calls ``sys.exit()`` when it is clicked. Be sure to pass a *function* and not the *return value* of a function as the ``func`` keyword argument. For example, the following code will cause your program to crash when the button is clicked.
::

    exit_button = Button( utils.SCREEN_M, "Exit", func=sys.exit() )

Since ``sys.exit()`` returns ``None``, the value ``None`` will be assigned to this button's ``func``. When the button is clicked, it will attempt to call ``None``, but will fail, since ``None`` is not a function.

How do I center things?
-----------------------

Most objects in buffalo can be centered with the ``x_centered`` and ``y_centered`` keyword arguments. For example,
::

    self.labels.add(
        Label(
            utils.SCREEN_M,
	    "This text is perfectly centered.",
	    x_centered=True,
            y_centered=True,
        )

will create a label who's center position (x, y) will be equal to the 2-tuple passed as the ``pos`` argument. In this case, the label's center position is set to ``utils.SCREEN_M``, making it perfectly centered on the screen. It should be noted that in the above examples, since ``x_centered`` and ``y_centered`` default to ``False``, all of the buttons are not perfectly centered on the screen. Instead, their top-left corners are perfectly centered with the screen.
	
How do I position objects relative to their size? (or how do I know how big an object is before I make it?)
-----------------------------------------------------------------------------------------------------------

Commonly, programmers want to make buttons and labels in the bottom left and bottom right of the screen. Take a moment to try this in Buffalo. You'll soon realize that to make a label or button flesh with the bottom of the screen, you must first know the height of the button. To rememdy this, two keyword arguments are part of most Buffalo objects.

Suppose you want to create an exit button in the bottom-left corner of the screen. Here's how to do that:
::

    self.buttons.add(
        Button(
            (5, utils.SCREEN_H - 5),
	    "Exit",
	    invert_y_pos=True,
        )
    )

The keyword argument ``invert_y_pos`` positions the button so the ``y`` value of the ``pos`` argument passed to the button's constructor actually refers to the position of the *bottom*, instead of the top of the button.

Normally, the ``pos`` argument sets the position of the Buffalo object's top-left corner. Setting ``invert_y_pos`` to ``True`` causes the position of the object to be calculated such that the argument passed as ``pos`` refers to the position of the *bottom*-left corner of the object, rather than the position of the top-left corner.

For more clarity, check out this code:
::

    >> button = Button( (5, 5), "blah blah" )
    >> button.pos
    (5, 5)
    >> button = Button( (5, 5), "blah blah", invert_x_pos=True )
    >> button.pos
    (-37, 5)

When ``invert_x_pos`` is ``True``, the position of the button is automatically calculated such that the position of the top-*right* (instead of top-left) corner of the button is ``(5, 5)``.
