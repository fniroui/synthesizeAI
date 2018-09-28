import os
import argparse
from pathlib import Path
from shutil import copyfile
import numpy as np
from PIL import Image 

parser = argparse.ArgumentParser(description='format')
parser.add_argument('--dir', type=str, default= '~/dataset/0/', help='location where sceneNet dataset is extracted from home directory')
parser.add_argument('--keep',  action='store_true', help='Call to keep copy images instead of moving them')
parser.add_argument('--color',  action='store_true', help='Do not convert to black & white')
parser.add_argument('--seq_num',  type=int, default=100, help='Number of sequences to process')


def _sort_dir(dir_list):
    dir_list.sort(key=lambda f: int(f.rsplit(os.path.extsep, 1)[0].rsplit(None,1)[-1]))
    return dir_list
  

if __name__ == '__main__':
    args = parser.parse_args()

    home = str(Path.home())
    in_dir = args.dir.replace('~', home)
    out_dir = './vid2vid/datasets/sceneNet/'

    assert os.path.isdir(in_dir), '%s is not a valid directory' % in_dir
    assert os.path.isdir(out_dir), 'vid2vid repo not found within depth2room'

    seq_num = 0

    dir_list = _sort_dir(os.listdir(in_dir))
    
    for seq in dir_list:
        print('Processing sequence ' + str(seq_num) + '.')

        in_dir_A = os.path.join(in_dir, seq + '/depth')
        in_dir_B = os.path.join(in_dir, seq + '/photo')

        out_dir_A = os.path.join(out_dir, 'train_A/seq' + str(seq_num).zfill(4))
        out_dir_B = os.path.join(out_dir, 'train_B/seq' + str(seq_num).zfill(4))

        if not os.path.exists(out_dir_A): 
            os.makedirs(out_dir_A)
        if not os.path.exists(out_dir_B): 
            os.makedirs(out_dir_B)

        for _, _, fnames in sorted(os.walk(in_dir_A)):
            data_num = 0
            fnames = _sort_dir(fnames)

            for fname in fnames:
                in_depth_name = os.path.join(in_dir_A, fname)
                in_rgb_name = os.path.join(in_dir_B, fname.replace('png', 'jpg'))

                out_depth_name = os.path.join(out_dir_A, str(seq_num).zfill(4) + '_' + str(data_num).zfill(4) + '.png')
                out_rgb_name = os.path.join(out_dir_B, str(seq_num).zfill(4) + '_' + str(data_num).zfill(4) + '.jpg')

                if args.keep:
                    copyfile(in_depth_name, out_depth_name)
                    if args.color:
                        copyfile(in_rgb_name, out_rgb_name)
                    else:
                        img = Image.open(in_rgb_name).convert('L')
                        img.save(out_rgb_name)
                else:
                    os.rename(in_depth_name, out_depth_name)
                    if args.color:
                        os.rename(in_rgb_name, out_rgb_name)
                    else:
                        img = Image.open(in_rgb_name).convert('L')
                        img.save(out_rgb_name)
                        os.remove(in_rgb_name)

                data_num += 1

        seq_num += 1 
        if seq_num >= args.seq_num: break 
