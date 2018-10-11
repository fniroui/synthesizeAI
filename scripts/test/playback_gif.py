import os
from pathlib import Path
import argparse
import numpy as np
import cv2
from PIL import Image
import imageio


parser = argparse.ArgumentParser(description='format')
parser.add_argument('--dir', type=str, default= 'vid2vid/datasets/sceneNet', help='Dataset directory')
parser.add_argument('--res', type=str, default= 'vid2vid/results/depth2room_320_8g', help='Result directory')
parser.add_argument('--num', type=int, default= 1, help='Number of result versions')


def depth_norm(img, depth_min = 0.0, depth_max = 5.0):
    """Normalizes the depth image
    img       : depth image
    depth_min : minimum depth range (m)
    depth_max : maximum depth range (m)
    """

    img = 255.0*(1.0 - (img - 1000.0*depth_min) / (1000.0*(depth_max - depth_min)))
    return img.astype(np.uint8)

 
def load_img(test_A, test_B, result, indx):
    """Loads images at a given index.
    test_A : path to the input image 
    test_B : path to the real image
    result : path to the synthesized image
    indx   : index of the sequence
    """

    imgs = []
    caption = ['Input', 'Real']
    
    img = np.array(Image.open(test_A).resize((320, 256)))
    img = cv2.applyColorMap(depth_norm(img), cv2.COLORMAP_JET)
    imgs.append(img)
    img = np.array(Image.open(test_B).convert('RGB').resize((320, 256)))
    imgs.append(img)

    caption_num = 0

    for f in sorted(os.listdir(result)):
        fake_pth = os.path.join(result, f)
        fake_imgs = sorted(os.listdir(fake_pth))

        caption_num += 1
        caption.append('Fake ' + str(caption_num))

        if indx < 2: 
            img = np.array(Image.open(test_B).convert('RGB').resize((320, 256)))
            imgs.append(img)
        else:
            fake_path = fake_pth + '/' + fake_imgs[indx - 2]
            img = np.array(Image.open(fake_path).convert('RGB').resize((320, 256)))
            imgs.append(img)

    return tuple(imgs), tuple(caption)


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
            imgs, imgs_caption = load_img(test_A + '/' + input_imgs[i], test_B + '/' + real_imgs[i], result, i)
            gif_frame = np.zeros([imgs[0].shape[0], imgs[0].shape[1] * len(imgs), 3])
            
            for j in range(len(imgs)):
                gif_frame[:, j*imgs[0].shape[1] : j*imgs[0].shape[1] + imgs[0].shape[1]] = imgs[j]
            
            writer.append_data(gif_frame)
