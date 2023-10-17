from Exercise_11_3_Employee import Employee

def test_give_custom_rise():
    worker = Employee('name', 'lastnmame', 1000)
    worker.give_rise(100)
    assert worker.salary == 1100

def test_give_default_rise():
    worker = Employee('name', 'lastnmame', 1000)
    worker.give_rise()
    assert worker.salary == 6000