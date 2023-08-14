# kitti2bag_lio

## 0 功能
[KITTI数据集](https://www.cvlibs.net/datasets/kitti/index.php)常用来评估SLAM系统的定位精度。其raw data给出了时间同步和非同步两种类型的数据，[kitti2bag](https://github.com/tomas789/kitti2bag)等官方推荐的转ROSbag工具，只能转换时间同步格式的数据，由于源数据做了时间同步，因此生成的bag中IMU与Lidar一样，仅有10Hz的频率，这显然不适用LIO，VIO系统。此工具整合了Ge Yao的代码[Sensor-Fusion](https://github.com/AlexGeControl/Sensor-Fusion)，可以方便快捷的将kitti数据集转换成具有高频IMU输出的ROS bag.

## 1 使用方法

### a 测试环境
- Ubuntu 20.04
- ROS Noetic

```bash
pip install pykitti 
```

### b 下载数据集
为了保留高频的IMU信息，需要下载未同步的数据，在[kitti官网](https://www.cvlibs.net/datasets/kitti/raw_data.php?type=city)上分别下载，**unsynced+unrectified data**, **synced+rectified data**以及**calibration**三个文件。

解压后按照以下目录整理(以kitti 07为例)
```
2011_09_30
   ├── 2011_09_30_drive_0027_extract
   │   ├── image_00
   │   ├── image_01
   │   ├── image_02
   │   ├── image_03
   │   ├── oxts
   │   └── velodyne_points
   ├── 2011_09_30_drive_0027_sync
   │   ├── image_00
   │   ├── image_01
   │   ├── image_02
   │   ├── image_03
   │   ├── oxts
   │   └── velodyne_points
   ├── calib_cam_to_cam.txt
   ├── calib_imu_to_velo.txt
   └── calib_velo_to_cam.txt
```

### c 开始转换
将仓库内的3个文件置于2011_09_30同一级目录下
运行
```bash
python kitti2bag_lio.py -d 2011_09_30 -s 0027
```
会得到如下输出
```bash
Generating 100Hz oxts ...
count                        11555
mean     0 days 00:00:00.009999798
std      0 days 00:00:00.000154661
min                0 days 00:00:00
25%      0 days 00:00:00.009966160
50%      0 days 00:00:00.009999566
75%      0 days 00:00:00.010031838
max      0 days 00:00:00.019960406
Name: timestamp, dtype: object

Successfully generate 100Hz oxts

Generating 100Hz bag
Exporting static transformations
Exporting time dependent transformations
Exporting IMU
Exporting camera 0
| |                                               | 1105 Elapsed Time: 0:00:08
Exporting camera 1
| |                                               | 1105 Elapsed Time: 0:00:05
Exporting camera 2
| |                                               | 1105 Elapsed Time: 0:00:17
Exporting camera 3
| |                                               | 1105 Elapsed Time: 0:00:14
Exporting velodyne data
| |                                               | 1105 Elapsed Time: 0:01:24
OVERVIEW 
path:        kitti_2011_09_30_drive_0027_synced.bag
version:     2.0
duration:    1:55s (115s)
start:       Sep 30 2011 12:40:25.07 (1317357625.07)
end:         Sep 30 2011 12:42:20.41 (1317357740.41)
size:        5.8 GB
messages:    67729
compression: none [4445/4445 chunks]
types:       geometry_msgs/TwistStamped [98d34b0043a2093cf9d9345ab6eef12e]
             sensor_msgs/CameraInfo     [c9a58c1b0b154e0e6da7578cb991d214]
             sensor_msgs/Image          [060021388200f6f0f447d0fcd9c64743]
             sensor_msgs/Imu            [6a62c6daae103f4ff57a132d6f95cec2]
             sensor_msgs/NavSatFix      [2d3a8cd499b9b4a0249fb98fd05cfa48]
             sensor_msgs/PointCloud2    [1158d486dd51d683ce2f1be655c3c181]
             tf2_msgs/TFMessage         [94810edda583a504dfda3829e70d7eec]
topics:      /kitti/camera_color_left/camera_info     1106 msgs    : sensor_msgs/CameraInfo    
             /kitti/camera_color_left/image_raw       1106 msgs    : sensor_msgs/Image         
             /kitti/camera_color_right/camera_info    1106 msgs    : sensor_msgs/CameraInfo    
             /kitti/camera_color_right/image_raw      1106 msgs    : sensor_msgs/Image         
             /kitti/camera_gray_left/camera_info      1106 msgs    : sensor_msgs/CameraInfo    
             /kitti/camera_gray_left/image_raw        1106 msgs    : sensor_msgs/Image         
             /kitti/camera_gray_right/camera_info     1106 msgs    : sensor_msgs/CameraInfo    
             /kitti/camera_gray_right/image_raw       1106 msgs    : sensor_msgs/Image         
             /kitti/oxts/gps/fix                     11555 msgs    : sensor_msgs/NavSatFix     
             /kitti/oxts/gps/vel                     11555 msgs    : geometry_msgs/TwistStamped
             /kitti/oxts/imu                         11555 msgs    : sensor_msgs/Imu           
             /kitti/velo/pointcloud                   1106 msgs    : sensor_msgs/PointCloud2   
             /tf                                     11555 msgs    : tf2_msgs/TFMessage        
             /tf_static                              11555 msgs    : tf2_msgs/TFMessage

Successfully generate 2011_09_30_drive_0027_100hz.bag

```
转换成功，生成2011_09_30_drive_0027_100hz.bag

### 注
此工具未整合Ge Yao提到的，删除用未同步数据生成的bag中的tf数据，用同步的bag替换的功能。

## 附  KITTI 序列对应关系

| No. | Sequence Name         |
|-----|-----------------------|
| 00  | 2011_10_03_drive_0027 |
| 01  | 2011_10_03_drive_0042 |
| 02  | 2011_10_03_drive_0034 |
| 03  | 2011_09_26_drive_0067 |
| 04  | 2011_09_30_drive_0016 |
| 05  | 2011_09_30_drive_0018 |
| 06  | 2011_09_30_drive_0020 |
| 07  | 2011_09_30_drive_0027 |
| 08  | 2011_09_30_drive_0028 |
| 09  | 2011_09_30_drive_0033 |
| 10  | 2011_09_30_drive_0034 |