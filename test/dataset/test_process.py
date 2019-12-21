import pytest
import pandas as pd

from pts.dataset import ProcessStartField, ProcessDataEntry


@pytest.mark.parametrize(
    "freq, expected",
    [
        ("B", "2019-11-01"),
        ("W", "2019-11-03"),
        ("M", "2019-11-30"),
        ("12M", "2019-11-30"),
        ("A-DEC", "2019-12-31"),
    ],
)
def test_process_start_field(freq, expected):
    process = ProcessStartField.process
    given = "2019-11-01 12:34:56"

    assert process(given, freq) == pd.Timestamp(expected, freq)
