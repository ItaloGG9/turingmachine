import os
import shutil

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for root, dirs, files in os.walk(base_dir):
        for d in dirs:
            if d == '__pycache__':
                path = os.path.join(root, d)
                shutil.rmtree(path, ignore_errors=True)
        for f in files:
            if f.endswith('.pyc') or f.endswith('.zip'):
                path = os.path.join(root, f)
                try:
                    os.remove(path)
                except:
                    pass

if __name__ == '__main__':
    main()
