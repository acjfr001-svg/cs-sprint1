import argparse
from .conversions import (
    to_celsius, to_fahrenheit, meters_to_feet, feet_to_meters, kg_to_lb, lb_to_kg
)
MAP = {
    ("F","C"): to_celsius, ("C","F"): to_fahrenheit,
    ("m","ft"): meters_to_feet, ("ft","m"): feet_to_meters,
    ("kg","lb"): kg_to_lb, ("lb","kg"): lb_to_kg
}
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--from", dest="src", required=True)
    p.add_argument("--to", dest="dst", required=True)
    p.add_argument("--value", type=float, required=True)
    a = p.parse_args()
    fn = MAP.get((a.src, a.dst))
    if not fn:
        raise SystemExit(f"Unsupported conversion {a.src}->{a.dst}")
    print(fn(a.value))
