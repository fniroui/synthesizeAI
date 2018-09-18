# depth2room

An implementation of [Video-to-Video Synthesis](https://tcwang0509.github.io/vid2vid/) for real-time translation of depth image stream to photorealistic RGB image stream.

## Prerequisites
- Ubuntu 16.04 LTS
- Python 3
- NVIDIA GPU + CUDA cuDNN
- PyTorch 0.4 or higher

## Setup
### Installation
- Install the required python libraries:
    ```bash
    pip install dominate requests
    ```
- Clone this repository:
    ```bash
    git clone https://github.com/fniroui/depth2room.git
    cd depth2room
    ```
- Clone the forked version of the [vid2vid](https://github.com/NVIDIA/vid2vid) repository which has been modified for this project:
    ```bash
    git clone https://github.com/fniroui/vid2vid.git

### Dataset
- The [SceneNet RGB-D](https://robotvault.bitbucket.io/scenenet-rgbd.html) dataset is used in this project.

### Testing

### Training
    ```

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/fniroui/depth2room/blob/master/LICENSE.txt) file for details and the license of the other projects used within this repository. 

## Attribution
Thank you to
[Ting-Chun Wang](https://tcwang0509.github.io/)<sup>1</sup>, [Ming-Yu Liu](http://mingyuliu.net/)<sup>1</sup>, [Jun-Yan Zhu](http://people.csail.mit.edu/junyanz/)<sup>2</sup>, [Guilin Liu](https://liuguilin1225.github.io/)<sup>1</sup>, Andrew Tao<sup>1</sup>, [Jan Kautz](http://jankautz.com/)<sup>1</sup>, and [Bryan Catanzaro](http://catanzaro.name/)<sup>1</sup> for their fantastic work on [Video-to-Video Synthesis](https://tcwang0509.github.io/vid2vid/). 

<sup>1</sup>NVIDIA Corporation, <sup>2</sup>MIT CSAIL
