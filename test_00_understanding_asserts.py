"""
This lesson introduces the basic assert statement in python.
assert is generally used to 'assert' the truth of an expression.
It takes the form assert <expr>, <optional message>.
If <expr> evaluates to False an AssertionError is raised with the <optional message>.
If it evaluates to True, nothing happens and execution moves to the next statement in the function.

In the tests below, replace the blanks with values so that the resulting expression is True.

Recommended flow to do the lessons is given below.
This approach comes in handy as we move to more complex topics
even if this is seem trivial at this point.

- attempt each test_XXX method individually instead of doing all of them at one go.
    The test names are chosen to tell you what you need to understand to solve the test :-)
- you can run a single method by clicking on "Run Test" above the method,
    this runs just that single method
- study the failure error messages in OUTPUT window
- fix the code with your expected code and re-run the test till the code passes.
- Use the python console to experiment, refer to online python docs, google search etc.
    if something is not clear.
- go to the next method once you have resolved a method.

Note: __ and ___ is just a constant to make the code valid python code,
      you need to replace it with correct values.
"""

# Ignore the below 3 lines.
import placeholders
__ = placeholders.__    # Replace me with expected value or True/False
___ = placeholders.___  # Replace me with numeric values


__author__ = 'Enhance46'


def test_assert_true():
    assert __  # This should be True -- replace ___ with True.


def test_assert_true_with_message():
    print("test print")
    # what error do you see when you run this test?
    assert __, "This is the failure message"
    # replace ___ with True to stop seeing the assertion error


def test_assert_equality():
    assert 2 + 5 == __  # replace __ with the expected value

# Fill in __ in the statements below to make the asserts succeed


def test_make_assert_true_1():
    assert __ > 7, "Fill in a value greater than 7"

# you can use the interpreter to find the value of 2**30


def test_make_assert_true_2():
    assert 2**30 < __, "Fill in value greater than 2**30"


def test_make_assert_true_3():
    string_1 = "Hello, World"
    string_2 = __
    assert string_1 == string_2


THREE_THINGS_I_LEARNT = """
- 
- 
- 
"""
