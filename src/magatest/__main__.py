import importlib
import os
import pathlib
import sys
import traceback


def import_tests():
    files = pathlib.Path('.').glob('**/test_*.py')

    for file in files:
        path = str(file.parent).replace(os.sep, '.')
        file_name = str(file.stem)
        module_path = f'{path}.{file_name}'
        module = importlib.import_module(module_path)
        _call_tests(module=module)


def _call_tests(module):
    for item in dir(module):
        if item.startswith('test_'):
            test_function = getattr(module, item)
            try:
                test_function()
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
