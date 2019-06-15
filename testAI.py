import unittest
import alien_invasion

class TestTile(unittest.TestCase):
   
    def setUp(self):
        AI = alien_invasion.AlienInvasion()
        self.title= AI.WindowTitle

    def test_WindowTitle(self):
        self.assertEqual(self.title,"Alien Invasion")


if __name__ == '__main__':
    unittest.main()