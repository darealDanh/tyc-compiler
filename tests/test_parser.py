"""
Parser test cases for TyC compiler
100 comprehensive test cases for parser covering all grammar structures
"""

import pytest
from tests.utils import Parser


# ========== Basic Program Structure (5 tests) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_program_main_no_return_type():
    """3. Main with inferred return type"""
    assert Parser("main() {}").parse() == "success"


def test_program_multiple_functions():
    """4. Multiple functions"""
    source = """
    int add(int a, int b) { return a + b; }
    void main() {}
    """
    assert Parser(source).parse() == "success"


def test_program_struct_and_function():
    """5. Struct and function"""
    source = """
    struct Point { int x; int y; };
    void main() {}
    """
    assert Parser(source).parse() == "success"


# ========== Struct Declarations (8 tests) ==========
def test_struct_simple():
    """6. Simple struct"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_struct_empty():
    """7. Empty struct"""
    source = "struct Empty { };"
    assert Parser(source).parse() == "success"


def test_struct_single_member():
    """8. Struct with single member"""
    source = "struct Single { int value; };"
    assert Parser(source).parse() == "success"


def test_struct_multiple_types():
    """9. Struct with multiple types"""
    source = "struct Person { string name; int age; float height; };"
    assert Parser(source).parse() == "success"


def test_struct_nested_type():
    """10. Struct with another struct type"""
    source = """
    struct Point { int x; int y; };
    struct Line { Point start; Point end; };
    """
    assert Parser(source).parse() == "success"


def test_struct_many_members():
    """11. Struct with many members"""
    source = "struct Data { int a; int b; int c; float d; string e; };"
    assert Parser(source).parse() == "success"


def test_multiple_structs():
    """12. Multiple struct declarations"""
    source = """
    struct A { int x; };
    struct B { float y; };
    struct C { string z; };
    """
    assert Parser(source).parse() == "success"


def test_struct_before_function():
    """13. Struct before function"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p; }
    """
    assert Parser(source).parse() == "success"


# ========== Function Declarations (10 tests) ==========
def test_function_no_params():
    """14. Function with no parameters"""
    source = 'void greet() { printString("Hello"); }'
    assert Parser(source).parse() == "success"


def test_function_one_param():
    """15. Function with one parameter"""
    source = "void printValue(int x) { printInt(x); }"
    assert Parser(source).parse() == "success"


def test_function_multiple_params():
    """16. Function with multiple parameters"""
    source = "int add(int a, int b, int c) { return a + b + c; }"
    assert Parser(source).parse() == "success"


def test_function_return_int():
    """17. Function returning int"""
    source = "int getNumber() { return 42; }"
    assert Parser(source).parse() == "success"


def test_function_return_float():
    """18. Function returning float"""
    source = "float getPi() { return 3.14; }"
    assert Parser(source).parse() == "success"


def test_function_return_string():
    """19. Function returning string"""
    source = 'string getName() { return "John"; }'
    assert Parser(source).parse() == "success"


def test_function_inferred_return():
    """20. Function with inferred return type"""
    source = "getValue() { return 10; }"
    assert Parser(source).parse() == "success"


def test_function_struct_param():
    """21. Function with struct parameter"""
    source = """
    struct Point { int x; int y; };
    void printPoint(Point p) { printInt(p.x); }
    """
    assert Parser(source).parse() == "success"


def test_function_struct_return():
    """22. Function returning struct"""
    source = """
    struct Point { int x; int y; };
    Point makePoint(int x, int y) { Point p; return p; }
    """
    assert Parser(source).parse() == "success"


def test_function_empty_body():
    """23. Function with empty body"""
    source = "void doNothing() {}"
    assert Parser(source).parse() == "success"


# ========== Variable Declarations (8 tests) ==========
def test_var_decl_auto_with_init():
    """24. Auto with initialization"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_no_init():
    """25. Auto without initialization"""
    source = "void main() { auto x; }"
    assert Parser(source).parse() == "success"


def test_var_decl_int_with_init():
    """26. Int with initialization"""
    source = "void main() { int x = 10; }"
    assert Parser(source).parse() == "success"


def test_var_decl_int_no_init():
    """27. Int without initialization"""
    source = "void main() { int x; }"
    assert Parser(source).parse() == "success"


def test_var_decl_float():
    """28. Float variable"""
    source = "void main() { float pi = 3.14; }"
    assert Parser(source).parse() == "success"


def test_var_decl_string():
    """29. String variable"""
    source = 'void main() { string name = "Alice"; }'
    assert Parser(source).parse() == "success"


def test_var_decl_struct():
    """30. Struct variable"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p; }
    """
    assert Parser(source).parse() == "success"


def test_var_decl_multiple():
    """31. Multiple variable declarations"""
    source = 'void main() { int x = 1; float y = 2.0; string z = "3"; }'
    assert Parser(source).parse() == "success"


# ========== If Statements (6 tests) ==========
def test_if_simple():
    """32. Simple if"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_if_with_block():
    """33. If with block"""
    source = "void main() { if (1) { printInt(1); } }"
    assert Parser(source).parse() == "success"


def test_if_else():
    """34. If-else"""
    source = "void main() { if (1) printInt(1); else printInt(0); }"
    assert Parser(source).parse() == "success"


def test_if_else_blocks():
    """35. If-else with blocks"""
    source = "void main() { if (1) { printInt(1); } else { printInt(0); } }"
    assert Parser(source).parse() == "success"


def test_if_nested():
    """36. Nested if"""
    source = "void main() { if (1) if (2) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_if_complex_condition():
    """37. If with complex condition"""
    source = "void main() { if (x > 5 && y < 10) printInt(1); }"
    assert Parser(source).parse() == "success"


# ========== While Statements (4 tests) ==========
def test_while_simple():
    """38. Simple while"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_with_block():
    """39. While with block"""
    source = "void main() { while (1) { printInt(1); } }"
    assert Parser(source).parse() == "success"


def test_while_complex_condition():
    """40. While with complex condition"""
    source = "void main() { while (x < 10 && y > 0) x = x + 1; }"
    assert Parser(source).parse() == "success"


def test_while_nested():
    """41. Nested while"""
    source = "void main() { while (1) while (2) printInt(1); }"
    assert Parser(source).parse() == "success"


# ========== For Statements (6 tests) ==========
def test_for_simple():
    """42. Simple for loop"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_for_with_block():
    """43. For with block"""
    source = "void main() { for (int i = 0; i < 10; ++i) { printInt(i); } }"
    assert Parser(source).parse() == "success"


def test_for_no_init():
    """44. For without init"""
    source = "void main() { for (; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_for_no_condition():
    """45. For without condition"""
    source = "void main() { for (auto i = 0; ; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_for_no_update():
    """46. For without update"""
    source = "void main() { for (auto i = 0; i < 10; ) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_for_minimal():
    """47. For with all parts empty"""
    source = "void main() { for (;;) printInt(1); }"
    assert Parser(source).parse() == "success"


# ========== Switch Statements (7 tests) ==========
def test_switch_simple():
    """48. Simple switch"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_switch_multiple_cases():
    """49. Switch with multiple cases"""
    source = """
    void main() { 
        switch (x) { 
            case 1: printInt(1); break; 
            case 2: printInt(2); break; 
        } 
    }
    """
    assert Parser(source).parse() == "success"


def test_switch_with_default():
    """50. Switch with default"""
    source = """
    void main() { 
        switch (x) { 
            case 1: printInt(1); break; 
            default: printInt(0); 
        } 
    }
    """
    assert Parser(source).parse() == "success"


def test_switch_empty():
    """51. Empty switch"""
    source = "void main() { switch (x) { } }"
    assert Parser(source).parse() == "success"


def test_switch_fallthrough():
    """52. Switch with fallthrough"""
    source = """
    void main() { 
        switch (x) { 
            case 1: 
            case 2: printInt(1); break; 
        } 
    }
    """
    assert Parser(source).parse() == "success"


def test_switch_expression_case():
    """53. Switch with expression in case"""
    source = "void main() { switch (x) { case 1+2: printInt(3); break; } }"
    assert Parser(source).parse() == "success"


def test_switch_default_first():
    """54. Switch with default first"""
    source = """
    void main() { 
        switch (x) { 
            default: printInt(0); 
            case 1: printInt(1); break; 
        } 
    }
    """
    assert Parser(source).parse() == "success"


# ========== Break and Continue (4 tests) ==========
def test_break_in_while():
    """55. Break in while"""
    source = "void main() { while (1) { break; } }"
    assert Parser(source).parse() == "success"


def test_continue_in_while():
    """56. Continue in while"""
    source = "void main() { while (1) { continue; } }"
    assert Parser(source).parse() == "success"


def test_break_in_for():
    """57. Break in for"""
    source = "void main() { for (;;) { break; } }"
    assert Parser(source).parse() == "success"


def test_continue_in_for():
    """58. Continue in for"""
    source = "void main() { for (;;) { continue; } }"
    assert Parser(source).parse() == "success"


# ========== Return Statements (5 tests) ==========
def test_return_void():
    """59. Return void"""
    source = "void main() { return; }"
    assert Parser(source).parse() == "success"


def test_return_int():
    """60. Return int"""
    source = "int getValue() { return 42; }"
    assert Parser(source).parse() == "success"


def test_return_expression():
    """61. Return expression"""
    source = "int add(int a, int b) { return a + b; }"
    assert Parser(source).parse() == "success"


def test_return_function_call():
    """62. Return function call"""
    source = "int wrapper() { return getValue(); }"
    assert Parser(source).parse() == "success"


def test_return_in_if():
    """63. Return in if"""
    source = "int check(int x) { if (x > 0) return 1; return 0; }"
    assert Parser(source).parse() == "success"


# ========== Expressions (15 tests) ==========
def test_expr_literal_int():
    """64. Integer literal expression"""
    source = "void main() { 42; }"
    assert Parser(source).parse() == "success"


def test_expr_literal_float():
    """65. Float literal expression"""
    source = "void main() { 3.14; }"
    assert Parser(source).parse() == "success"


def test_expr_literal_string():
    """66. String literal expression"""
    source = 'void main() { "hello"; }'
    assert Parser(source).parse() == "success"


def test_expr_addition():
    """67. Addition expression"""
    source = "void main() { auto x = 1 + 2; }"
    assert Parser(source).parse() == "success"


def test_expr_subtraction():
    """68. Subtraction expression"""
    source = "void main() { auto x = 5 - 3; }"
    assert Parser(source).parse() == "success"


def test_expr_multiplication():
    """69. Multiplication expression"""
    source = "void main() { auto x = 3 * 4; }"
    assert Parser(source).parse() == "success"


def test_expr_division():
    """70. Division expression"""
    source = "void main() { auto x = 10 / 2; }"
    assert Parser(source).parse() == "success"


def test_expr_modulus():
    """71. Modulus expression"""
    source = "void main() { auto x = 10 % 3; }"
    assert Parser(source).parse() == "success"


def test_expr_comparison():
    """72. Comparison expression"""
    source = "void main() { auto x = 5 < 10; }"
    assert Parser(source).parse() == "success"


def test_expr_equality():
    """73. Equality expression"""
    source = "void main() { auto x = 5 == 5; }"
    assert Parser(source).parse() == "success"


def test_expr_logical_and():
    """74. Logical AND expression"""
    source = "void main() { auto x = 1 && 2; }"
    assert Parser(source).parse() == "success"


def test_expr_logical_or():
    """75. Logical OR expression"""
    source = "void main() { auto x = 1 || 0; }"
    assert Parser(source).parse() == "success"


def test_expr_unary_minus():
    """76. Unary minus expression"""
    source = "void main() { auto x = -5; }"
    assert Parser(source).parse() == "success"


def test_expr_unary_not():
    """77. Unary NOT expression"""
    source = "void main() { auto x = !flag; }"
    assert Parser(source).parse() == "success"


def test_expr_complex():
    """78. Complex expression"""
    source = "void main() { auto x = (a + b) * (c - d) / e; }"
    assert Parser(source).parse() == "success"


# ========== Increment/Decrement (4 tests) ==========
def test_prefix_increment():
    """79. Prefix increment"""
    source = "void main() { ++x; }"
    assert Parser(source).parse() == "success"


def test_postfix_increment():
    """80. Postfix increment"""
    source = "void main() { x++; }"
    assert Parser(source).parse() == "success"


def test_prefix_decrement():
    """81. Prefix decrement"""
    source = "void main() { --x; }"
    assert Parser(source).parse() == "success"


def test_postfix_decrement():
    """82. Postfix decrement"""
    source = "void main() { x--; }"
    assert Parser(source).parse() == "success"


# ========== Member Access (3 tests) ==========
def test_member_access():
    """83. Member access"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p; auto val = p.x; }
    """
    assert Parser(source).parse() == "success"


def test_member_assignment():
    """84. Member assignment"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p; p.x = 10; }
    """
    assert Parser(source).parse() == "success"


def test_member_increment():
    """85. Member increment"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p; p.x++; }
    """
    assert Parser(source).parse() == "success"


# ========== Function Calls (5 tests) ==========
def test_function_call_no_args():
    """86. Function call without arguments"""
    source = "void main() { getValue(); }"
    assert Parser(source).parse() == "success"


def test_function_call_one_arg():
    """87. Function call with one argument"""
    source = "void main() { printInt(42); }"
    assert Parser(source).parse() == "success"


def test_function_call_multiple_args():
    """88. Function call with multiple arguments"""
    source = "void main() { add(1, 2, 3); }"
    assert Parser(source).parse() == "success"


def test_function_call_nested():
    """89. Nested function calls"""
    source = "void main() { printInt(add(1, 2)); }"
    assert Parser(source).parse() == "success"


def test_function_call_in_expression():
    """90. Function call in expression"""
    source = "void main() { auto x = getValue() + 10; }"
    assert Parser(source).parse() == "success"


# ========== Struct Initialization (3 tests) ==========
def test_struct_init_empty():
    """91. Empty struct initialization"""
    source = """
    struct Empty { };
    void main() { Empty e = {}; }
    """
    assert Parser(source).parse() == "success"


def test_struct_init_with_values():
    """92. Struct initialization with values"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p = {10, 20}; }
    """
    assert Parser(source).parse() == "success"


def test_struct_init_nested():
    """93. Nested struct initialization"""
    source = """
    struct Point { int x; int y; };
    struct Line { Point start; Point end; };
    void main() { Line l = {{0, 0}, {10, 10}}; }
    """
    assert Parser(source).parse() == "success"


# ========== Block Statements (2 tests) ==========
def test_block_nested():
    """94. Nested blocks"""
    source = "void main() { { { printInt(1); } } }"
    assert Parser(source).parse() == "success"


def test_block_with_declarations():
    """95. Block with declarations"""
    source = "void main() { { int x = 1; int y = 2; auto z = x + y; } }"
    assert Parser(source).parse() == "success"


# ========== Assignment Expressions (3 tests) ==========
def test_assignment_simple():
    """96. Simple assignment"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"


def test_assignment_chained():
    """97. Chained assignment"""
    source = "void main() { int x; int y; int z; x = y = z = 10; }"
    assert Parser(source).parse() == "success"


def test_assignment_in_expression():
    """98. Assignment in expression"""
    source = "void main() { int x; int y; y = (x = 5) + 7; }"
    assert Parser(source).parse() == "success"


# ========== Complex Programs (2 tests) ==========
def test_complete_program():
    """99. Complete program"""
    source = """
    struct Point { int x; int y; };
    
    int add(int a, int b) {
        return a + b;
    }
    
    void main() {
        auto x = 10;
        auto y = 20;
        auto sum = add(x, y);
        printInt(sum);
        
        Point p = {x, y};
        p.x = p.x + 1;
        printInt(p.x);
    }
    """
    assert Parser(source).parse() == "success"


def test_factorial_program():
    """100. Factorial program"""
    source = """
    int factorial(int n) {
        if (n <= 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }
    
    void main() {
        auto num = readInt();
        auto result = factorial(num);
        printInt(result);
    }
    """
    assert Parser(source).parse() == "success"
