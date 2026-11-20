# show_structure.py  скрипт показывает структуру проекта убирая «мусорные» папки (.git, __pycache__, виртуальное окружение)
# Запусти в терминале: python show_structure.py
import os

SKIP_DIRS = {'.git', '.idea', '__pycache__', 'venv', '.venv', 'env', 'node_modules', 'migrations', '.vscode'}

def show_structure(root_path, max_depth=None):
    def walk(path, prefix='', depth=0):
        if max_depth is not None and depth > max_depth:
            return
        try:
            with os.scandir(path) as it:
                entries = sorted(it, key=lambda e: (not e.is_dir(follow_symlinks=False), e.name.lower()))
        except (PermissionError, NotADirectoryError, OSError) as e:
            print(prefix + f'[недоступно: {e}]')
            return

        entries = [e for e in entries if e.name not in SKIP_DIRS]
        count = len(entries)
        for i, entry in enumerate(entries):
            is_last = (i == count - 1)
            connector = '└── ' if is_last else '├── '
            print(prefix + connector + entry.name)
            if entry.is_dir(follow_symlinks=False):
                sub_prefix = prefix + ('    ' if is_last else '│   ')
                walk(entry.path, sub_prefix, depth + 1)

    print(os.path.basename(root_path) or root_path)
    walk(root_path)

if __name__ == '__main__':
    show_structure(os.getcwd())
