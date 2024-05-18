from datetime import datetime

from carreira.__main__ import format_y_axis, format_date


def test_format_date():
    assert format_date('19/05/2022') == datetime(2022, 5, 19, 0, 0)


def test_format_y_axis_anos():
    assert format_y_axis(757.17, None) == '2,1 anos'


def test_format_y_axis_ano():
    assert format_y_axis(499.14, None) == '1,4 ano'


def test_format_y_axis_0():
    assert format_y_axis(0.0, None) == ''


def test_format_y_axis_meses():
    assert format_y_axis(200.0, None) == '6 meses'
