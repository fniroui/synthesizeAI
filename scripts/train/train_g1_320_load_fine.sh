cd ~/depth2room/vid2vid
python train.py --name depth2room_320_2 --dataroot datasets/sceneNet --input_nc 1 \
--loadSize 320 --n_downsample_G 3 --n_frames_total 4 --n_scales_spatial 3 --num_D 3 \
--niter_fix_global 5 --max_frames_per_gpu 4 --max_dataset_size 1 --tf_log \
--load_pretrain checkpoints/depth2room_320_1 --display_freq 5 --lr 0.0002 \
--niter 5 --niter_decay 5 --niter_step 1

