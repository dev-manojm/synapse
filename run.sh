#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run model training (only if not already trained)
python model/train_model.py

# Start Flask app
python app/main.py
