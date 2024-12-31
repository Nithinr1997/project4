mport
unittest


class TestNotebook(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 2), 5)


unittest.main(argv=[''], verbosity=2, exit=False)

#This is project4