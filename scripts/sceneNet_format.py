import os
import argparse
from pathlib import Path
from shutil import copyfile

parser = argparse.ArgumentParser(description='format')
parser.add_argument('--dir', type=str, default= '~/Downloads/train/0/', help='location where sceneNet dataset is extracted from home directory')
parser.add_argument('--keep',  action='store_true', help='Call to keep copy images instead of moving them')

if __name__ == '__main__':
    args = parser.parse_args()

    home = str(Path.home())
    in_dir = args.dir.replace('~', home)
    out_dir = './vid2vid/datasets/sceneNet/'

    assert os.path.isdir(in_dir), '%s is not a valid directory' % in_dir
    assert os.path.isdir(out_dir), 'vid2vid repo not found within depth2room'

    seq_num = 0

    dir_list = os.listdir(in_dir)
    dir_list.sort(key=lambda f: int(f.rsplit(os.path.extsep, 1)[0].rsplit(None,1)[-1]))
    
    for f in dir_list:
        in_dir_A = os.path.join(in_dir, f + '/depth')
        in_dir_B = os.path.join(in_dir, f + '/photo')

        out_dir_A = os.path.join(out_dir, 'train_A/seq' + str(seq_num).zfill(4))
        out_dir_B = os.path.join(out_dir, 'train_B/seq' + str(seq_num).zfill(4))

        if not os.path.exists(out_dir_A): 
            os.makedirs(out_dir_A)
        if not os.path.exists(out_dir_B): 
            os.makedirs(out_dir_B)

        for _, _, fnames in sorted(os.walk(in_dir_A)):
            data_num = 0
            fnames.sort(key=lambda f: int(f.rsplit(os.path.extsep, 1)[0].rsplit(None,1)[-1]))

            for fname in fnames:
                in_depth_name = os.path.join(in_dir_A, fname)
                in_rgb_name = os.path.join(in_dir_B, fname.replace('png', 'jpg'))

                out_depth_name = os.path.join(out_dir_A, str(seq_num).zfill(4) + '_' + str(data_num).zfill(4) + '.png')
                out_rgb_name = os.path.join(out_dir_B, str(seq_num).zfill(4) + '_' + str(data_num).zfill(4) + '.jpg')
    
                if args.keep:
                    copyfile(in_depth_name, out_depth_name)
                    copyfile(in_rgb_name, out_rgb_name)
                else:
                    os.rename(in_depth_name, out_depth_name)
                    os.rename(in_rgb_name, out_rgb_name)

                data_num += 1
            
        seq_num += 1