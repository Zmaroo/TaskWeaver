import sys
import os

# Add the project directory to sys.path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "project"))
sys.path.append(project_dir)

from .cli import __main__

def main():
    __main__.main()

if __name__ == "__main__":
    main()
