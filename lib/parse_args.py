from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()

    parser.add_argument('--ip', '-i', required=True)
    parser.add_argument('--port', '-p', required=True)

    return parser.parse_args()