# Test-Driven Development Ex: Text analyzer function

import unittest
import os

# Comment the below code to see the failure
def analyze_text(filename):
    """ Calculate the number of lines and characters in the files

    Args :
          filename: The name of the file to analyze

    Raises:
            IOError: If the "filename" does not exist or can't be read

    Returns: A tuple where the first element is the nummber of lines in the file and second element is the number of chracters
    """
    lines = 0
    chars = 0
    with open(filename,'r') as fp:
        for line in fp:
            lines += 1
            chars += len(line)
        return (lines, chars)               # A tuple containing (line-count, character-count). Here returns (4,121) for setUp Fixture

# Use the TestCase of module unittest
class TextAnalysisTests(unittest.TestCase):
    """ Tests for the 'analyze_text()' function"""

    # 1st fixture is run before each test method
    def setUp(self):
        """Fixture that creates a file for the text analyzer to use"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename,'w') as fp:
            fp.write("Now we are engaged in a civil war\n"
                     "testing whether the nation\n"
                     "or any nation so conceived and so dedicated,\n"
                     "can long endure")

    # 2nd fixture is run after the analyze_text() function
    def tearDown(self):
        """ Fixture that deletes the files used by setUp """
        try:
            os.remove(self.filename)
        except:
            pass                    # It doesn't matter if the file does not exists


    # Create method in a TestCase using test_ . Automatically discovered by the unittest framework and dont require explicit registration
    def test_function_runs(self):
        """ Basic smoke test: does the function run"""
        analyze_text(self.filename)

    def test_line_count(self):
        """ Check that the line count is correct"""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        """ CHeck that the chracter count is correct"""
        self.assertEqual(analyze_text(self.filename)[1], 121)

    def test_no_such_file(self):
        """ Check the proper exception is thrown for missing file"""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))



# Define the main block
# unittest.main() will search for all test cases with the TestCase subclass in the module and execute all of their test methods
if __name__ == '__main__':
    unittest.main()


"""
Output :
If analyze_text() was not defined :
E
======================================================================
ERROR: test_function_runs (__main__.TextAnalysisTests)
Basic smoke test: does the function run
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_test_files\TestAnalyzer.py", line 12, in test_function_runs
    analyze_text()
NameError: name 'analyze_text' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.001s


If analyze_text(self.filename) does not return 4, then the test will fail
.F
======================================================================
FAIL: test_line_count (__main__.TextAnalysisTests)
Check that the line count is correct
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_test_files\TestAnalyzer.py", line 40, in test_line_count
    self.assertEqual(analyze_text(self.filename), 4)
AssertionError: None != 4

----------------------------------------------------------------------
Ran 2 tests in 0.020s


"""
