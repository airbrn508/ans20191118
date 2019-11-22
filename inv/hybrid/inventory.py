#!/usr/bin/env python3

def empty_inventory():
    return {'_meta': {'hostsvars': {}}}

if __name__ == "main__":
    parser = argparse.ArgumentParser()
    parser.add_arguent('--list', action = 'store_true')
    parser.add_arguent('--host', action = 'store')
    args = parse.parse_args()

