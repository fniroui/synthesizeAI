cd ~/depth2room/vid2vid
python train.py --name depth2room_320_8g --dataroot datasets/sceneNet --input_nc 1 \
--loadSize 320 --gpu_ids 0,1,2,3,4,5,6,7 --n_gpus_gen 4 --n_frames_total 8 \
--niter_step 2 --niter_fix_global 8 --num_D 3 --load_pretrain checkpoints/depth2room_320_2 \
--n_scales_spatial 2 --tf_log --display_freq 100 --max_dataset_size 50
