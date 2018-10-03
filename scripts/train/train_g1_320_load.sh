cd ~/depth2room/vid2vid
python train.py --name depth2room_320_1 --dataroot datasets/sceneNet --input_nc 1 \
--loadSize 320 --n_downsample_G 2 --n_frames_total 5 --n_scales_spatial 3 --num_D 3 \
--niter_fix_global 10 --max_frames_per_gpu 4 --max_dataset_size 10 --tf_log \
--load_pretrain checkpoints/depth2room_320_0 --display_freq 10
