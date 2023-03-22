from carreira import format_y_axis


def test_anos():
    assert format_y_axis(757.17, None) == '2,1 anos'


def test_ano():
    assert format_y_axis(499.14, None) == '1,4 ano'


def test_0():
    assert format_y_axis(0.0, None) == ''


def test_meses():
    assert format_y_axis(200.0, None) == '6 meses'
