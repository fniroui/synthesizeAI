python vid2vid/train.py --name depth2room_320 --dataroot datasets/sceneNet --input_nc 1 \
--loadSize 320 --gpu_ids 0,1,2,3,4,5,6,7 --n_gpus_gen 6 --n_frames_total 12 \
--niter_step 2 --niter_decay 5 --niter_fix_global 8 --num_D 3 --load_pretrain checkpoints/label2city_512 \
--n_scales_spatial 2 
