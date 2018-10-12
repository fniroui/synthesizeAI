import os
from pathlib import Path
import argparse
import numpy as np
import imageio

import playback as pb


parser = argparse.ArgumentParser(description='format')
parser.add_argument('--dir', type=str, default= 'vid2vid/datasets/sceneNet', help='Dataset directory')
parser.add_argument('--res', type=str, default= 'vid2vid/results/depth2room_320_1', help='Result directory')
parser.add_argument('--num', type=int, default= 1, help='Number of result versions')


if  __name__ == '__main__':
    args = parser.parse_args()
    test_A = os.path.join(Path(__file__).parents[2], args.dir + '/test_A')
    test_B = os.path.join(Path(__file__).parents[2], args.dir + '/test_B')
    result = os.path.join(Path(__file__).parents[2], args.res + '/test_latest')

    test_A = os.path.join(test_A, os.listdir(test_A)[0])
    test_B = os.path.join(test_B, os.listdir(test_B)[0])

    input_imgs = sorted(os.listdir(test_A))
    real_imgs = sorted(os.listdir(test_B))

    frame_size = (256, 320)
    seq_len = len(sorted(os.listdir(test_A)))
    
    with imageio.get_writer('result.gif', mode='I', duration=0.12) as writer:
        for i in range(seq_len):
            imgs, imgs_caption = pb.load_img(test_A + '/' + input_imgs[i], test_B + '/' + real_imgs[i], result, i)
            gif_frame = np.zeros([imgs[0].shape[0], imgs[0].shape[1] * len(imgs), 3])
            
            for j in range(len(imgs)):
                gif_frame[:, j*imgs[0].shape[1] : j*imgs[0].shape[1] + imgs[0].shape[1]] = imgs[j]
            
            writer.append_data(gif_frame)
