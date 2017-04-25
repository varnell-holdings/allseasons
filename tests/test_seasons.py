import seasons
import pytest
from datetime import datetime


def test_astronomical_dates():
    result = seasons.astronomical_dates(2017)
    expected = {'dec': datetime(2017, 12, 21, 16, 27, 48, 281359),
                'june': datetime(2017, 6, 21, 4, 24, 17, 882888),
                'sept': datetime(2017, 9, 22, 20, 1, 41, 290341),
                'march': datetime(2017, 3, 20, 10, 28, 37, 516239)}
    assert result == expected


def test_between_two_values():
    dates = seasons.astronomical_dates(2017)
    july = datetime(2017, 7, 3, 1, 1, 1)
    assert seasons.between(july, 'march', 'sept')
    assert seasons.between(july, 'march', 'dec')
    assert seasons.between(july, 'june', 'sept')
    assert seasons.between(july, 'june', 'dec')
    assert seasons.between(july, 'march', None)
    assert seasons.between(july, 'june', None)
    assert seasons.between(july, None, 'sept')
    assert seasons.between(july, None, 'dec')
    assert not seasons.between(july, 'march', 'june')
    assert not seasons.between(july, 'sept', 'dec')
    assert not seasons.between(july, None, 'march')
    assert not seasons.between(july, None, 'june')
    assert not seasons.between(july, 'sept', None)
    assert not seasons.between(july, 'dec', None)


@pytest.mark.parametrize(('seasonset', 'expected'), [
    (seasons.nh_met, 'summer'),
    (seasons.nh_ast, 'summer'),
    (seasons.sh_met, 'winter'),
    (seasons.sh_ast, 'winter'),
])
def test_get_season_3_july(seasonset, expected):
    date = datetime(1983, 7, 3, 1, 1, 1)
    assert seasonset.get_season(date) == expected


@pytest.mark.parametrize(('seasonset', 'expected'), [
    (seasons.nh_met, 'spring'),
    (seasons.nh_ast, 'winter'),
    (seasons.sh_met, 'autumn'),
    (seasons.sh_ast, 'summer'),
])
def test_get_season_20_march(seasonset, expected):
    """This date falls in between the astronomical and meteorological seasons
    """
    date = datetime(2017, 3,20, 1, 1, 1)
    assert seasonset.get_season(date) == expected