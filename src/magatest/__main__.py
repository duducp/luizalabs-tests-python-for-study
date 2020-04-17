import importlib
import os
import traceback, sys


def import_tests():
    IDENTIFICATION_FILES = 'test_'
    IGNORED_PREFIX = '__pycache__'
    IGNORE_FILES = []

    for dirpath, dirnames, filenames in os.walk("."):
        if IGNORED_PREFIX in dirpath:
            continue

        for file in filenames:
            if file.startswith(IDENTIFICATION_FILES) and file not in IGNORE_FILES:
                filename_no_ext, _ = os.path.splitext(os.path.join(dirpath, file))
                filename_no_ext = filename_no_ext[2:]
                module_path = filename_no_ext.replace(os.sep, ".")
                imported = importlib.import_module(module_path)

                for item in dir(imported):
                    if item.startswith('test_'):
                        test_method = getattr(imported, item)
                        try:
                            test_method()
                            print(
                                f'\033[92m Test {item} passed =D'
                            )
                        except Exception:
                            print('\033[93m')
                            print(f'Test {item} failed =(')
                            print('\033[91m')
                            traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    import_tests()
