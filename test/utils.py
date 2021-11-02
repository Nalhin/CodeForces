import os
from pathlib import Path
from typing import Tuple, List


def load_test_files(path: str) -> List[Tuple[str, str]]:
    provided_input = [Path(os.path.join(os.path.dirname(path), 'tests', file)).read_text() for file in
                      os.listdir(os.path.join(os.path.dirname(path), 'tests')) if
                      'in' in file]
    expected_output = [Path(os.path.join(os.path.dirname(path), 'tests', file)).read_text() for file in
                       os.listdir(os.path.join(os.path.dirname(path), 'tests')) if
                       'out' in file]

    return [*zip(sorted(provided_input), sorted(expected_output))]
