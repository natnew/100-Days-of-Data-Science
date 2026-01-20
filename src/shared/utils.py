import os
import sys
import importlib.util
from pathlib import Path
from dotenv import load_dotenv

# Ensure the root directory is in python path so we can access src.shared
ROOT_DIR = Path(__file__).resolve().parent.parent

def load_project_env():
    """
    Loads environment variables from the root .env file.
    """
    env_path = ROOT_DIR / ".env"
    load_dotenv(env_path)

def get_project_path(day_number: int) -> Path:
    """
    Finds the directory for a specific day number (e.g., 1 -> src/001.../day_001...).
    """
    src_dir = ROOT_DIR / "src"
    day_str = f"day_{day_number:03d}"
    
    for category in src_dir.iterdir():
        if category.is_dir():
            for project in category.iterdir():
                if project.is_dir() and project.name.startswith(day_str):
                    return project
    return None

def verify_structure():
    """
    Checks if essential project structure exists.
    """
    return (ROOT_DIR / "src").exists() and (ROOT_DIR / "requirements.txt").exists()
