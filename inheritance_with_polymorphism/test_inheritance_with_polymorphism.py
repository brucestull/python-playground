import unittest
import inheritance_with_polymorphism as iwp

# python -m unittest test_inheritance_with_polymorphism.py

TEST_NAME_ANIMAL = "Animal"
TEST_NAME_MAMMAL = "Mammal"
TEST_NAME_CAT = "Bunbun"
TEST_NAME_HUMAN = "Flynnt"


class AnimalTestCase(unittest.TestCase):
    """
    Tests for the `Animal` class.
    """

    def test_has_correct_name(self):
        """
        `name` attribute should be set correctly in the `__init__` method from constructor argument.
        """
        animal = iwp.Animal(TEST_NAME_ANIMAL)
        self.assertEqual(animal.name, TEST_NAME_ANIMAL)

    def test_has_mobility_is_true(self):
        """
        `has_mobility` attribute should be set to `True` in the `__init__` method.
        """
        animal = iwp.Animal(TEST_NAME_ANIMAL)
        self.assertTrue(animal.has_mobility)

    def test_sound_off_method_is_none(self):
        """
        `sound_off` method should return `None` since it is not implemented
        in the `Animal` class.
        """
        animal = iwp.Animal(TEST_NAME_ANIMAL)
        self.assertIsNone(animal.sound_off())

class MammalTestCase(unittest.TestCase):
    """
    Tests for the `Mammal` class.
    """

    def test_has_correct_name(self):
        """
        `name` attribute should be set correctly in the `__init__` method from constructor argument.
        """
        mammal = iwp.Mammal(TEST_NAME_MAMMAL)
        self.assertEqual(mammal.name, TEST_NAME_MAMMAL)

    def test_has_mobility_is_true(self):
        """
        `has_mobility` attribute should be set to `True` in the `__init__` method.
        """
        mammal = iwp.Mammal(TEST_NAME_MAMMAL)
        self.assertTrue(mammal.has_mobility)

    def test_has_fur_is_true(self):
        """
        `has_fur` attribute should be set to `True` in the `__init__` method.
        """
        mammal = iwp.Mammal(TEST_NAME_MAMMAL)
        self.assertTrue(mammal.has_fur)


class CatTestCase(unittest.TestCase):
    """
    Tests for the `Cat` class.
    """

    def test_has_correct_name(self):
        """
        `name` attribute should be set correctly in the `__init__` method from constructor argument.
        """
        cat = iwp.Cat(TEST_NAME_CAT)
        self.assertEqual(cat.name, TEST_NAME_CAT)

    def test_has_mobility_is_true(self):
        """
        `has_mobility` attribute should be set to `True` in the `__init__` method.
        """
        cat = iwp.Cat(TEST_NAME_CAT)
        self.assertTrue(cat.has_mobility)

    def test_has_fur_is_true(self):
        """
        `has_fur` attribute should be set to `True` in the `__init__` method.
        """
        cat = iwp.Cat(TEST_NAME_CAT)
        self.assertTrue(cat.has_fur)

    def test_sound_off_method_is_correct(self):
        """
        `sound_off` method should return the correct string.
        """
        cat = iwp.Cat(TEST_NAME_CAT)
        self.assertEqual(cat.sound_off(), f"Meow, I'm {TEST_NAME_CAT}.")


class HumanTestCase(unittest.TestCase):
    """
    Tests for the `Human` class.
    """

    def test_has_correct_name(self):
        """
        `name` attribute should be set correctly in the `__init__` method
        from constructor argument.
        """
        human = iwp.Human(TEST_NAME_HUMAN)
        self.assertEqual(human.name, TEST_NAME_HUMAN)

    def test_has_mobility_is_true(self):
        """
        `has_mobility` attribute should be set to `True` in the `__init__`
        method.
        """
        human = iwp.Human(TEST_NAME_HUMAN)
        self.assertTrue(human.has_mobility)

    def test_has_fur_is_true(self):
        """
        `has_fur` attribute should be set to `True` in the `__init__` method.
        """
        human = iwp.Human(TEST_NAME_HUMAN)
        self.assertTrue(human.has_fur)

    def test_has_spoken_language_is_true(self):
        """
        `has_spoken_language` attribute should be set to `True` in the
        `__init__` method.
        """
        human = iwp.Human(TEST_NAME_HUMAN)
        self.assertTrue(human.has_spoken_language)

    def test_sound_off_method_is_correct(self):
        """
        `sound_off` method should return the correct string.
        """
        human = iwp.Human(TEST_NAME_HUMAN)
        self.assertEqual(human.sound_off(), f"Hello, I'm {TEST_NAME_HUMAN}.")