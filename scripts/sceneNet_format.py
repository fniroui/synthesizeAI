import shutil
import argparse
from pathlib import Path

home = str(Path.home())
parser = argparse.ArgumentParser(description='format')

parser.add_argument('--dir', type=str, default= home + '/Downloads/train/0/', help='location where sceneNet dataset is extracted')

if __name__ == '__main__':
    args = parser.parse_args()
    shutil.move(args.dir, "./vid2vid/datasets/sceneNet/")