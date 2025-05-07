from app.convert import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_celsius_to_fahrenheit():
    assert round(celsius_to_fahrenheit(0), 2) == 32.00
    assert round(celsius_to_fahrenheit(100), 2) == 212.00

def test_fahrenheit_to_celsius():
    assert round(fahrenheit_to_celsius(32), 2) == 0.00
    assert round(fahrenheit_to_celsius(212), 2) == 100.00