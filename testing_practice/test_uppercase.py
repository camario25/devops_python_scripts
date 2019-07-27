import unittest
import uppercase_word_module

class Test__uppercase_word(unittest.TestCase):
    def test_single_capital_letter(self):
        test_input = "Apple"
        test_output = uppercase_word_module.uppercase_word_func(test_input)
        self.assertEqual(test_output, "APPLE")
    
    def test_all_lowercase(self):
        test_input = "apple"
        test_output = uppercase_word_module.uppercase_word_func(test_input)
        self.assertEqual(test_output, "APPLE")
    
    def test_all_uppercase(self):
        test_input = "APPLE"
        test_output = uppercase_word_module.uppercase_word_func(test_input)
        self.assertEqual(test_output, "APPLE")

    def test_empty_input(self):
        test_input = ""
        test_output = uppercase_word_module.uppercase_word_func(test_input)
        self.assertEqual(test_output, "")

    def test_integers(self):
        test_input = "123"
        test_output = uppercase_word_module.uppercase_word_func(test_input)
        self.assertEqual(test_output, "123")


    def test_mixed_characters(self):
        test_input = "123?/ lsdfAS"
        test_output = uppercase_word_module.uppercase_word_func(test_input)
        self.assertEqual(test_output, "123?/ LSDFAS")

if __name__ == '__main__':
    unittest.main()