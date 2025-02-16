import sys
from pathlib import Path

def add_project_root_to_path():
    """Add the project root directory to Python path"""
    project_root = Path(__file__).parent.parent
    if str(project_root) not in sys.path:
        sys.path.append(str(project_root)) 