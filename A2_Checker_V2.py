# Youzhang Mark Sun
# Oct 14, 2019
# 66 test cases

import unittest
import elevation as e

class A2CheckerV2(unittest.TestCase):
    def setUp(self):
        self.m_1 = [[1]]
        self.m_2 = [[2, 3], 
                    [5, 1]]
        self.m_3 = [[11, 12, 16], 
                    [9, 8, 14], 
                    [4, 27, 2]]
        self.m_4 = [[8, 31, 18, 15], 
                    [44, 30, 11, 25], 
                    [55, 59, 22, 62], 
                    [5, 14, 46, 60]]
        self.m_5 = [[58, 103, 45, 96, 115], 
                    [70, 8, 56, 31, 55], 
                    [107, 78, 52, 89, 91], 
                    [35, 40, 20, 16, 112], 
                    [60, 93, 67, 99, 37]]

    def test_compare(self):
        print("\ncompare_elevations_within_row:")
        self.m_x = [[1, 2, 3], [5, 6, 5], [4, 5, 8]]
        self.assertListEqual(e.compare_elevations_within_row(self.m_x, 0, 2), [1, 1, 0], "contain equal")
        self.assertListEqual(e.compare_elevations_within_row(self.m_x, 1, 6), [2, 1, 0], "contain equal")
        self.assertListEqual(e.compare_elevations_within_row(self.m_x, 2, 7), [2, 0, 1], "simple")
        self.assertListEqual(e.compare_elevations_within_row(self.m_3, 0, 10), [0, 0, 3], "simple")
        self.assertListEqual(e.compare_elevations_within_row(self.m_3, 1, 10), [2, 0, 1], "simple")

    def test_update(self):
        print("\nupdate_elevation:")
        e.update_elevation(self.m_3, [0, 1], [2, 1], 1)
        self.assertListEqual(self.m_3, [[11, 13, 16], [9, 9, 14], [4, 28, 2]], "vertical entire")
        e.update_elevation(self.m_3, [0, 0], [1, 0], 1)
        self.assertListEqual(self.m_3, [[12, 13, 16], [10, 9, 14], [4, 28, 2]], "vertical partial")
        e.update_elevation(self.m_4, [1, 0], [1, 3], 2)
        self.assertListEqual(self.m_4, [[8, 31, 18, 15], [46, 32, 13, 27], [55, 59, 22, 62], [5, 14, 46, 60]], "horizontal entire")
        e.update_elevation(self.m_4, [2, 1], [2, 2], 2)
        self.assertListEqual(self.m_4, [[8, 31, 18, 15], [46, 32, 13, 27], [55, 61, 24, 62], [5, 14, 46, 60]], "horizontal partial")
        e.update_elevation(self.m_2, [0, 0], [0, 0], 3)
        self.assertListEqual(self.m_2, [[5, 3], [5, 1]], "edge case one spot")
        e.update_elevation(self.m_2, [1, 0], [1, 1], 5)
        self.assertListEqual(self.m_2, [[5, 3], [10, 6]], "horizontal entire")
        e.update_elevation(self.m_5, [0, 1], [4, 1], -1)
        self.assertListEqual(self.m_5, [[58, 102, 45, 96, 115], [70, 7, 56, 31, 55], [107, 77, 52, 89, 91], [35, 39, 20, 16, 112], [60, 92, 67, 99, 37]], "vertical entire")
        e.update_elevation(self.m_5, [2, 1], [2, 3], 1000)
        self.assertListEqual(self.m_5, [[58, 102, 45, 96, 115], [70, 7, 56, 31, 55], [107, 1077, 1052, 1089, 91], [35, 39, 20, 16, 112], [60, 92, 67, 99, 37]], "horizontal partial")
        e.update_elevation(self.m_5, [4, 4], [4, 4], 10)
        self.assertListEqual(self.m_5, [[58, 102, 45, 96, 115], [70, 7, 56, 31, 55], [107, 1077, 1052, 1089, 91], [35, 39, 20, 16, 112], [60, 92, 67, 99, 47]], "edge case one spot")

    def test_average(self):
        print("\nget_average_elevation:")
        self.assertAlmostEqual(e.get_average_elevation(self.m_1), 1, 3, "simple")
        self.assertAlmostEqual(e.get_average_elevation(self.m_2), 2.75, 3, "simple")
        self.assertAlmostEqual(e.get_average_elevation(self.m_3), 11.4444, 3, "simple")
        self.assertAlmostEqual(e.get_average_elevation(self.m_4), 31.5625, 3, "simple")
        self.assertAlmostEqual(e.get_average_elevation(self.m_5), 65.32, 3, "simple")

    def test_peak(self):
        print("\nfind_peak:")
        self.assertListEqual(e.find_peak(self.m_1), [0, 0], "simple")
        self.assertListEqual(e.find_peak(self.m_2), [1, 0], "simple")
        self.assertListEqual(e.find_peak(self.m_3), [2, 1], "simple")
        self.assertListEqual(e.find_peak(self.m_4), [2, 3], "simple")
        self.assertListEqual(e.find_peak(self.m_5), [0, 4], "simple")

    def test_is_sink(self):
        print("\nis_sink:")
        self.assertTrue(e.is_sink(self.m_1, [0, 0]), "edge case no surrounding")
        self.assertFalse(e.is_sink(self.m_1, [1, 1]), "out of bound")
        self.assertFalse(e.is_sink(self.m_2, [0, 0]), "special case diagonal")
        self.assertTrue(e.is_sink(self.m_2, [1, 1]), "edge case corner")
        self.m_x = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.assertTrue(e.is_sink(self.m_x, [1, 1]), "edge case all same")
        self.assertFalse(e.is_sink(self.m_3, [1, 2]), "simple")
        self.assertTrue(e.is_sink(self.m_4, [1, 2]), "simple")
        self.assertFalse(e.is_sink(self.m_4, [3, 1]), "simple")
        self.assertFalse(e.is_sink(self.m_4, [-1, 2]), "out of bound")
        self.assertTrue(e.is_sink(self.m_5, [1, 1]), "simple")
        self.assertTrue(e.is_sink(self.m_5, [3, 3]), "simple")
        self.assertFalse(e.is_sink(self.m_5, [3, 2]), "simple")

    def test_local_sink(self):
        print("\nfind_local_sink:")
        self.assertListEqual(e.find_local_sink(self.m_1, [0, 0]), [0, 0], "edge case no surrounding")
        self.assertListEqual(e.find_local_sink(self.m_2, [1, 1]), [1, 1], "edge case already sink")
        self.assertListEqual(e.find_local_sink(self.m_2, [0, 0]), [1, 1], "simple diagonal")
        self.assertListEqual(e.find_local_sink(self.m_3, [1, 1]), [2, 2], "simple diagonal")
        self.assertListEqual(e.find_local_sink(self.m_3, [1, 2]), [2, 2], "simple diagonal")
        self.assertListEqual(e.find_local_sink(self.m_4, [1, 1]), [0, 0], "simple diagonal")
        self.assertListEqual(e.find_local_sink(self.m_4, [2, 2]), [1, 2], "simple")
        self.assertListEqual(e.find_local_sink(self.m_5, [1, 1]), [1, 1], "edge case already sink")
        self.assertListEqual(e.find_local_sink(self.m_5, [2, 3]), [3, 3], "simple")

    def test_hike(self):
        print("\ncan_hike_to:")
        self.assertTrue(e.can_hike_to(self.m_3, [2, 2], [0, 2], 100), "simple")
        self.assertTrue(e.can_hike_to(self.m_3, [2, 2], [0, 2], 14), "edge case end with 0")
        self.assertFalse(e.can_hike_to(self.m_3, [2, 2], [0, 2], 13), "simple not enough")
        self.m_x = [[7, 7, 7], [1, 1, 7], [1, 1, 6]]
        self.assertTrue(e.can_hike_to(self.m_x, [2, 2], [0, 0], 100), "simple")
        self.assertTrue(e.can_hike_to(self.m_x, [2, 2], [0, 0], 1), "edge case end with 0")
        self.assertFalse(e.can_hike_to(self.m_x, [2, 2], [0, 0], 0), "edge case end not enough")
        self.m_x = [[7, 7, 7], [1, 1, 7], [1, 1, 7]]
        self.assertTrue(e.can_hike_to(self.m_x, [2, 2], [0, 0], 0), "edge case end with 0")
        self.assertTrue(e.can_hike_to(self.m_4, [2, 2], [0, 1], 31), "edge case end with 0")
        self.assertFalse(e.can_hike_to(self.m_4, [2, 2], [0, 1], 30), "edge case not enough")
        self.m_x = [[10007, 100, 9], [1, 1, 8], [1, 1, 7]]
        self.assertTrue(e.can_hike_to(self.m_x, [2, 2], [0, 0], 10010), "simple")
        self.assertFalse(e.can_hike_to(self.m_x, [2, 2], [0, 0], 9999), "edge case not enough")
        self.assertFalse(e.can_hike_to(self.m_x, [2, 2], [0, 0], 50), "simple not enough")
        self.m_x = [[100, 1, 1], [60, 1, 1], [59, 58, 50]]
        self.assertTrue(e.can_hike_to(self.m_x, [2, 2], [1, 0], 20), "simple")
        self.assertFalse(e.can_hike_to(self.m_x, [2, 2], [0, 0], 10), "simple not enough")

    def test_resolution(self):
        print("\nget_lower_resolution")
        self.assertListEqual(e.get_lower_resolution(self.m_1), [[1]], "odd size")
        self.assertListEqual(e.get_lower_resolution(self.m_2), [[2]], "simple")
        self.assertListEqual(e.get_lower_resolution(self.m_3), [[10, 15], [15, 2]], "odd size")
        self.assertListEqual(e.get_lower_resolution(self.m_4), [[28, 17], [33, 47]], "simple")
        self.assertListEqual(e.get_lower_resolution(self.m_5), [[59, 57, 85], [65, 44, 101], [76, 83, 37]], "odd size")

    def tearDown(self):
        pass

def basic():
    suite = unittest.TestSuite()
    suite.addTest(A2CheckerV2("test_compare"))
    suite.addTest(A2CheckerV2("test_update"))
    suite.addTest(A2CheckerV2("test_average"))
    suite.addTest(A2CheckerV2("test_peak"))
    return suite

def sink():
    suite = unittest.TestSuite()
    suite.addTest(A2CheckerV2("test_is_sink"))
    suite.addTest(A2CheckerV2("test_local_sink"))
    return suite

def complex():
    suite = unittest.TestSuite()
    suite.addTest(A2CheckerV2("test_hike"))
    suite.addTest(A2CheckerV2("test_resolution"))
    return suite

if (__name__ == "__main__"):
    runner = unittest.TextTestRunner()
    basic = runner.run(basic())
    if (basic.wasSuccessful()):
        print("Passed basic tests!")
    print("======================================================================")
    sink = runner.run(sink())
    if (sink.wasSuccessful()):
        print("Passed sink related tests!")
    print("======================================================================")
    complex = runner.run(complex())
    if (complex.wasSuccessful()):
        print("Passed complex tests!")