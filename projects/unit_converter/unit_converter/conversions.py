def to_celsius(f: float) -> float:
    return (f - 32.0) * (5.0/9.0)

def to_fahrenheit(c: float) -> float:
    return c * (9.0/5.0) + 32.0

def meters_to_feet(m: float) -> float:
    return m * 3.280839895

def feet_to_meters(ft: float) -> float:
    return ft / 3.280839895

def kg_to_lb(kg: float) -> float:
    return kg * 2.20462262185

def lb_to_kg(lb: float) -> float:
    return lb / 2.20462262185
