# Load libraries
library(tidyverse)
library(caret)

# --- Load and preprocess data ---
load_and_process_data <- function() {
  # Load dataset
  df <- read.csv("data/train.csv")


  cat("Data loaded successfully. Shape:", dim(df)[1], "rows,", dim(df)[2], "columns\n")

  # Remove duplicates
  df <- df[!duplicated(df), ]
  cat("Duplicates removed. Shape:", dim(df)[1], "rows,", dim(df)[2], "columns\n")

  # Handle missing values
  df <- df %>%
    filter(!is.na(Age), !is.na(Fare), !is.na(Embarked), !is.na(Sex))
  df$Embarked[is.na(df$Embarked)] <- names(sort(table(df$Embarked), decreasing = TRUE))[1]
  cat("Missing values handled.\n")

  # Feature engineering
  df <- df %>%
    mutate(
      FamilySize = SibSp + Parch + 1,
      Sex = ifelse(Sex == "male", 0, 1)
    )
  cat("Feature engineering complete.\n")

  # Select features
  features <- c("Pclass", "Age", "Fare", "Sex", "FamilySize")
  df <- df[, c(features, "Survived", "Name")]

  # Split into train and test
  set.seed(42)
  train_index <- createDataPartition(df$Survived, p = 0.8, list = FALSE)
  train <- df[train_index, ]
  test <- df[-train_index, ]
  cat("Train/Test split complete:", nrow(train), "train rows,", nrow(test), "test rows\n")

  # Train model 
  model <- glm(Survived ~ Pclass + Age + Fare + Sex + FamilySize,
               data = train, family = binomial)
  cat("Model trained successfully.\n")

  # Evaluate
  train_pred <- ifelse(predict(model, newdata = train, type = "response") > 0.5, 1, 0)
  train_acc <- mean(train_pred == train$Survived)
  cat("Training Accuracy:", round(train_acc, 3), "\n")

  # Predict on test
  test$PredictedSurvival <- ifelse(predict(model, newdata = test, type = "response") > 0.5, 1, 0)

  # Save output
  output <- test %>%
    select(Name, PredictedSurvival)
  write.csv(output, "predictions_r.csv", row.names = FALSE)
  cat("Predictions saved to predictions_r.csv\n")

  # Print sample predictions
  cat("\nSample Predictions:\n")
  print(head(output, 10))
}

# Run script
load_and_process_data()
