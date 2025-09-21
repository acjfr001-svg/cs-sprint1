from unit_converter.conversions import (
    to_celsius, to_fahrenheit, meters_to_feet, feet_to_meters, kg_to_lb, lb_to_kg
)
def almost(a,b,eps=1e-6): return abs(a-b) <= eps

def test_temp_roundtrip():
    assert almost(to_celsius(to_fahrenheit(0)), 0)
    assert almost(to_celsius(to_fahrenheit(100)), 100)
    assert almost(to_fahrenheit(to_celsius(32)), 32)

def test_lengths():
    # 1 meter = 3.280839895 ft
    assert almost(feet_to_meters(3.280839895), 1.0)
    assert almost(meters_to_feet(1.0), 3.280839895)

def test_mass():
    # 1 kg = 2.20462262185 lb
    assert almost(lb_to_kg(2.20462262185), 1.0)
    assert almost(kg_to_lb(1.0), 2.20462262185)
