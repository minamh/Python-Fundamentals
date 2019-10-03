import unittest
import os

def analyze_text(filename):
    number_of_lines=0
    number_of_chars = 0
    with open(filename, mode='rt', encoding='utf-8') as f:
        for line in f:
            number_of_lines = number_of_lines+1
            number_of_chars+=len(line)
    print(f"Number of lines is {number_of_lines}")
    return (number_of_lines,number_of_chars)

class TextAnalysisTests(unittest.TestCase):
    """Test for the analyze_text() function"""

    def setUp(self):
        """Fixture that creates a file for the text methods to use"""
        self.filename = 'text_abalysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged ina  great civil war.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass


    def test_function_runs(self):
        """Basic smoke test: does the function run"""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct"""
        self.assertEqual(analyze_text(self.filename)[0],4)

    def test_character_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 131)

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))
if __name__ == '__main__':
    unittest.main()