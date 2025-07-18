# main.py
from reference_manual import print_reference_manual
from tests import test_number_to_pair, test_pair_to_number, test_reference_manual_length

if __name__ == '__main__':
    # 测试颜色编码转换
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    
    # 测试参考手册格式
    test_reference_manual_length()
    
    # 打印参考手册
    print_reference_manual()
    print('✅ 所有测试通过!')
