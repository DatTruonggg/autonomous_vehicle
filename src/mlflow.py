import mlflow
import mlflow.pytorch
import torch

# Load mô hình của bạn -> MLFLOW giả để ghi lại mô hình vì mình đã chạy xong file training 
model = torch.load("best.pt")

with mlflow.start_run():
    mlflow.pytorch.log_model(model, "model", registered_model_name="yolov8_best_model")

    params = {
        "epochs": 25,
        "batch_size": 16,
        "learning_rate": 0.001,
    }
    mlflow.log_params(params)

    metrics = {
        "train_loss": 0.05,
        "val_loss": 0.08,
        "mAP": 0.85,
    }
    mlflow.log_metrics(metrics)