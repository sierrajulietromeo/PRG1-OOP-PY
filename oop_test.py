from oop import PRIORITY, valid_integer, validate_priority, todays_date, Task, ToDo
import re
import pytest
from datetime import datetime

# pip install pytest in the terminal
# pytest -v oop_test.py


def test_01_valid_integer_operations():
    # Test positive integers and their string representations
    for i in range(21):
        assert valid_integer(i) == True
        assert valid_integer(str(i)) == True

    # Test negative integers and their string representations
    for i in range(-20, 0):
        assert valid_integer(i) == False
        assert valid_integer(str(i)) == False

    # Test zero
    for i in [0, -0, +0]:  
        assert valid_integer(i) == True

    # Test invalid inputs (non-numeric characters, empty strings, etc.)
    for i in ['-0', 'A', '0A', '1.0', 'A0', '', ' ', '.']:
        assert valid_integer(i) == False


def test_02_valid_priority_operations():
    # Test valid priorities (no change expected)
    for i in [1, 3, 5, 7]:
        assert validate_priority(i) == i
        assert validate_priority(str(i)) == i 

    # Test invalid priorities (default to 1)
    for i in [0, 2, 4, 6, 8]:
        assert validate_priority(i) == 1
        assert validate_priority(str(i)) == 1

    # Test invalid inputs (non-numeric characters)
    for i in ['A', 'A0', '0A', '.', ' ']:
        assert validate_priority(i) == 1
        assert validate_priority(str(i)) == 1


def test_03_valid_datetime_now_operations():
    # Get the current date and time
    now = datetime.now()

    # Format the date and time string
    expected_date_str = now.strftime("%d/%m/%Y")
    expected_time_str = now.strftime("%H:%M:%S")
    expected_now = expected_date_str + " " + expected_time_str

    actual_now = todays_date()
    assert actual_now == expected_now


def test_04_check_task_attributes():
    now = datetime.now()
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S")

    # Create a Task object 
    task = Task('T1', PRIORITY['LOW']) 

    # Assert task attributes
    assert task.added == formatted_now  # Check if _added matches the formatted datetime
    assert task.title == 'T1'           # Check if _title is 'T1'
    assert task.priority == PRIORITY['LOW']  # Check if _priority is PRIORITY['LOW']


def test_05_check_task_class_rw_accessors():
    x = Task('T1', PRIORITY['LOW'] )  # Create a Task object (You need to implement the Task class)

    # Check 'added' property
    added_descriptor = Task.added.fget  # Get the getter function for 'added'
    assert callable(added_descriptor)    # Assert it's a function (getter exists)
    with pytest.raises(AttributeError):  # Expect setting 'added' to raise an error
        x.added = "new value"

    # Check 'title' property
    title_descriptor = Task.title.fget   # Get the getter function for 'title'
    assert callable(title_descriptor)    # Assert it's a function (getter exists)
    with pytest.raises(AttributeError):  # Expect setting 'title' to raise an error
        x.title = "new title"

    # Check 'priority' property
    priority_descriptor = Task.priority   # Get the property descriptor for 'priority'
    assert callable(priority_descriptor.fget)  # Assert it has a getter function
    assert callable(priority_descriptor.fset)  # Assert it has a setter function


def test_06_task_class_behaviour():
    task = Task('T1', PRIORITY['LOW']) 

    # Test initial priority
    assert task.priority == PRIORITY['LOW']

    # Test setting a valid high priority
    task.priority = PRIORITY['HIGH']
    assert task.priority == PRIORITY['HIGH']

    # Test setting an invalid low priority (should default to LOW)
    task.priority = 0 
    assert task.priority == PRIORITY['LOW']

    # Test setting an invalid high priority (should default to LOW)
    task.priority = 10 
    assert task.priority == PRIORITY['LOW']


def test_07_check_todo_class_functions():
    todo = ToDo()  # Create a ToDo object

    # Check if 'add' is a function
    assert callable(todo.add)

    # Check if 'remove' is a function
    assert callable(todo.remove)

    # Check if 'list' is a function
    assert callable(todo.list)

    # Check if 'task' is a function
    assert callable(todo.task)


def test_08_todo_class_behaviour_add_list():
    tasks = ToDo()
    
    # Add tasks and check returned values (expected to be the current size of the ToDo list)
    assert tasks.add(Task('ACME T1', PRIORITY['LOW'])) == 1
    assert tasks.add(Task('ACME T2', PRIORITY['MEDIUM'])) == 2
    assert tasks.add(Task('ACME T3', PRIORITY['MEDIUM'])) == 3
    assert tasks.add(Task('ACME T4', PRIORITY['HIGH'])) == 4

    # Test list() method
    task_list = tasks.list()
    assert len(task_list) == 4          # Check the number of tasks in the list
    assert len(task_list[0]) == 3     # Check the number of attributes per task (assuming it's 3: added_date, title, priority)

    # Test remove() method
    assert not tasks.remove('ACME T5')   # Removing a non-existent task should return False
    assert tasks.remove('ACME T4')      # Removing an existing task should return True

    # Test list() again after removal
    task_list = tasks.list()
    assert len(task_list) == 3           # Check the number of tasks after removal
    assert task_list[1][1] == 'ACME T2'  # Check the title of the task at index 1


def test_09_todo_class_task_access():
    tasks = ToDo()
    
    # Add tasks and check returned values
    assert tasks.add(Task('ACME T1', PRIORITY['LOW'])) == 1
    assert tasks.add(Task('ACME T2', PRIORITY['MEDIUM'])) == 2

    # Test accessing a non-existent task (expecting an exception)
    with pytest.raises(Exception, match="Task 'ACME T9' Not Found"):
        tasks.task('ACME T9')

    # Test modifying a task's priority through the ToDo object
    tasks.task('ACME T2').priority = PRIORITY['URGENT']
    assert tasks.task('ACME T2').priority == PRIORITY['URGENT']