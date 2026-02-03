"""
Lexer test cases for TyC compiler
100 comprehensive test cases for lexer covering all tokens and error cases
"""

import pytest
from tests.utils import Tokenizer


# ========== Keywords (16 tests) ==========
def test_keyword_auto():
    """1. Keyword: auto"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_keyword_break():
    """2. Keyword: break"""
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"


def test_keyword_case():
    """3. Keyword: case"""
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"


def test_keyword_continue():
    """4. Keyword: continue"""
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"


def test_keyword_default():
    """5. Keyword: default"""
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"


def test_keyword_else():
    """6. Keyword: else"""
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"


def test_keyword_float():
    """7. Keyword: float"""
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"


def test_keyword_for():
    """8. Keyword: for"""
    tokenizer = Tokenizer("for")
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"


def test_keyword_if():
    """9. Keyword: if"""
    tokenizer = Tokenizer("if")
    assert tokenizer.get_tokens_as_string() == "if,<EOF>"


def test_keyword_int():
    """10. Keyword: int"""
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"


def test_keyword_return():
    """11. Keyword: return"""
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"


def test_keyword_string():
    """12. Keyword: string"""
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"


def test_keyword_struct():
    """13. Keyword: struct"""
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"


def test_keyword_switch():
    """14. Keyword: switch"""
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"


def test_keyword_void():
    """15. Keyword: void"""
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"


def test_keyword_while():
    """16. Keyword: while"""
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"


# ========== Operators (18 tests) ==========
def test_operator_plus():
    """17. Operator: +"""
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"


def test_operator_minus():
    """18. Operator: -"""
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"


def test_operator_mult():
    """19. Operator: *"""
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"


def test_operator_div():
    """20. Operator: /"""
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"


def test_operator_mod():
    """21. Operator: %"""
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"


def test_operator_equal():
    """22. Operator: =="""
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"


def test_operator_notequal():
    """23. Operator: !="""
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"


def test_operator_lt():
    """24. Operator: <"""
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"


def test_operator_gt():
    """25. Operator: >"""
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"


def test_operator_lte():
    """26. Operator: <="""
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"


def test_operator_gte():
    """27. Operator: >="""
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"


def test_operator_or():
    """28. Operator: ||"""
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"


def test_operator_and():
    """29. Operator: &&"""
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"


def test_operator_not():
    """30. Operator: !"""
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"


def test_operator_incr():
    """31. Operator: ++"""
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"


def test_operator_decr():
    """32. Operator: --"""
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"


def test_operator_assign():
    """33. Operator: ="""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_operator_dot():
    """34. Operator: ."""
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"


# ========== Separators (7 tests) ==========
def test_separator_lbrace():
    """35. Separator: {"""
    tokenizer = Tokenizer("{")
    assert tokenizer.get_tokens_as_string() == "{,<EOF>"


def test_separator_rbrace():
    """36. Separator: }"""
    tokenizer = Tokenizer("}")
    assert tokenizer.get_tokens_as_string() == "},<EOF>"


def test_separator_lparen():
    """37. Separator: ("""
    tokenizer = Tokenizer("(")
    assert tokenizer.get_tokens_as_string() == "(,<EOF>"


def test_separator_rparen():
    """38. Separator: )"""
    tokenizer = Tokenizer(")")
    assert tokenizer.get_tokens_as_string() == "),<EOF>"


def test_separator_semi():
    """39. Separator: ;"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_separator_comma():
    """40. Separator: ,"""
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"


def test_separator_colon():
    """41. Separator: :"""
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ":,<EOF>"


# ========== Integer Literals (5 tests) ==========
def test_integer_single_digit():
    """42. Integer: single digit"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_integer_multiple_digits():
    """43. Integer: multiple digits"""
    tokenizer = Tokenizer("12345")
    assert tokenizer.get_tokens_as_string() == "12345,<EOF>"


def test_integer_zero():
    """44. Integer: zero"""
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"


def test_integer_large():
    """45. Integer: large number"""
    tokenizer = Tokenizer("999999999")
    assert tokenizer.get_tokens_as_string() == "999999999,<EOF>"


def test_integer_with_operator():
    """46. Integer: with operator (negative)"""
    tokenizer = Tokenizer("-42")
    assert tokenizer.get_tokens_as_string() == "-,42,<EOF>"


# ========== Float Literals (10 tests) ==========
def test_float_simple():
    """47. Float: simple decimal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_float_zero():
    """48. Float: zero"""
    tokenizer = Tokenizer("0.0")
    assert tokenizer.get_tokens_as_string() == "0.0,<EOF>"


def test_float_leading_zero():
    """49. Float: leading zero"""
    tokenizer = Tokenizer("0.123")
    assert tokenizer.get_tokens_as_string() == "0.123,<EOF>"


def test_float_no_decimal_part():
    """50. Float: no decimal part"""
    tokenizer = Tokenizer("5.")
    assert tokenizer.get_tokens_as_string() == "5.,<EOF>"


def test_float_no_integer_part():
    """51. Float: no integer part"""
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"


def test_float_exponent_positive():
    """52. Float: exponent positive"""
    tokenizer = Tokenizer("1.23e4")
    assert tokenizer.get_tokens_as_string() == "1.23e4,<EOF>"


def test_float_exponent_negative():
    """53. Float: exponent negative"""
    tokenizer = Tokenizer("5.67E-2")
    assert tokenizer.get_tokens_as_string() == "5.67E-2,<EOF>"


def test_float_exponent_only():
    """54. Float: exponent only (no decimal)"""
    tokenizer = Tokenizer("1e4")
    assert tokenizer.get_tokens_as_string() == "1e4,<EOF>"


def test_float_exponent_capital():
    """55. Float: capital E exponent"""
    tokenizer = Tokenizer("2E-3")
    assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"


def test_float_complex():
    """56. Float: complex with exponent"""
    tokenizer = Tokenizer("123.456e+789")
    assert tokenizer.get_tokens_as_string() == "123.456e+789,<EOF>"


# ========== String Literals (10 tests) ==========
def test_string_simple():
    """57. String: simple string"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_string_empty():
    """58. String: empty string"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"


def test_string_with_spaces():
    """59. String: with spaces"""
    tokenizer = Tokenizer('"hello world"')
    assert tokenizer.get_tokens_as_string() == "hello world,<EOF>"


def test_string_escape_backslash():
    """60. String: escape backslash"""
    tokenizer = Tokenizer(r'"hello\\world"')
    assert tokenizer.get_tokens_as_string() == r"hello\\world,<EOF>"


def test_string_escape_quote():
    """61. String: escape quote"""
    tokenizer = Tokenizer(r'"He said \"Hi\""')
    assert tokenizer.get_tokens_as_string() == r'He said \"Hi\",<EOF>'


def test_string_escape_newline():
    """62. String: escape newline"""
    tokenizer = Tokenizer(r'"line1\nline2"')
    assert tokenizer.get_tokens_as_string() == r"line1\nline2,<EOF>"


def test_string_escape_tab():
    """63. String: escape tab"""
    tokenizer = Tokenizer(r'"hello\ttab"')
    assert tokenizer.get_tokens_as_string() == r"hello\ttab,<EOF>"


def test_string_all_escapes():
    """64. String: all valid escapes"""
    tokenizer = Tokenizer(r'"\b\f\r\n\t\"\\"')
    assert tokenizer.get_tokens_as_string() == r'\b\f\r\n\t\"\\ ,<EOF>'


def test_string_special_chars():
    """65. String: special characters"""
    tokenizer = Tokenizer('"!@#$%^&*()"')
    assert tokenizer.get_tokens_as_string() == "!@#$%^&*(),<EOF>"


def test_string_numbers():
    """66. String: with numbers"""
    tokenizer = Tokenizer('"test123"')
    assert tokenizer.get_tokens_as_string() == "test123,<EOF>"


# ========== Identifiers (5 tests) ==========
def test_identifier_simple():
    """67. Identifier: simple"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_identifier_underscore():
    """68. Identifier: with underscore"""
    tokenizer = Tokenizer("_test")
    assert tokenizer.get_tokens_as_string() == "_test,<EOF>"


def test_identifier_with_digits():
    """69. Identifier: with digits"""
    tokenizer = Tokenizer("var123")
    assert tokenizer.get_tokens_as_string() == "var123,<EOF>"


def test_identifier_camelCase():
    """70. Identifier: camelCase"""
    tokenizer = Tokenizer("myVariable")
    assert tokenizer.get_tokens_as_string() == "myVariable,<EOF>"


def test_identifier_all_caps():
    """71. Identifier: all caps"""
    tokenizer = Tokenizer("MAX_VALUE")
    assert tokenizer.get_tokens_as_string() == "MAX_VALUE,<EOF>"


# ========== Comments (4 tests) ==========
def test_line_comment():
    """72. Comment: line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_line_comment_with_code():
    """73. Comment: line comment after code"""
    tokenizer = Tokenizer("auto x = 5; // comment")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,;,<EOF>"


def test_block_comment():
    """74. Comment: block comment"""
    tokenizer = Tokenizer("/* This is a block comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_block_comment_multiline():
    """75. Comment: multiline block comment"""
    tokenizer = Tokenizer("/* Line 1\nLine 2\nLine 3 */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


# ========== Error Cases: ILLEGAL_ESCAPE (7 tests) ==========
def test_error_illegal_escape_x():
    """76. Error: illegal escape \\x"""
    tokenizer = Tokenizer(r'"hello\x"')
    assert "Illegal Escape In String: hello\\x" in tokenizer.get_tokens_as_string()


def test_error_illegal_escape_a():
    """77. Error: illegal escape \\a"""
    tokenizer = Tokenizer(r'"test\a"')
    assert "Illegal Escape In String: test\\a" in tokenizer.get_tokens_as_string()


def test_error_illegal_escape_digit():
    """78. Error: illegal escape \\1"""
    tokenizer = Tokenizer(r'"value\1"')
    assert "Illegal Escape In String: value\\1" in tokenizer.get_tokens_as_string()


def test_error_illegal_escape_space():
    """79. Error: illegal escape with space"""
    tokenizer = Tokenizer(r'"hello\ "')
    assert "Illegal Escape In String: hello\\ " in tokenizer.get_tokens_as_string()


def test_error_illegal_escape_at_start():
    """80. Error: illegal escape at start"""
    tokenizer = Tokenizer(r'"\k"')
    assert "Illegal Escape In String: \\k" in tokenizer.get_tokens_as_string()


def test_error_illegal_escape_multiple():
    """81. Error: illegal escape in middle"""
    tokenizer = Tokenizer(r'"prefix\qsuffix"')
    assert "Illegal Escape In String: prefix\\q" in tokenizer.get_tokens_as_string()


def test_error_illegal_escape_symbol():
    """82. Error: illegal escape with symbol"""
    tokenizer = Tokenizer(r'"test\@end"')
    assert "Illegal Escape In String: test\\@" in tokenizer.get_tokens_as_string()


# ========== Error Cases: UNCLOSE_STRING (7 tests) ==========
def test_error_unclose_string_newline():
    """83. Error: unclosed string with newline"""
    tokenizer = Tokenizer('"hello\n')
    assert "Unclosed String: hello" in tokenizer.get_tokens_as_string()


def test_error_unclose_string_eof():
    """84. Error: unclosed string at EOF"""
    tokenizer = Tokenizer('"hello')
    assert "Unclosed String: hello" in tokenizer.get_tokens_as_string()


def test_error_unclose_string_empty():
    """85. Error: unclosed empty string"""
    tokenizer = Tokenizer('"')
    assert "Unclosed String:" in tokenizer.get_tokens_as_string()


def test_error_unclose_string_with_escape():
    """86. Error: unclosed string with valid escape"""
    tokenizer = Tokenizer(r'"hello\n')
    assert "Unclosed String:" in tokenizer.get_tokens_as_string()


def test_error_unclose_string_carriage_return():
    """87. Error: unclosed string with carriage return"""
    tokenizer = Tokenizer('"test\r')
    assert "Unclosed String: test" in tokenizer.get_tokens_as_string()


def test_error_unclose_string_long():
    """88. Error: unclosed string long text"""
    tokenizer = Tokenizer('"this is a very long string that is not closed')
    assert "Unclosed String:" in tokenizer.get_tokens_as_string()


def test_error_unclose_string_with_spaces():
    """89. Error: unclosed string with spaces"""
    tokenizer = Tokenizer('"hello world\n')
    assert "Unclosed String: hello world" in tokenizer.get_tokens_as_string()


# ========== Error Cases: ERROR_CHAR (3 tests) ==========
def test_error_char_at():
    """90. Error: unrecognized char @"""
    tokenizer = Tokenizer("@")
    assert "Error Token @" in tokenizer.get_tokens_as_string()


def test_error_char_hash():
    """91. Error: unrecognized char #"""
    tokenizer = Tokenizer("#")
    assert "Error Token #" in tokenizer.get_tokens_as_string()


def test_error_char_dollar():
    """92. Error: unrecognized char $"""
    tokenizer = Tokenizer("$")
    assert "Error Token $" in tokenizer.get_tokens_as_string()


# ========== Complex/Mixed Cases (8 tests) ==========
def test_complex_variable_declaration():
    """93. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"


def test_complex_function_declaration():
    """94. Complex: function declaration"""
    tokenizer = Tokenizer("int add(int a, int b) {")
    assert tokenizer.get_tokens_as_string() == "int,add,(,int,a,,,int,b,),{,<EOF>"


def test_complex_if_statement():
    """95. Complex: if statement"""
    tokenizer = Tokenizer("if (x < 10) { return x; }")
    assert tokenizer.get_tokens_as_string() == "if,(,x,<,10,),{,return,x,;,},<EOF>"


def test_complex_for_loop():
    """96. Complex: for loop"""
    tokenizer = Tokenizer("for (auto i = 0; i < 10; ++i)")
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,10,;,++,i,),<EOF>"


def test_complex_struct_declaration():
    """97. Complex: struct declaration"""
    tokenizer = Tokenizer("struct Point { int x; int y; };")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,int,y,;,},;,<EOF>"


def test_complex_member_access():
    """98. Complex: member access"""
    tokenizer = Tokenizer("p.x = 10;")
    assert tokenizer.get_tokens_as_string() == "p,.,x,=,10,;,<EOF>"


def test_complex_logical_expression():
    """99. Complex: logical expression"""
    tokenizer = Tokenizer("(x > 5) && (y < 10) || !flag")
    assert tokenizer.get_tokens_as_string() == "(,x,>,5,),&&,(,y,<,10,),||,!,flag,<EOF>"


def test_complex_string_in_function():
    """100. Complex: string in function call"""
    tokenizer = Tokenizer('printString("Hello, World!");')
    assert tokenizer.get_tokens_as_string() == "printString,(,Hello, World!,),;,<EOF>"

