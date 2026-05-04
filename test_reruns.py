import pytest, random


VERSION = '1.2.0'

@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_1():
    assert random.choice([True, False])

@pytest.mark.flaky(reruns=2, reruns_delay=2, condition=VERSION == '1.2.0')
class TestReruns:
    def test_2(self):
        assert random.choice([True, False])

    def test_3(self):
        assert random.choice([True, False])