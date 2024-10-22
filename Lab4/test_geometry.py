import unittest
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class CircleTestCase(unittest.TestCase):
    def test_circle_area_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_circle_area_positive(self):
        res = circle_area(3)
        self.assertAlmostEqual(res, 28.274333882308138)  # Pi * 3^2
    
    def test_circle_perimeter_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_positive(self):
        res = circle_perimeter(3)
        self.assertAlmostEqual(res, 18.84955592153876)  # 2 * Pi * 3


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = rectangle_area(10, 10)
        self.assertEqual(res, 100)

    def test_rectangle_area(self):
        res = rectangle_area(4, 5)
        self.assertEqual(res, 20)

    def test_zero_perimeter(self):
        res = rectangle_perimeter(0, 5)
        self.assertEqual(res, 10)

    def test_rectangle_perimeter(self):
        res = rectangle_perimeter(4, 5)
        self.assertEqual(res, 18)


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = square_area(4)
        self.assertEqual(res, 16)

    def test_zero_perimeter(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimeter(self):
        res = square_perimeter(4)
        self.assertEqual(res, 16)


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_triangle_area(self):
        res = triangle_area(10, 5)
        self.assertEqual(res, 25)

    def test_triangle_perimeter(self):
        res = triangle_perimeter(3, 4, 5)
        self.assertEqual(res, 12)


if __name__ == '__main__':
    unittest.main()
