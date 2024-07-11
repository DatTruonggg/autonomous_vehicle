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

### 2.2 Result 

**Loss**:

**train/box_loss, train/cls_loss, train/dfl_loss**: These loss metrics decrease consistently during training, indicating that the model is learning to predict bounding box locations, classify objects, and estimate distances more accurately.
val/box_loss, val/cls_loss, val/dfl_loss: The validation losses also decrease, suggesting that the model is not overfitting (memorizing the training data). However, there is some fluctuation in the later epochs, possibly due to a small validation set or randomness in the training process.

**Precision and Recall**:

**metrics/precision(B)**: Precision increases over time, showing that the model is making more accurate bounding box predictions.
**metrics/recall(B)**: Recall also increases, indicating that the model is detecting more objects overall.

**mAP (mean Average Precision)**:

**metrics/mAP50(B)**: mAP@0.5 (mean average precision with an IoU threshold of 0.5) increases and reaches a good value (around 0.8), demonstrating the model's strong object detection capabilities.
**metrics/mAP50-95(B)**: mAP@0.5:0.95 (mean average precision across IoU thresholds from 0.5 to 0.95) also increases, but its value is lower than mAP@0.5, suggesting that the model still struggles to predict very precise bounding boxes with high IoU.

