from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

print("🚀 Pipeline started")

# Step 1: Ingestion
ingestion = DataIngestion()
train_path, test_path = ingestion.initiate_data_ingestion()

print("📥 Ingestion done")

# Step 2: Transformation
transform = DataTransformation()
train_arr, test_arr, _ = transform.initiate_data_transformation(train_path, test_path)

print("🔄 Transformation done")

# Step 3: Model Training
trainer = ModelTrainer()
trainer.initiate_model_trainer(train_arr, test_arr)

print("✅ Pipeline completed")
