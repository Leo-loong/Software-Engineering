import unittest

from White import Triangle
from Black import CheckId


def compute_check_digit(id17):
    """计算身份证第18位校验码"""
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_map = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    total = sum(int(id17[i]) * weights[i] for i in range(17))
    return check_map[total % 11]


class MyTest(unittest.TestCase):

    # ==================== 黑盒测试：身份证号校验 ====================

    # --- 有效等价类 ---

    def test_black_valid_numeric_check(self):
        """有效身份证号 — 校验码为数字"""
        self.assertEqual(CheckId.Black('110221200004100610').exec(), 1)

    def test_black_valid_X_check(self):
        """有效身份证号 — 校验码为大写X"""
        # 11022120000410008 的加权和=112, 112%11=2, 对应校验码X
        self.assertEqual(CheckId.Black('11022120000410008X').exec(), 1)

    def test_black_valid_x_check(self):
        """有效身份证号 — 校验码为小写x"""
        self.assertEqual(CheckId.Black('11022120000410008x').exec(), 1)

    # --- 无效等价类：长度非法 ---

    def test_black_invalid_empty(self):
        """空字符串"""
        self.assertEqual(CheckId.Black('').exec(), 0)

    def test_black_invalid_too_short(self):
        """长度小于18位"""
        self.assertEqual(CheckId.Black('11022120000410061').exec(), 0)

    def test_black_invalid_too_long(self):
        """长度大于18位"""
        self.assertEqual(CheckId.Black('1102212000041006100').exec(), 0)

    # --- 无效等价类：字符非法 ---

    def test_black_invalid_letter_in_body(self):
        """前17位包含字母"""
        self.assertEqual(CheckId.Black('1102212000041006A0').exec(), 0)

    def test_black_invalid_special_char(self):
        """包含特殊字符"""
        self.assertEqual(CheckId.Black('1102212000041006-0').exec(), 0)

    # --- 无效等价类：出生日期非法 ---

    def test_black_invalid_month_00(self):
        """月份为00"""
        self.assertEqual(CheckId.Black('110221200000100610').exec(), 0)

    def test_black_invalid_month_13(self):
        """月份为13"""
        self.assertEqual(CheckId.Black('110221200013100610').exec(), 0)

    def test_black_invalid_day_00(self):
        """日期为00"""
        self.assertEqual(CheckId.Black('110221200004000610').exec(), 0)

    def test_black_invalid_day_32(self):
        """日期为32"""
        self.assertEqual(CheckId.Black('110221200004320610').exec(), 0)

    def test_black_invalid_feb_30(self):
        """2月30日"""
        self.assertEqual(CheckId.Black('110221200002300610').exec(), 0)

    def test_black_invalid_feb_29_non_leap(self):
        """非闰年2月29日（2023年不是闰年）"""
        self.assertEqual(CheckId.Black('110221202302290610').exec(), 0)

    def test_black_invalid_future_date(self):
        """出生日期在未来"""
        self.assertEqual(CheckId.Black('110221209901010610').exec(), 0)

    # --- 无效等价类：校验码错误 ---

    def test_black_invalid_wrong_check_digit(self):
        """校验码错误（正确为0，错误改为1）"""
        self.assertEqual(CheckId.Black('110221200004100611').exec(), 0)

    def test_black_invalid_wrong_X_to_digit(self):
        """校验码应为X但给了数字"""
        self.assertEqual(CheckId.Black('110221200004100080').exec(), 0)


    # ==================== 白盒测试：三角形类型判断（分支覆盖） ====================

    # --- 分支1：非整数输入 → "not a triangle!" ---

    def test_white_non_int_string(self):
        """字符串参数"""
        self.assertEqual(Triangle.triangle("3", 4, 5), "not a triangle!")

    def test_white_non_int_float(self):
        """浮点数参数"""
        self.assertEqual(Triangle.triangle(3.5, 4, 5), "not a triangle!")

    # --- 分支2：整数但超出范围或不能构成三角形 → "not a triangle!" ---

    def test_white_out_of_range_below(self):
        """边长为0"""
        self.assertEqual(Triangle.triangle(0, 4, 5), "not a triangle!")

    def test_white_out_of_range_above(self):
        """边长超过10000"""
        self.assertEqual(Triangle.triangle(10001, 4, 5), "not a triangle!")

    def test_white_boundary_lower(self):
        """边长为1（下边界有效值）"""
        self.assertEqual(Triangle.triangle(1, 1, 1), "equilateral triangle!")

    def test_white_boundary_upper(self):
        """边长为10000（上边界有效值）"""
        self.assertEqual(Triangle.triangle(10000, 10000, 10000), "equilateral triangle!")

    def test_white_triangle_inequality(self):
        """不满足三角形不等式：1+2=3，不大于3"""
        self.assertEqual(Triangle.triangle(1, 2, 3), "not a triangle!")

    def test_white_triangle_inequality_2(self):
        """不满足三角形不等式：2+3=5"""
        self.assertEqual(Triangle.triangle(2, 3, 5), "not a triangle!")

    # --- 分支3：三边相等 → "equilateral triangle!" ---

    def test_white_equilateral(self):
        """等边三角形"""
        self.assertEqual(Triangle.triangle(5, 5, 5), "equilateral triangle!")

    # --- 分支4：两边相等 → "isosceles triangle!" ---

    def test_white_isosceles_ab(self):
        """等腰三角形：a==b"""
        self.assertEqual(Triangle.triangle(3, 3, 5), "isosceles triangle!")

    def test_white_isosceles_bc(self):
        """等腰三角形：b==c"""
        self.assertEqual(Triangle.triangle(5, 3, 3), "isosceles triangle!")

    def test_white_isosceles_ac(self):
        """等腰三角形：a==c"""
        self.assertEqual(Triangle.triangle(3, 5, 3), "isosceles triangle!")

    # --- 分支5：三边互不相等 → "regular triangle!" ---

    def test_white_regular(self):
        """普通三角形（三边不等）"""
        self.assertEqual(Triangle.triangle(3, 4, 5), "regular triangle!")

    def test_white_regular_boundary(self):
        """普通三角形（边界附近）"""
        self.assertEqual(Triangle.triangle(2, 3, 4), "regular triangle!")


if __name__ == '__main__':
    # ---------- 黑盒测试套件 ----------
    suite_black = unittest.TestSuite()
    black_tests = [
        MyTest('test_black_valid_numeric_check'),
        MyTest('test_black_valid_X_check'),
        MyTest('test_black_valid_x_check'),
        MyTest('test_black_invalid_empty'),
        MyTest('test_black_invalid_too_short'),
        MyTest('test_black_invalid_too_long'),
        MyTest('test_black_invalid_letter_in_body'),
        MyTest('test_black_invalid_special_char'),
        MyTest('test_black_invalid_month_00'),
        MyTest('test_black_invalid_month_13'),
        MyTest('test_black_invalid_day_00'),
        MyTest('test_black_invalid_day_32'),
        MyTest('test_black_invalid_feb_30'),
        MyTest('test_black_invalid_feb_29_non_leap'),
        MyTest('test_black_invalid_future_date'),
        MyTest('test_black_invalid_wrong_check_digit'),
        MyTest('test_black_invalid_wrong_X_to_digit'),
    ]
    suite_black.addTests(black_tests)

    # ---------- 白盒测试套件 ----------
    suite_white = unittest.TestSuite()
    white_tests = [
        MyTest('test_white_non_int_string'),
        MyTest('test_white_non_int_float'),
        MyTest('test_white_out_of_range_below'),
        MyTest('test_white_out_of_range_above'),
        MyTest('test_white_boundary_lower'),
        MyTest('test_white_boundary_upper'),
        MyTest('test_white_triangle_inequality'),
        MyTest('test_white_triangle_inequality_2'),
        MyTest('test_white_equilateral'),
        MyTest('test_white_isosceles_ab'),
        MyTest('test_white_isosceles_bc'),
        MyTest('test_white_isosceles_ac'),
        MyTest('test_white_regular'),
        MyTest('test_white_regular_boundary'),
    ]
    suite_white.addTests(white_tests)

    runner = unittest.TextTestRunner(verbosity=2)

    print("=" * 50)
    print("黑盒测试套件（身份证号校验）")
    print("=" * 50)
    runner.run(suite_black)

    print()
    print("=" * 50)
    print("白盒测试套件（三角形类型判断）")
    print("=" * 50)
    runner.run(suite_white)
