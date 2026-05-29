import sys
from io import StringIO
from text_editor_output import greeting, calculate_pi


def test_greeting():
    """Test the greeting function"""
    print("Testing greeting function...")
    
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    greeting()
    
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert output.strip() == "Hi there", f"Expected 'Hi there', got '{output.strip()}'"
    print("✓ greeting() test passed!")


def test_calculate_pi():
    """Test the calculate_pi function"""
    print("\nTesting calculate_pi function...")
    
    pi_value = calculate_pi()
    expected_pi = 3.14159
    
    print(f"  Calculated pi: {pi_value}")
    print(f"  Expected pi:   {expected_pi}")
    
    assert pi_value == expected_pi, f"Expected {expected_pi}, got {pi_value}"
    assert isinstance(pi_value, float), "Pi should be a float"
    
    # Verify it's rounded to 5 decimal places
    pi_str = str(pi_value)
    if '.' in pi_str:
        decimal_places = len(pi_str.split('.')[1])
        assert decimal_places <= 5, f"Pi should be rounded to 5 decimal places, got {decimal_places}"
    
    print("✓ calculate_pi() test passed!")


def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Running all tests for text_editor_output.py")
    print("=" * 50)
    
    try:
        test_greeting()
        test_calculate_pi()
        
        print("\n" + "=" * 50)
        print("All tests passed! ✓")
        print("=" * 50)
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()
