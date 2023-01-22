import unittest

from core.replacer import replace_content


class TestStringMethods(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(replace_content('<html><div>Black Russia</div></html>'),
                         '<html><div>BlackHub Games</div></html>')

    def test_ignoring_case(self):
        self.assertEqual(replace_content('<html><div>blacK ruSsia</div></html>'),
                         '<html><div>BlackHub Games</div></html>')

    def test_ignoring_newline(self):
        self.assertEqual(replace_content('<html><div>blacK \n ruSsia</div></html>'),
                         '<html><div>BlackHub Games</div></html>')

    def test_dividing_by_one_tag(self):
        self.assertEqual(replace_content('<html><div>blacK <span> ruSsia</div></html>'),
                         '<html><div>BlackHub <span> Games</div></html>')

    def test_dividing_by_two_tags_concat(self):
        self.assertEqual(replace_content('<html><div>blacK <span><b> ruSsia</div></html>'),
                         '<html><div>BlackHub <span><b> Games</div></html>')

    def test_dividing_by_two_tags_separate(self):
        self.assertEqual(replace_content('<html><div>blacK <span> <b> ruSsia</div></html>'),
                         '<html><div>BlackHub <span> <b> Games</div></html>')

    def test_dividing_by_three_tags_different_cases(self):
        self.assertEqual(replace_content('<html><div>blacK <span><span><b> ruSsia</div></html>'),
                         '<html><div>BlackHub <span><span><b> Games</div></html>')
        self.assertEqual(replace_content('<html><div>blacK <span> <span><b> ruSsia</div></html>'),
                         '<html><div>BlackHub <span> <span><b> Games</div></html>')
        self.assertEqual(replace_content('<html><div>blacK <span><span> <b> ruSsia</div></html>'),
                         '<html><div>BlackHub <span><span> <b> Games</div></html>')
        self.assertEqual(replace_content('<html><div>blacK <span> <span> <b> ruSsia</div></html>'),
                         '<html><div>BlackHub <span> <span> <b> Games</div></html>')


if __name__ == '__main__':
    unittest.main()
