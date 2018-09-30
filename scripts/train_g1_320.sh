python vid2vid/train.py --name depth2room_320 --dataroot datasets/sceneNet --input_nc 1 \
--loadSize 320 --n_downsample_G 2 --n_frames_total 4 --num_D 2 --niter 20 \
--max_frames_per_gpu 4 --max_dataset_size 50 --tf_log --nThreads 3
