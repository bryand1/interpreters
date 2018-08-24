import src.headlines


def test_headlines():
    h1 = 'Apple stock reaches one trillion dollars'
    lexer = src.headlines.Lexer(h1)
    interpreter = src.headlines.Interpreter(lexer)
    result = interpreter.expr()
    assert result == ['Apple', 'stock', 'reaches', 'one', 'trillion', 'dollars']
