import io
from unittest.mock import patch

import pytest

from test.utils import load_test_files
from ._231_A_team import main

test_data = load_test_files(__file__)


@pytest.mark.parametrize("provided_input,expected_output,input_index", test_data)
def test(provided_input, expected_output, input_index):
    with patch('sys.stdin', io.StringIO(provided_input)), \
            patch('sys.stdout', new_callable=io.StringIO) as stdout:
        main()

        assert stdout.getvalue() == expected_output, f"Test for input {input_index} failed"