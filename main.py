# main.py
from reference_manual import print_reference_manual
from tests import test_number_to_pair, test_pair_to_number, test_reference_manual_length

if __name__ == '__main__':
    # Test color code transformed
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    
    # Test reference manual format
    test_reference_manual_length()
    
    # Print reference manual 
    print_reference_manual()
    print('✅ Test Passed!')
