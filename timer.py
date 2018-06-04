import argparse

import time

from tqdm import tqdm


def main(args):
    num_seconds = 60**2 * args['hours'] + 60 * args['minutes'] + args['seconds']
    for i in tqdm(range(num_seconds)):
        time.sleep(1)
    _beep()


def _beep():
    for _ in range(3):
        for _ in range(3):
            print('\a')
            time.sleep(.1)
        time.sleep(.5)


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--hours', required=False, default=0, type=int)
    parser.add_argument('-m', '--minutes', required=False, default=0, type=int)
    parser.add_argument('-s', '--seconds', required=False, default=0, type=int)
    args = vars(parser.parse_args())
    return args


if __name__ == '__main__':
    args = _parse_args()
    main(args)
