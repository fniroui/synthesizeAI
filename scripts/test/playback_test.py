import os
from pathlib import Path
import argparse
import streamlit as st
import numpy as np
import cv2
from PIL import Image


parser = argparse.ArgumentParser(description='format')
parser.add_argument('--dir', type=str, default= 'vid2vid/datasets/sceneNet', help='Dataset directory')
parser.add_argument('--res', type=str, default= 'vid2vid/results/depth2room_320_8g', help='Result directory')
parser.add_argument('--num', type=int, default= 1, help='Number of result versions')


def load_img(test_A, test_B, result, indx, seq_len):
    imgs = []
    caption = ['Input', 'Real']
    
    img = cv2.resize(cv2.imread(test_A),(320, 256), interpolation = cv2.INTER_CUBIC)
    imgs.append(img)
    img = cv2.resize(cv2.imread(test_B),(320, 256), interpolation = cv2.INTER_CUBIC)
    imgs.append(img)

    caption_num = 0

    for f in sorted(os.listdir(result)):
        fake_pth = os.path.join(result, f)
        fake_imgs = sorted(os.listdir(fake_pth))

        caption_num += 1
        caption.append('Fake ' + str(caption_num))

        if indx < (seq_len - len(fake_imgs)):
            img = cv2.resize(cv2.imread(test_B),(320, 256), interpolation = cv2.INTER_CUBIC)
            imgs.append(img)
        else:
            fake_path = fake_pth + '/' + fake_imgs[indx]
            img = cv2.resize(cv2.imread(fake_path),(320, 256), interpolation = cv2.INTER_CUBIC)
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

    st.title('depth2room results:')
    animation = st.empty()
    progress_bar = st.empty()
    
    for i in range(seq_len):
        imgs, imgs_caption = load_img(test_A + '/' + input_imgs[i], test_B + '/' + real_imgs[i], result, i, seq_len)
        animation.image(imgs, caption = imgs_caption, clamp=True)
        progress_bar.progress(int((i + 1.0) / seq_len * 100))
