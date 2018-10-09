# synthesize.AI

<!-- <p align='center'>  
  <img src='images/result_50.gif' width='640'/>  
</p> -->

An implementation of [Video-to-Video Synthesis](https://tcwang0509.github.io/vid2vid/) for real-time synthesis of coloured image sequences from depth image stream, designed for more robust robotic development in simulated environments. 

## Prerequisites
- Ubuntu 16.04 LTS
- Python 3
- NVIDIA GPU (compute capability 6.0+) & CUDA cuDNN
- PyTorch 0.4 or higher

## Setup
### Installation
- Install the required python libraries:
    ```bash
    pip install dominate requests streamlit
    ```
- Clone this repository to your home folder:
    ```bash
    git clone https://github.com/fniroui/synthesizeAI.git
    cd depth2room
    ```
- Clone the forked version of the [vid2vid](https://github.com/NVIDIA/vid2vid) repository which has been modified for this project:
    ```bash
    git clone https://github.com/fniroui/vid2vid.git
    cd vid2vid
    ```
- Download and compile a snapshot of [FlowNet2](https://github.com/NVIDIA/flownet2-pytorch) by running:
    ```
    python scripts/download_flownet2.py
    ```
- Download the FlowNet2 checkpoint:
    ```
    python scripts/download_models_flownet2.py
    ```

### Dataset
- The [SceneNet RGB-D](https://robotvault.bitbucket.io/scenenet-rgbd.html) dataset is used in this project. Download the complete or partial training dataset.
- Navigate to the synthesizeAI directory and run:
    ```
    python scripts/data/sceneNet_format.py --dir "sceneNet directory"
    ```
    with the directory of the downloaded dataset to move and format the dataset to `./vid2vid/datasets/Scenenet`.

### Testing
- Download the model and extract it to the `.vid2vid/checkpoints` folder:
    ```
    https://drive.google.com/open?id=1ppXTHXsFaGB-vrNjJlPswWuVDrMka3zg
    ```
- To use the provided test sequence located at `./vid2vid/dataset/sceneNet/test_A and test_B`, run `bash scripts/test/test_320.bash` or:
    ```
    bash scripts/test/test_320.bash
    ```

### Training
- Download the dataset and format it by following the above instructions.
- If you have a single GPU, run `bash scripts/train/train_g1_320.sh` or:
    ```bash
    cd ~/depth2room/vid2vid
    python train.py --name depth2room_320_0 --dataroot datasets/sceneNet --input_nc 1 --loadSize 320 --n_downsample_G 2 --n_frames_total 2 --n_scales_spatial 2 -num_D 3 --max_frames_per_gpu 4 --max_dataset_size 20 --tf_log --display_freq 10
    ```
- For multi-GPU training, run `bash scripts/train/train_320.sh ` or:
    ```bash
    cd ~/depth2room/vid2vid
    python train.py --name depth2room_320_8g --dataroot datasets/sceneNet --input_nc 1 --loadSize 320 --gpu_ids 0,1,2,3,4,5,6,7 --n_gpus_gen 4 --n_frames_total 6 --niter_step 2 --niter_fix_global 8 --num_D 3 --n_scales_spatial 2 --tf_log --display_freq 100 --max_dataset_size 50
    ```

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/fniroui/depth2room/blob/master/LICENSE.txt) file for details and the license of the other projects used within this repository. 

## Attribution
Thank you to
[Ting-Chun Wang](https://tcwang0509.github.io/)<sup>1</sup>, [Ming-Yu Liu](http://mingyuliu.net/)<sup>1</sup>, [Jun-Yan Zhu](http://people.csail.mit.edu/junyanz/)<sup>2</sup>, [Guilin Liu](https://liuguilin1225.github.io/)<sup>1</sup>, Andrew Tao<sup>1</sup>, [Jan Kautz](http://jankautz.com/)<sup>1</sup>, and [Bryan Catanzaro](http://catanzaro.name/)<sup>1</sup> for their fantastic work on [Video-to-Video Synthesis](https://tcwang0509.github.io/vid2vid/). 

<sup>1</sup>NVIDIA Corporation, <sup>2</sup>MIT CSAIL
