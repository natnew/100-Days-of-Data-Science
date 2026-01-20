import os
import pytest
from pathlib import Path

def test_project_structure():
    """
    Verifies that the src directory structure matches expectation.
    """
    root_dir = Path(os.getcwd())
    src_dir = root_dir / "src"
    
    assert src_dir.exists(), "src directory is missing"
    
    categories = [
        d for d in src_dir.iterdir() 
        if d.is_dir() and d.name not in ["shared", "__pycache__"]
    ]
    assert len(categories) == 9, f"Expected 9 categories, found {len(categories)}"

def test_requirements_file():
    """
    Verifies requirements.txt exists and is not empty.
    """
    req_file = Path("requirements.txt")
    assert req_file.exists(), "requirements.txt is missing"
    assert req_file.stat().st_size > 0, "requirements.txt is empty"

def test_project_folders_created():
    """
    Verifies that we have 100 day folders.
    """
    src_dir = Path("src")
    project_folders = []
    
    for cat in src_dir.iterdir():
        if cat.is_dir():
            for proj in cat.iterdir():
                if proj.is_dir() and proj.name.startswith("day_"):
                    project_folders.append(proj)
                    
    assert len(project_folders) == 100, f"Expected 100 project folders, found {len(project_folders)}"

def test_each_project_has_main_and_readme():
    """
    Verifies that every project folder has a main.py and README.md.
    """
    src_dir = Path("src")
    
    for cat in src_dir.iterdir():
        if cat.is_dir():
            for proj in cat.iterdir():
                if proj.is_dir() and proj.name.startswith("day_"):
                    assert (proj / "main.py").exists(), f"{proj.name} is missing main.py"
                    assert (proj / "README.md").exists(), f"{proj.name} is missing README.md"
