import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="User management add to parse json file and store locally")
    parser.add_argument('--export', help="flag won’t take any arguments, default value is False with missing")
    parser.add_argument("destination", help="Path to the inventory JSON file")
    return parser
