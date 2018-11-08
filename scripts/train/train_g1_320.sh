cd ~/depth2room/vid2vid
python train.py --name depth2room_320_0 --dataroot datasets/sceneNet --input_nc 1 \
--loadSize 320 --n_downsample_G 2 --n_frames_total 2 --n_scales_spatial 2  --num_D 3 \
--max_frames_per_gpu 4 --max_dataset_size 20 --tf_log \
--load_pretrain checkpoints/label2city_2048 --display_freq 10
