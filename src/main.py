#!/usr/bin/env python3
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer, util
from datetime import datetime

# === CONFIGURATION ===
FILENAME = "context.txt"
SIMILARITY_THRESHOLD = 0.5 # Steering strength

# === LOGGING FUNCTION ===
def write_log(message, log_file="log.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}\n"
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(full_message)

# === LOAD CONTEXT ===
def read_file_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip().lower() for line in file.readlines()]
    
def load_questions(filepath):
    questions = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                questions.append(line)
    return questions

def run_batch(filepath, alpha_values=[0.1, 0.5, 0.9]):
    questions = load_questions(filepath)
    for prompt in questions:
        for alpha in alpha_values:
            write_log("-------------------------------------------------------------------------------------------")
            write_log(f"\nRunning: '{prompt}' with ALPHA={alpha}")
            print(f"Running: '{prompt}' with ALPHA={alpha}")
            # main(prompt, ALPHA=alpha)


if __name__ == "__main__":
    try:
        run_batch('questions.txt')
    except Exception as e:
        write_log(f"Error{str(e)}")
    finally:
        write_log("\n------------------------------------------------------------------------------------------\n")

