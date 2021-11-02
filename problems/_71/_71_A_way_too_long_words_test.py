import io
from unittest.mock import patch

import pytest

from test.utils import load_test_files
from ._71_A_way_too_long_words import main

test_data = load_test_files(__file__)


@pytest.mark.parametrize("provided_input,expected_output", test_data)
def test(provided_input, expected_output):
    with patch('sys.stdin', io.StringIO(provided_input)), \
            patch('sys.stdout', new_callable=io.StringIO) as stdout:
        main()

        assert stdout.getvalue() == expected_output
