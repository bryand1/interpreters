import src.headlines
import src.util


def test_headlines():
    h1 = 'Apple stock reaches one trillion dollars'
    lexer = src.headlines.Lexer(h1)
    interpreter = src.headlines.Interpreter(lexer)
    result = interpreter.expr()
    assert result == ['Apple', 'stock', 'reaches', 'one', 'trillion', 'dollars']

    h1 = 'Tesla ends flirtation with going private as Elon Musk cites belief that company is “better off”'
    lexer = src.headlines.Lexer(h1)
    interpreter = src.headlines.Interpreter(lexer)
    result = interpreter.expr()
    expected = ['Tesla', 'ends', 'flirtation', 'with', 'going', 'private', 'as', 'Elon', 'Musk', 'cites',
                'belief', 'that', 'company', 'is', ['better', 'off']]
    assert result == expected


def test_flatten():
    x = ['a', 'b', ['c', 'd']]
    result = src.util.flatten(x)
    assert result == "a b 'c d'"
