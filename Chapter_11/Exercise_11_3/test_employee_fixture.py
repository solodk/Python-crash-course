from Exercise_11_3_Employee import Employee
import pytest

@pytest.fixture
def worker():
    instance = Employee('name', 'lastname', 1000)
    return instance

def test_give_custom_rise(worker):
    worker.give_rise(100)
    assert worker.salary == 1100

def test_give_default_rise(worker):
    worker.give_rise()
    assert worker.salary == 6000