import sys
import os
import argparse
import subprocess
from pathlib import Path

# Add root to sys.path so we can import src.shared.utils
sys.path.append(os.getcwd())
try:
    from src.shared.utils import get_project_path
except ImportError:
    # Fallback if src.shared isn't found immediately (e.g. initial run)
    def get_project_path(day_number):
        src_dir = Path("src")
        day_str = f"day_{day_number:03d}"
        for category in src_dir.iterdir():
            if category.is_dir():
                for project in category.iterdir():
                    if project.is_dir() and project.name.startswith(day_str):
                        return project
        return None

def run_day(day_number):
    project_path = get_project_path(day_number)
    if not project_path:
        print(f"Error: Could not find project for Day {day_number}")
        sys.exit(1)
    
    print(f"🚀 Running Day {day_number}: {project_path.name}")
    print(f"📂 Path: {project_path}")
    print("-" * 50)
    
    main_script = project_path / "main.py"
    if not main_script.exists():
        print(f"Error: No main.py found in {project_path}")
        sys.exit(1)

    # Set PYTHONPATH to include root so src.shared is importable
    env = os.environ.copy()
    root_path = os.getcwd()
    env["PYTHONPATH"] = root_path + os.pathsep + env.get("PYTHONPATH", "")
    
    try:
        # Run the script with the updated environment
        subprocess.run([sys.executable, str(main_script)], env=env, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Execution failed with code {e.returncode}")
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        print("\n🛑 Execution interrupted by user.")
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="Manage 100 Days of Data Science Projects")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run a specific day's project")
    run_parser.add_argument("day", type=int, help="Day number (1-100) to run")

    # Test command
    test_parser = subparsers.add_parser("test", help="Run repository tests")

    args = parser.parse_args()
    
    if args.command == "run":
        run_day(args.day)
    elif args.command == "test":
        print("🧪 Running tests...")
        subprocess.run([sys.executable, "-m", "pytest", "tests"], check=False)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
