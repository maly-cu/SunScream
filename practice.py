# ______________________________________________________________________________________________________________________
# 1. GUI Layouts, Labels & Inputs
# Layouts are containers used to arrange widgets in a particular manner.
#       AnchorLayout: Widgets can be anchored to the ‘top’, ‘bottom’, ‘left’, ‘right’ or ‘center’.
#       BoxLayout: Widgets are arranged sequentially, in either a ‘vertical’ or a ‘horizontal’ orientation.
#       FloatLayout: Widgets are essentially unrestricted.
#       RelativeLayout: Child widgets are positioned relative to the layout.
#       GridLayout: Widgets are arranged in a grid defined by the rows and cols properties.
#       PageLayout: Used to create simple multipage layouts, in a way that allows easy flipping from one page to
#       another using borders.
#       ScatterLayout: Widgets are positioned similarly to a RelativeLayout, but can be translated, rotated and scaled.
#       StackLayout: Widgets are stacked in a lr-tb (left to right then top to bottom) or tb-lr order.
# When you add a widget to a layout, the following properties are used to determine the widget’s size and position,
# depending on the type of layout:
#       size_hint: defines the size of a widget as a fraction of the parents size.
#       Values are restricted to range 0.0 - 1.0 i.e. 0.01 = 1/100th of the parent size (1%) and 1. = same size (100%).
#       pos_hint: is used to place the widget relative to the parent.
# The size_hint and pos_hint are used to calculate a widget’s size and position only if the value(s) are not set to None
# . If you set these values to None, the layout will not position/size the widget, and you can specify the values
# (x, y, width, height) directly in screen coordinates.
# YOUTUBE TUTORIAL -
#       https://www.youtube.com/watch?v=QUHnJrFouv8&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn&index=2&ab_channel=TechWithTim

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# Create and set your grid layout
class MyGrid(GridLayout):
    def __init__(self, **kwargs):  # take **kwargs parameters
        """ Initialize and set parameters"""
        super(MyGrid, self).__init__(**kwargs)  # call GridLayout's constructor to inherit from it
        # Now we can change the properties of the grid layouts
        self.cols = 2  # changes number of columns
        # Think of this as editing tkinter grid or CSS styling
        # Next thing we need is to add some widgets to the grid
        self.add_widget(Label(text='First Name: '))  # add_widget() is a method of GridLayout class
        self.first_name = TextInput(multiline=False)  # TextInput default is big multiline textbox
        self.add_widget(self.first_name)

        self.add_widget(Label(text='Last Name: '))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

        self.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)
        self.padding = 10

# NOTE: PIXEL SIZES VARY ACROSS DEVICES SO TO BE SAFE, USE "dp" which means

class MyApp(App):
    def build(self):
        # Now instead of returning a label/widget here, we're gonna return my grid.
        return MyGrid()

    # The reason we can do this is that when we inherit from grid layout, we get the properties of a grid : its
    # width, height, no of columns and widgets attached to it so when we return this grid we can actually draw all
    # the widgets and everything that belonged to my grid which is inherited from grid layout okay and that's the
    # beauty of kind of inheritance and object-oriented programming when we're doing something like creating a GUI or
    # graphical user interface


if __name__ == '__main__':
    MyApp().run()

# ______________________________________________________________________________________________________________________

# 2. Creating Buttons and Triggering Events
# Kivy is mostly event-based, meaning the flow of the program is determined by events.
# Clock events: The Clock object allows you to schedule a function call in the future as a one-time event with
# schedule_once(), or as a repetitive event with schedule_interval().
# You can also create Triggered events with create_trigger().
# Triggers have the advantage of being called only once per frame, even if you have scheduled multiple triggers for
# the same callback.

# Input events: All the mouse click, touch and scroll wheel events are part of the MotionEvent, extended by
# Input Postprocessing and dispatched through the on_motion event in the Window class.
# This event then generates the on_touch_down(), on_touch_move() and on_touch_up() events in the Widget.
# For an in-depth explanation, have a look at Input management - https://kivy.org/doc/stable/api-kivy.input.html.

# Class events: Our base class EventDispatcher used by Widget, uses the power of our Properties for dispatching changes.
# This means when a widget changes its position or size, the corresponding event is automatically fired.
# In addition, you have the ability to create your own events using register_event_type(), as the on_press & on_release
# events in the Button widget demonstrate.
# Another thing to note is that if you override an event, you become responsible for implementing all its behaviour
# previously handled by the base class.
# The easiest way to do this is to call super():
# if super().on_touch_down(touch):
#         return True

# Get more familiar with events in the Events & Properties documentation: https://kivy.org/doc/stable/guide/events.html

# Let's go back to the grid layout and create a button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button  # Let's import Button


# Create and set your grid layout
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        """ Initialize and set parameters"""
        super(MyGrid, self).__init__(**kwargs)  # warning cos of duplication on same page


        self.cols = 2
        self.add_widget(Label(text='First Name: '))
        self.first_name = TextInput(multiline=False)
        self.add_widget(self.first_name)

        self.add_widget(Label(text='Last Name: '))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

        self.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)
        self.padding = 100

        # Let's add a button
        self.submit = Button(text='Submit Info', font_size=20)
        self.add_widget(self.submit)

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()

# After we do this, not only is our button not triggering anything, it also is stuck in one column
# kivy does not have a column span property so to center it, we create another grid layout to contain the button
# and put both of these in a container grid. Kinda like creating a container div and inner divs in html

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        """ Initialize and set parameters"""
        super(MyGrid, self).__init__(**kwargs)  # warning cos of duplication on same page
        self.cols = 1  # sets our main layout to 1 big container column

        # Let's create the inner grid with all the labels and buttons
        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.padding = 50

        # Now let's build the inside grid
        self.inside.add_widget(Label(text='First Name: '))
        self.first_name = TextInput(multiline=False)
        self.inside.add_widget(self.first_name)

        self.inside.add_widget(Label(text='Last Name: '))
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)

        self.inside.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        # Let's actually add self.inside to the main container grid as a row
        self.add_widget(self.inside)

        # Finally, we don't need to create another container grid, we can just add the submit button as the next row
        # of the container grid.
        self.submit = Button(text='Submit Info', font_size=20)
        # So now, let's bind a function to the button.
        self.submit.bind(on_press=self.pressed)  # remember, no function ()s for calls like this. on_press is built-in
        self.add_widget(self.submit)

# When the button press event occurs, it calls the function
    def pressed(self, instance):
        """ When the event is triggered, this function is called"""
        print("Pressed")
        firstname = self.first_name.text
        lastname = self.last_name.text
        email = self.email.text
        print(
            f"Good Day {firstname + ' ' + lastname}, \n We have received your application and will get back to you at {email}.")
        self.first_name.text = self.last_name.text = self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()

# BUT HOLD-UP, HOW DOL WE GET THE INPUTS OF THE TextInput ??
# To do that is the function, we replace it with

def pressed(self, instance):
    """ When the event is triggered, this function is called"""
    # To get the text is simple, we just call the text using their names
    firstname = self.first_name.text
    lastname = self.last_name.text
    email = self. email.text
    print(f"Good Day {firstname + lastname}, \n We have received your application and will get back to you at {email}.")
    # We can clear the Input Fields upon submit as well using the simple assignment method
    self.first_name.text = self.last_name.text = self. email.text = ""
# ______________________________________________________________________________________________________________________

# 3. The .kv design language
# Think of this as the CSS language for styling/designing kivy.
# Kivy provides a design language specifically geared towards easy and scalable GUI Design.
# The language makes it simple to separate the interface design from the application logic, adhering to the separation
# of concerns principle.

# Let's redo our app above with just the main functionalities and the kv language

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# Import the widgets class to be used to build the widgets
from kivy.uix.widget import Widget


# Create class to draw our widgets in, but inherit from widget, not Layout
class TheGrid(Widget):  # changed the name to avoid styling class with above blocks of code
    pass


class MyApp(App):
    def build(self):
        return TheGrid()


if __name__ == '__main__':
    MyApp().run()

# To name the kv file, you must name it the name of your app class, minus 'app' in LOWERCASE
# e.g class MyApp(App)          ------ my.kv
#     class SunscreenApp(App)   ------ sunscreen.kv
#     class Project(App)        ------ project.kv
# It must have the same name as your app class but if the name ends in App, it must be excluded

# So let's create a 'my.kv' file

# In that file, we just type out exactly what we want to show up on screen

# a. Reference the class that we're going to be using to draw the widgets in. In our case, it's the MyGrid class
# It works with indentation. Think of the indents as brackets and all code is inside it
"""
<MyGrid>
    Label:
        text: "test with kv"
"""

# If you run the main code as is right now, even though the .kv file is not referenced anywhere in the main.py file,
# it will build the label

# This is because kivy when run, automatically looks for a .kv file with the name of the class holding your app

# Simple right?
# Let's build what we had again with kivy
# Remember! We had:
#   a 1 column grid container with 2 rows,
#   a 2 column grid with widgets(3 labels, 3TextInput fields) in row 1 and
#   a submit button in row 2 of the grid container

# Let's build this in kivy:

# 1. reference class being styled
"""
<TheGrid>
    GridLayout:  # create container grid
        cols:1

        GridLayout:  # create widgets grid inside container grid
            cols:2
            # create widgets indented under this grid
            Label:
                text: "Name: "

            TextInput:
                multiline:False

            Label:
                text: "Email: "

            TextInput:
                multiline:False
            
        # create button in row 2 under the main grid container indent
        Button:
            text:"Submit"
"""
# ALWAYS BE CAREFUL ABOUT INDENTATION AS THEY MATTER A LOT

# What we get as output is a screen with our widgets created at the bottom right hand corner of the screen.
# the reason this is happeneing is that if you remember, our class TheGrid inherited from Widget instead of GridLayout
# like before. Widgets have a set default size so to the app, all our grids and widgets are contained in a widget.
# To get this to occupy the screen, we have to use a few more properties to override the default size.

# The way we do that is to change the size of the container to the size of the root/window
# Right under our top Grid container, we set the size:

"""
<TheGrid>
    GridLayout:  # create container grid
        cols:1
        size: root.width, root.height
        
"""

# You can adjust this by subtracting from the width/height of the root window e.g.
"""size: root.width-100, root.height-100"""

# We can also change position using 'pos' to adjust/align/pad the grid by the specified size in the space
"""size: root.width-100, root.height-100"""
"""pos: 50, 50"""

# So we can have all our logic in the python file and all our styling in the kv file
# ______________________________________________________________________________________________________________________

# 4. Object Properties and .kv Events
# So how can we make our button work and catch events now that we've seperated the two files?
# To catch the ids for the widgets, we need to set up some values known as Object properties

# in the .kv file, we declare the properties name and email that we need right after referencing the class being built:
"""
<TheGrid>

    name: name
    email: email
    
    GridLayout:  # create container grid
        cols:1
        size: root.width, root.height
    ...
    ...
"""
# name: name - 1st variable is the variable name to be called in .py & 2nd variable is that of the widget id in kv file
# input: name would still work but we would reference input in the function in .py and name is the widget id in .kv
# now in the fields, we set the id to these global propeties/variables
"""
...
...
        GridLayout:  
            cols:2

            Label:
                text: "Name: "

            TextInput:
                id: name
                multiline:False

            Label:
                text: "Email: "

            TextInput:
                id: email
                multiline:False

        # create button in row 2 under the main grid container indent
        Button:
            text:"Submit"
"""

# Now we can access our values from within the python file:

# a. we import the property class

from kivy.app import App
from kivy.uix.widget import Widget
# Object property class import
from kivy.properties import ObjectProperty


# b. In Widget class, assign the object properties to the chosen variables
class TheGrid(Widget):
    name = ObjectProperty()
    email = ObjectProperty()
# NOTE: the variable name & email MUST be the same as what we named them in the .kv file to sync up.
# Remember, they're the 1st variable name before the colon in name: name or input: name


class MyApp(App):
    def build(self):
        return TheGrid()


if __name__ == '__main__':
    MyApp().run()

# So now how can we bind the button to an event??
# Remember that the property for the button event is 'on_press'
# so let's create the function to be called on button press in .py file

class TheGrid(Widget):
    name = ObjectProperty()
    email = ObjectProperty()

    def pressed(self):
        print(
            f"Good Day {self.name.text}, "
            f"\n We have received your application and will get back to you at {self.email.text}."
        )
        self.name.text = self.email.text = ""

# and declare the  Object property in the .kv file
        """
        Button:
            text:"Submit"
            on_press: root.pressed()
        """
# what root does is take the root class TheGrid and calls the btn() func inside it
# If we said "on_press:btn()", it would look for a function not inside a class but in the outer indent

# Essentially, we have linked up all our widgets and ids together. Full code below
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class TheGrid2(Widget):
    name = ObjectProperty()
    email = ObjectProperty()

    def pressed(self):
        print(
            f"Good Day {self.name.text}, "
            f"\n We have received your application and will get back to you at {self.email.text}."
        )
        self.name.text = self.email.text = ""


class MyApp(App):
    def build(self):
        return TheGrid2()


if __name__ == '__main__':
    MyApp().run()

# .kv code
"""
<TheGrid2>
    name: name
    email: email

    GridLayout:  # create container grid
        cols:1
        size: root.width-100, root.height-100
        pos: 50, 50

        GridLayout:  # create widgets grid inside container grid
            cols:2
            # create widgets indented under this grid

            Label:
                text: "Name: "

            TextInput:
                id: name
                multiline:False

            Label:
                text: "Email: "

            TextInput:
                id: email
                multiline:False

        # create button in row 2 under the main grid container indent
        Button:
            text:"Submit"
            on_press: root.pressed()  # bind function on press using Object Property
"""
# ______________________________________________________________________________________________________________________

# 5. FloatLayout for Dynamic Placement
# As described in section 1, the FloatLayout is a layout that allows for some dynamic positioning.
# Think absolute position in CSS

# Float layout is really nice as it's meant kind of for better dynamically sized screens and widgets and
# layouts and whatnot. The grid layout was nice but there was a few issues with that in terms of resize
# ability and things might overlap so a float layout is really a better layout to use.

# It runs on all different kind of operating systems especially like phones like Android apps and iPhone apps

# So let's delete everything essentially including the code in our kv file and start right from the beginning
# with float layout

# a. what we need to do when we use float layout is obviously import it:
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


# b. Now instead of creating a float layout class and doing all that we did last time let's just create the app and
# return a new float layout and that's actually all we need to do from within our Python script
class MyApp(App):
    def build(self):
        return FloatLayout()


if __name__ == '__main__':
    MyApp().run()


# c.  we can move over to our kv file which will be what we're working with for the rest of this lesson.
# so if you remember in the grid section, we declared what section we worked on in the kv file first like:
"""
<MyGrid>

"""
# This is actually what's known as a parent tag. It is the the parent to all properties indented below it, so if we
# maybe assign a size to the grid, that means that all of those widgets underneath get resized to fit inside the
# container. They'll all stretch to fit in.

# For example, if in my .kv I use
"""
<FloatLayout>:
"""

# This means that whenever I create anything in here it will apply to not only this float layout but any float layout
# that I create in this program. So if for some reason I had a float layout inside of a float layout, everything in that
# float layout would have the same properties as what's gonna be in this tag.

# So just like we created the FloatLayout parent tag, we can also create a parent tag for something like a button:

"""
<Button>
    font_size: 40
    color:0.3,0.6,0.7,1
    
<FloatLayout>
    Button:
        text: "Kivy with"
        
    Button:
        text: "May"
"""


# color stands for text color and is in format RGBA(red green blue alpha) which means is that the value has to be
# between -1 and 1. The A in RGBA stands for alpha which is like opacity but a bit different

# Now since we define these two properties in the button parent tag, all other buttons will have these properties

# When we run this, we get 2 buttons on top of each other that fill the screen, so you can only see the last
# made button as the other one is underneath, but they are both in the specified color and size

# Let's resize these buttons now.
"""
<Button>
    font_size: 40
    color:0.3,0.6,0.7,1
    
    # add size property. This takes a percentage of screen size for width & height btwn 0 and 1
    size_hint: 0.2, 0.5
            # so this means width of 20% of screen size and height of 50% of screen size
"""

# Let's set our positions now.
# With float layout, instead of 'pos', we use 'pos_hint' which is a dict with 6 keys:
#       pos_hint:{'x'. 'y', 'top', 'bottom', 'left', 'right'}
#       all these keys take a value btwn 0 and 1 (think of it like the degree of something)
#       let's use x & top

# The coordinate system in kivy starts from the bottom left corner of the screen(0,0)
# So if we want to move something to the right, we can add to x and to move towards the top, add to top (remember 0 - 1)
# Let's test this:
"""
    Button:
        pos_hint: {'x":0.5, 'top':1}
        text: "Kivy with"
"""
# Now we see that the button 'Kivy with' is moved 50% x of the screen and 100% to the top of the screen
# Float layout is mostly relative to the screen so when resized, it's responsive instead of static like the font_size

# -------- Change properties based on state
# We can actually change properties of the button based on a state. Our button has about three states:
#       normal,
#       down(clicked) and
#       hover

# So if we wanted to for example change the text of a button when we're clicking it, we can do that from within the .kv
# file:

# a. we can set an id
"""
    Button:
        id: btn
        text: "May" 
"""

# b. we use an if statement to check the state of the id. So let's change the text when clicked
"""
    Button:
        id: btn
        text: "May" if btn.state == "normal" else "Clicked"
"""

# Let's change the background color now
"""
    Button:
        id: btn
        text: "May" if btn.state == "normal" else "Clicked"
        background-color: 0.3,0.4,0.5,1 if btn.state == normal else 1,1,1,1
"""


# So this is a brief intro to float layout and how we can resize things and dynamically change them

# ______________________________________________________________________________________________________________________

# 6. Touch Input/Mouse Input
#
# Here, we're gonna see how we can get mouse input and also touch input(like if someone touch the screen with their
# thumb or drag something around).

# First, we're gonna have to re-import our widgets
from kivy.app import App
from kivy.uix.widget import Widget


# b. Now we'll create a class for the touch input
class Touch(Widget):
    # inside, let's define a few in-built functions
    def on_touch_down(self, touch):
        pass

    def on_touch_move(self, touch):
        pass

    def on_touch_up(self, touch):
        pass

    # What these functions are gonna do is they have one input parameter called 'touch' and  when we touch down on the
    # screen we will get the position of where we pressed and a few a few other piece of information as well

    # Same thing with move and up: when we're moving while touching the screen we'll be able to get that
    # information and then if we release, we'll be able to see where we released and when we released

    # Since we're inheriting from widget, these inbuilt functions just work on any layout(grid, box, float)


# Now, we can specify behaviour for our app on touch within those functions
class Touch(Widget):
    def on_touch_down(self, touch):
        print("Mouse Down at ", touch)

    def on_touch_move(self, touch):
        print("Mouse Dragged to ", touch)

    def on_touch_up(self, touch):
        print("Mouse released at ", touch)

# Now let's build our app and return Touch


class MyApp(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    MyApp().run()

# Now, let's make a simple button in the .kv file to test
"""
<Touch>
    Button:
        text: "Touch Test"
"""

# Now let's run this and we get output like:
"""
Mouse Down at  <MouseMotionEvent spos=(0.08260325406758448, 0.13188647746243742) pos=(66.0, 79.00000000000001)>
Mouse released at  <MouseMotionEvent spos=(0.08260325406758448, 0.13188647746243742) pos=(66.0, 79.00000000000001)>
Mouse Down at  <MouseMotionEvent spos=(0.08260325406758448, 0.13188647746243742) pos=(66.0, 79.00000000000001)>
Mouse Dragged to  <MouseMotionEvent spos=(0.06758448060075094, 0.13355592654424042) pos=(54.0, 80.00000000000001)>
"""
# s-pos : relative position to screen
# pos: absolute x & y position

# If you notice, although our app works, we get the position, it isn't dependent on the button, it's working anywhere
# Matter of fact, our button no longer works/clicks Why??
# Because button by default already has those functions so when we create it in our class, it overrides the functions
# attached to widgets

# If we want our button to retain functionality and not be overriden by our function, we can use object properties

# a. let's import the object property function
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


# b. let's initialise an object property for the button
class Touch(Widget):

    btn = ObjectProperty()

    def on_touch_down(self, touch):
        print("Mouse Down at ", touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print("Mouse Dragged to ", touch)

    def on_touch_up(self, touch):
        print("Mouse released at ", touch)
        self.btn.opacity = 1


class MyApp(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    MyApp().run()

# In .kv file, let's create a matching variable
"""
<Touch>
    btn:bttn
    
    Button:
        id: bttn
        text: "Touch Test"
"""

# Now when we run this, our button has its click functionality.

# HOWEVER!! THIS ISN'T IDEAL COS IT TRIGGERS IT NO MATTER WHERE THE MOUSE CLICKS
# Another way to do this from the youtube vid comment section:
#       Almog Surizon
#       3 years ago
#       Hello Tim, great video. Just wanted to add.
#       When you override the on touch method, you should add the super().on_touch_down(touch).
#       So it will add all the implementations of touching that the kivy use anyway.
#       If you add the button opacity it does not really click it, and won't call the command of the button(on_press).
#       And with what you do, it'll "click" the button any time the on_touch_down() method is called, no matter where
#       on the screen it was triggered.

#       Instead, do:
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Touch(Widget):

    btn = ObjectProperty()

    def on_touch_down(self, touch):
        print("Mouse Down at ", touch)
        super().on_touch_down(touch)  # This instead calls the inbuilt function instead of overriding it so the button
        # still retains it's default behaviour

    def on_touch_move(self, touch):
        print("Mouse Dragged to ", touch)
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        print("Mouse released at ", touch)
        super().on_touch_up(touch)


class MyApp(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    MyApp().run()

# ______________________________________________________________________________________________________________________

# 7. Simple Drawing App (Using Canvas)
# Here, we're going to be creating a very simple and basic drawing application .
# This is just introduce us to the graphic system in Kivy, nothing too complex.
# Just drawing a square and moving it using touch input

# If interested in doing more, check out the docs at https://kivy.org/doc/stable/
# You can read through, and they're pretty self-explanatory in terms of how to create different shapes and objects.

# What we're going to do here will give us enough of a foundation to draw some basic shapes onto your screen

# a. First thing we'll do is to import the kivy graphics modules we need. We need this to draw
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.app import App

# The way that drawing works in Kivy is kind of based off of something called opengl.
# Essentially, you have a canvas and that canvas contains drawing instructions and you can give instructions to the
# canvas obviously to draw different things as well as update those positions/instructions.

# b. This project is just based off of our last lesson so let's just clear our .kv file and copy the .py code below
class Touch(Widget):

    # c. Let's define an init here and create our canvas
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        # d. What we're going to do here is to draw a rectangle.
        # The way to do that is to use widget's inbuilt canvas method
        """        
        with self.canvas:
            self.rect = Rectangle(pos=(0,0), size=(50,50))
        """

        # e. so how do we change the color? We change the color of the canvas pen BEFORE drawing it, so let's redo it
        with self.canvas:
            Color(1, 0, 1, 0.5)
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))
            # You can draw multiple on the canvas
            # Please note that the canvas uses STATIC POSITIONS, we're setting absolute x and y axis unlike the relative
            # placements used before. So if you adjust the scree, the drawings do not adjust

# f. So now, let's make our shapes follow us around when we hold and drag our mouse/touch

    def on_touch_down(self, touch):
        # We do this simply by assigning the shape's position to anywhere the screen records a touch input
        self.rect.pos = touch.pos
        print("Square Clicked at ", touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Square Dragged to ", touch)


class MyApp(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    MyApp().run()

# That's all! Now your shape follows around or goes to where you click.

# ______ Drawing a Line
# Obviously, there's a lot more things you can do with this in terms of drawing e.g. you can draw lines

# a. from kivy graphics, let's import the line module
from kivy.graphics import Line
from kivy.uix.widget import Widget
from kivy.app import App


# b. like we did above, in our canvas, we just create the line and give it positions
class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 1, 0.5)
            Line(points=[20,30,100,400,90,300], width=10)


class MyApp(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    MyApp().run()


# Et Voila!! That's all. Try to read up and experiment on your own cos you learn better from practice but this is
# the basic intro to kivy graphics

# ______________________________________________________________________________________________________________________

# 8. Navigation Between Multiple Screens
# Here we're going to be going through how to change screens. So essentially having multiple windows and then doing some
# kind of transition between them based on an event.

# For this lesson, we're going to have a login form and if you type in the password correctly, it'll move you to the
# next page. # To achieve this, we'll go through quite a few steps. Let's start with a basic template:

"""
from kivy.app import App

class MyMainApp(App):
    def build(self):
        return

if __name__ == "__main__":
    MyMainApp().run()

"""
# a. we're actually gonna start by doing something different that we haven't done before
# If you remember our .kv file naming convention, we can actuall use something called a builder to allow us to load our
# .kv file no matter what the name is. So let's import it
"""
from kivy.lang import Builder
from kivy.app import App
"""
# b. right before our app class, we load it.
"""kv = Builder.load_file("my.kv")
"""
# c. So now, we can return kv without naming ou kv file same as app
"""
class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
"""
# d. Now, to switch between screens, we use kivy modules called ScreenManager and well Screens
# Let's import them
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.app import App

# e. So we're going to set up 3 classes to represent our 2 screens and 1 screen manager for transitions.

class LogInPage(Screen):
    pass

class SecretPage(Screen):
    pass

class Navigator(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()

# Now let's move on to our .kv file.
# So if you remember about the indentation hierarchy, we'll have our screen hierarchy declared at the top
"""
Navigator:
    LogInPage:
    SecretPage:
    
# Now let's create our individual pages like before:

<LogInPage>
    name: "login"  # name is what we call to transition between screens
    
    # Like we've done before with multiple grid layouts, let's create the input labels and fields
    GridLayout:  # create container grid
        cols:1

        GridLayout:  # create widgets grid inside container grid
            cols:2
            # create widgets indented under this grid
            Label:
                text: "Password: "

            TextInput:
                # give password an id so we can check the value against a correct password
                id: passw
                multiline:False
            
        # create button in row 2 under the main grid container indent
        Button:
            text:"Submit"
            # we'll have an on_release event to trigger next page navigation
            # To transition to another window, we use app.root.current and the name we set earlier
            on_release: app.root.current = "secret"
            
<SecretPage>
    name: "secret"
    
    # let's show the secret on the page
    Label:
        text: "Hey, come here... don't tell anyone but you're very beautiful. Shhh!!
        
    # let's add a button to help us navigate back to the login page
    Button:
        text: "<-"
        # we'll have an on_release event to transition to named window
        on_release: app.root.current = "login"
"""

# I TESTED THIS IN MAIN INSTEAD, TOO MUCH CONFLICT WITH SHARED .kv FILE CAUSING ERRORS
# If we run this, everything should work fine. You can go on to style the buttons and widgets as you prefer


# Notice though that these transitions are probably not ideal as they are all coming from right to left, like forwards
# To go forward and backwards, on EACH screen, set the transition directions.
# You must set for all else, once changed, it sticks. Let's take secrets page for example:
"""
<SecretPage>
    name: "secret"
    
    Label:
        text: "Hey, come here... don't tell anyone but you're very beautiful. Shhh!!
        
    Button:
        text: "<-"
        on_release: app.root.current = "login"
        
        # here we change the transition
        root.manager.transition.direction = "right"
"""
# Now how can we check that the password is correct? We can just add a little bit of logic in our .kv file with if else
# Let's do that under our Submit button so it does not work if incorrect
"""
    Button:
    text: "Submit"
    # let's add our transition condition
    on_release: app.root.current = "secret" if passw.text == "May" else "login"

"""
# And that's how that works!! Full code below:
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.app import App

# e. So we're going to set up 3 classes to represent our 2 screens and 1 screen manager for transitions.

class LogInPage(Screen):
    pass

class SecretPage(Screen):
    pass

class Navigator(ScreenManager):
    pass

# ALWAYS do this just BEFORE MAIN APP class, else it loads first without declaring classes above
kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()

# ________ in .kv file
"""
Navigator:
    LogInPage:
    SecretPage:

# Now let's create our individual pages like before:

<LogInPage>
    name: "login"  # name is what we call to transition between screens

    # Like we've done before with multiple grid layouts, let's create the input labels and fields
    GridLayout:  # create container grid
        cols:1

        GridLayout:  # create widgets grid inside container grid
            cols:2
            # create widgets indented under this grid
            Label:
                text: "Password: "

            TextInput:
                id: passw
                multiline:False

        # create button in row 2 under the main grid container indent
        Button:
            text:"Submit"
            # we'll have an on_release event to trigger next page navigation
            # To transition to another window, we use app.root.current and the name we set earlier
            on_release:
                app.root.current = "secret" if passw.text == "May" else "login"
                root.manager.transition.direction = "left"

<SecretPage>
    name: "secret"

    GridLayout:  # create container grid
        cols:1

        GridLayout:  # create label grid inside container grid
            cols:1

            # let's show the secret on the page
            Label:
                text: "Hey, come here... don't tell anyone but you're very beautiful. Shhh!!"

        # let's add a button to help us navigate back to the login page
        Button:
            text: "Back <-"
            # we'll have an on_release event to transition to named window
            on_release:
                app.root.current = "login"
                root.manager.transition.direction = "right"

"""
# If you want to do all your logic in python, or check the password, then try using ObjectProperties like before

# ______________________________________________________________________________________________________________________

# 9. Creating a Pop-up Window
# We're going to be creating pop-up windows which is actually very useful and is super simple to do.
# Let's build a very basic interface

# a. First we import the pop-up module
from kivy.uix.popup import Popup
# b. let's import the rest of the modules we know
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

# b. We create a class for the popup which we'll use to define the widgets in our popup, and also make it a float layout
class PU(FloatLayout):
    pass

# In the .kv file, let's set up the pop-up's position, size, label etc
"""
<P>:
    Label:
        text: "You pressed the button"
        size_hint: 0.6, 0.2
        pos_hint{"x":0.4, "top": 0.5}
        
    # Let's add a button to our pop-up
    Button:
        text: "Ok"
        size_hint: 0.4, 0.2
        pos_hint{"x":0.4, "y": 0.1}        

"""
# c. To create a pop-up, we can just create a function to create and show it so that way, whenever you call it, a popup
# shows. You can make this a method to one of your classes or just leave it as a function
def show_popup():
    # so let's create a new instance of p which holds our pop-up content
    show = PU()

    # now, let's call our pop-up method from the popup module
    popup_message = Popup(title="Message", content=show, size_hint=(None, None), size=(400, 400))
    # title - title of out pop-up box
    # content - instance of our PU class holding our content
    # size_hint - we set to None so it doesn't dynamically resize
    # size - static width, height size

    # To show this window, we open it
    popup_message.open()


# d. Now we have the popup set up, to trigger it, let's create a simple button widget
class Widgets(Widget):
    # remember, we can create a function to call in the .kv file
    def btn(self):
        show_popup()

class MyApp(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    MyApp().run()


# e. Let's add the button to the .kv file and call our function on press
"""
<Widgets>
    Button:
        text:"Press Me"
        on_release: root.btn
"""
# Now let's run this and it should work. And that's it.
# If you press anywhere outside the pop-up window, it will close. For closing on button press, do personal research


# ______________________________________________________________________________________________________________________


# ______________________________________________________________________________________________________________________
