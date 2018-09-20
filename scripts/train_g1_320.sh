python vid2vid/train.py --name depth2room_320 --dataroot datasets/sceneNet --input_nc 1 \
--loadSize 320 --n_frames_total 8 --niter_step 2 --niter_fix_global 8 --niter_decay 5 --num_D 1 \
--load_pretrain checkpoints/label2city_512 --n_downsample_G 2 --max_frames_per_gpu 2 \
--n_scales_spatial 2 --tf_log
