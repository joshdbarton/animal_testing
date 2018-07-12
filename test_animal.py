import unittest
import sys
sys.path.append("../")
from animal import Animal
from animal import Dog


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")

    def test_animal_creation(self):

        bob = Dog("Bob")

        self.assertIsInstance(bob, Dog)
        self.assertIsInstance(bob, Animal)

    def test_animal_can_set_legs(self):
        self.bob.set_legs(4)
        self.assertEqual(self.bob.legs, 4)

    def test_animal_can_set_speed(self):
        self.bob.walk()
        self.assertEqual(self.bob.speed, 0.8 )

    def test_dog_string(self):
        bob_string = self.bob.__str__()
        self.assertEqual(bob_string, "Bob is a Dog")

if __name__=="__main__":
    unittest.main()