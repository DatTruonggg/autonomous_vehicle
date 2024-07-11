# Autonomous Vehicle
# Quick start

## 1. Create the new environment
Command prompt:

`conda create --name <env_name> python==3.11`

Run file `test.ipynb` in `src` folder. 

## 2. Background 

### 2.1 Traffic sign detection

I use YOLOv5 to train traffic sign detection tasks with the Roboflow custom dataset. YOLOv5 comes in various versions (e.g., YOLOv5s, YOLOv5m, YOLOv5l, YOLOv5x) with varying complexity and accuracy. 

Roboflow data link: https://universe.roboflow.com/vietnam-traffic-sign-detection/vietnam-traffic-sign-detection-2i2j8/dataset/6

**Note**: I use the Roboflow dataset as the main method of traffic sign detection and the Kaggle dataset as a test file.
