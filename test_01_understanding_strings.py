"""
string is one of the most commonly used data types,
it used to represent textual data.
It has different behavior than a char* in C.

I recommend you to do this lesson by experimenting in the console (REPL).
Run each test individually and fix each one, one assert at a time.

Start reading online documentation/resources
only if you are not able to figure it out by experiment.
"""

# Ignore the below 3 lines.
import placeholders
__ = placeholders.__    # Replace me with expected value or True/False
___ = placeholders.___  # Replace me with numeric values


__author__ = 'Enhance46'


def test_string_type():
    assert 'str' == type("Hello World").__name__
    assert __ == isinstance("Hello World", str)


def test_single_quoted_strings_are_strings():
    assert __ == isinstance('Hello World', str)


def test_double_quoted_strings_are_strings():
    assert __ == isinstance("Hello World", str)


def test_triple_quoted_strings_are_strings():
    assert isinstance("""Hello World""", str) == __


def test_triple_single_quoted_strings_are_strings():
    assert __ == isinstance('''Hello World''', str)


def test_raw_strings_are_strings():
    # raw string literals are specified using the r before the first quote
    # raw strings are used to avoid escaping backslashes, usually useful
    # when specifying things like window's paths which use backslash. e.g. r"c:\work\myfile.ini"

    assert True == isinstance(r"Hello \n World", str)
    assert 1 == len("\n")
    assert 2 == len(r"\n")

    # write a non-raw string in the ___ to make both strings equal.
    assert 'Hello\\n' == __


def test_single_quoted_strings_can_embed_double_quotes():
    first = 'The pilot said "Jump"'
    # ability to embed the other quote avoids the hassle of escaping quotes in strings
    second = "The pilot said \"Jump\""  # note back slash escaping of "
    are_equal = (first == second)
    assert are_equal == __


def test_double_quoted_strings_can_embed_single_quotes():
    first = "The pilot said 'Jump'"
    second = 'The pilot said \'Jump\''  # note back slash escaping of '
    are_equal = (first == second)
    assert are_equal == __


def test_triple_quoted_strings_can_have_both_single_and_double_quotes():
    # Edit tq_str to make are_equal True
    tq_str = """ Isn't the "Hobbit" great? """
    dq_str = "Isn't the \"Hobbit\" great?"
    are_equal = (tq_str == dq_str)
    assert are_equal == __


def test_triple_quoted_strings_can_span_lines():
    tq_str = """Hello
World"""
    dq_str =  "__"  # what is the double quoted form of tq_str
    assert (tq_str == dq_str)


def test_string_len():
    assert len("Hello 'world'") == __ # what is the length
    assert len('Hello \'world\'') == __ # what is the length


def test_triple_quoted_strings_can_span_lines2():
    string = """Hello
    World"""
    assert isinstance(string, str) == True
    assert len(string) == __ # what is the length


def test_strings_can_be_indexed():
    string = "Hello"
    assert __ == string[0]
    assert __ == string[1]
    assert __ == string[2]
    assert __ == string[3]
    assert __ == string[4]
    assert __ == string[-1]  # solves the common use case to iterate from end
    assert __ == string[-2]
    assert __ == string[-3]
    assert __ == string[-4]
    assert __ == string[-5]
    assert __ == string[-0]  # hint -0 is 0
    assert __ == len(string)
    try:
        # raises an error, we will revisit exceptions later
        out_of_bounds = string[5]
    except IndexError as ie:
        print(ie)
        assert True  # make this True to proceed.


def test_chars_are_strings_too():
    string = "Hello"
    first_char = string[0]
    assert __ == type(first_char).__name__
    assert __ == type('a').__name__
    assert __ == type("a").__name__


def test_strings_are_immutable():
    # strings in python cannot be modified unlike in C
    string = "Hello"
    try:
        string[0] = __
    except TypeError as te:
        # run this test alone in py.test and observe the  'FAILURES' section and 'Captured stdout call' section
        # at the end. see the error messages in FAILURES and the print statements in "Captured stdout call"
        # Print statements can be added to failing tests and can be  observed in a similar manner
        print("Can you see me in pytest output?")
        print(te)
        assert True    # after you observe, make this True to proceed.


def test_string_concat():
    assert __ == "Hello " + " world"
    assert __ == """Hello """ + 'world'
    assert __ == 'Hello ' + "world"


def test_string_slicing():
    #  Slicing creates new strings
    string = "Hello world"
    #with begin : end
    assert __ == string[0:0]

    assert __ == string[0:2]
    assert __ == string[1:5]
    assert __ == string[1:-1]
    assert __ == string[2:-2]

    # with :end, note usage of negative indices as well.
    assert __ == string[:0]
    assert __ == string[:4]
    assert __ == string[:-1]

    # with begin:
    assert __ == string[0:]
    assert __ == string[4:]
    assert __ == string[-1:]

    # observe the invariant
    assert __ == string[:0] + string[0:]
    assert __ == string[:1] + string[1:]
    assert __ == string[:2] + string[2:]
    assert __ == string[:3] + string[3:]


def test_string_repeat():
    assert __ == "Hello" * 3
    assert __ == len("Hello " * 2)


def test_string_combine():
    # Use slicing to pass the assert.

    hello = "Hello World"
    bye = "Goodbye moon"
    assert bye[0:7] + hello[5:11] == __


def test_string_formatting():
    greeting = "Hello '{0}'".format("learner")
    assert "Hello 'learner'" == greeting

    truth = "{1} plus {1} makes {0}".format("two", "one")
    assert truth == __

    stmt = "{name} is {age} years old".format(name="Ravi", age=25)
    assert __  == stmt


def test_string_formatting_literals():
    """
    literals which start with f are implicitly treated as expressions which are evaluated at runtime.
    This makes formatting a little more easier to understand.
    The full details are at: https://www.python.org/dev/peps/pep-0498/, read it to get an idea of how a feature
    is introduced into python.
    """
    value = 10
    assert __ == f"value is: {value}"
    value = 20
    assert __ == f"value is: {value + 10}"
    name, age = "Ramu", 20
    assert __ == f"{name} is {age} years old!"


def test_string_membership(): # True or False
    assert __ == ('c' in 'apple')   # is there a precedence issue here or something else?
    assert __ == ('a' in 'apple')
    assert ('app' in 'apple') == __


def test_string_methods():
    word = "hello"
    assert __ == word.capitalize()
    assert __ == word.center(10)
    assert __ == word.zfill(10)
    assert __ == word.replace("l", "zebra")
    # you can experiment with all methods on string in console
    # by entering "something". (enter the dot too) to pop up all the available methods.

# Now apply what you have learnt above.


# implement rotate_right method to run test_rotate
# Don't touch the function def rotate_right
def rotate_right(input, count):
    """
    write a single line of code using what you have learnt in this lesson - slicing and concat
    assume 0 <= count <= len(input)
    """
    n=input[len(input)-count:]+input[:len(input)-count]
    return n  # replace __ with the code


def test_rotate():
    assert __ == rotate_right("hello", 0)
    assert __ == rotate_right("hello", 1)
    assert __ == rotate_right("hello", 2)
    assert __ == rotate_right("hello", 3)
    assert __ == rotate_right("hello", 4)
    assert __ == rotate_right("hello", 5)


# Read this after you finish the lesson:
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

THREE_THINGS_I_LEARNT = """
-Strings Slicing
-Comparision
-Membership and Rotation
"""
