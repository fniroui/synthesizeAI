cd ~/depth2room/vid2vid
python test.py --name depth2room_320 --loadSize 320 --input_nc 1 --n_scales_spatial 3 \
--n_downsample_G 3 --dataroot datasets/sceneNet --use_real_img
