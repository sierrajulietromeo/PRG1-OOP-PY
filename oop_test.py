import pytest
from datetime import datetime
from oop import PRIORITY, valid_positive_integer, validate_priority, todays_date, TaskList, Task 

# pip install pytest in the terminal
# pytest -v oop_test.py
# pytest -v oop_test.py::test_valid_positive_integer (runs a specific test)


# Test validPositiveInteger
def test_valid_positive_integer():
    assert valid_positive_integer(10) == True
    assert valid_positive_integer('10') == True
    assert valid_positive_integer(25) == True
    assert valid_positive_integer('25') == True
    assert valid_positive_integer(100) == True
    assert valid_positive_integer('100') == True
    assert valid_positive_integer(3) == True
    assert valid_positive_integer('3') == True

    # Test invalid cases
    assert valid_positive_integer(-100) == False
    assert valid_positive_integer(-25) == False
    assert valid_positive_integer(-0) == False
    assert valid_positive_integer(0.0) == False
    assert valid_positive_integer(1.0) == False
    assert valid_positive_integer(1.2) == False
    assert valid_positive_integer(-1.0) == False
    assert valid_positive_integer('-0') == False
    assert valid_positive_integer('A') == False
    assert valid_positive_integer('0A') == False
    assert valid_positive_integer('1.0') == False
    assert valid_positive_integer('') == False
    assert valid_positive_integer(' ') == False
    assert valid_positive_integer('.') == False

# Test validatePriority
def test_validate_priority():
    # Test integer priorities
    assert validate_priority(1) == PRIORITY["LOW"]
    assert validate_priority(3) == PRIORITY["MEDIUM"]
    assert validate_priority(5) == PRIORITY["HIGH"]
    assert validate_priority(7) == PRIORITY["URGENT"]
       
    # Test string priorities
    assert validate_priority('1') == PRIORITY["LOW"]
    assert validate_priority('3') == PRIORITY["MEDIUM"]
    assert validate_priority('5') == PRIORITY["HIGH"]
    assert validate_priority('7') == PRIORITY["URGENT"]

    # Test invalid priorities
    assert validate_priority(0) == PRIORITY["LOW"]
    assert validate_priority(2) == PRIORITY["LOW"]
    assert validate_priority(4) == PRIORITY["LOW"]
    assert validate_priority(6) == PRIORITY["LOW"]
    assert validate_priority(8) == PRIORITY["LOW"]
    assert validate_priority('A') == PRIORITY["LOW"]
    assert validate_priority('A0') == PRIORITY["LOW"]
    assert validate_priority('0A') == PRIORITY["LOW"]
    assert validate_priority('.') == PRIORITY["LOW"]
    assert validate_priority(' ') == PRIORITY["LOW"]

# Test todaysDate
def test_todays_date():
    # Get the current system time
    current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    assert todays_date() == current_time

def test_task_private_attributes():
    # Test that private attributes exist
    task = Task("T1", PRIORITY["LOW"])
    assert hasattr(task, "_added")
    assert hasattr(task, "_title")
    assert hasattr(task, "_priority")

def test_task_added_property():
    # Test that added is a read-only property and has the correct format
    task = Task("T1", PRIORITY["LOW"])
    assert isinstance(task.added, str)  # Should be a string in the correct format

    # Verify that added is read-only by attempting to set it
    with pytest.raises(AttributeError):
        task.added = "02/01/2024 00:00:00"

def test_task_title_property():
    # Test that title is a read-only property
    task = Task("T1", PRIORITY["LOW"])
    assert task.title == "T1"  # Should return the correct title

    # Verify that title is read-only by attempting to set it
    with pytest.raises(AttributeError):
        task.title = "NEW TITLE"

def test_task_priority_property():
    # Test priority getter and setter using PRIORITY dictionary
    task = Task("T1", PRIORITY["LOW"])
    assert task.priority == PRIORITY["LOW"]

    # Test setting priority to valid values
    task.priority = PRIORITY["HIGH"]
    assert task.priority == PRIORITY["HIGH"]

    # Test setting priority to invalid values (should default to LOW)
    task.priority = 0
    assert task.priority == PRIORITY["LOW"]

    task.priority = 10
    assert task.priority == PRIORITY["LOW"]

def test_tasklist_methods_exist():
    # Test that TaskList has the required methods
    task_list = TaskList()
    assert hasattr(task_list, "add")
    assert hasattr(task_list, "remove")
    assert hasattr(task_list, "list")
    assert hasattr(task_list, "get_task")

def test_tasklist_add_and_list_tasks():
    # Test adding tasks and listing them
    task_list = TaskList()
    task1 = Task("ACME T1", PRIORITY["LOW"])
    task2 = Task("ACME T2", PRIORITY["MEDIUM"])
    task3 = Task("ACME T3", PRIORITY["MEDIUM"])
    task4 = Task("ACME T4", PRIORITY["HIGH"])

    assert task_list.add(task1) == 1
    assert task_list.add(task2) == 2
    assert task_list.add(task3) == 3
    assert task_list.add(task4) == 4

    # Verify the list of tasks
    task_list_items = task_list.list()
    assert len(task_list_items) == 4
    assert task_list_items[0][1] == "ACME T1"
    assert task_list_items[1][1] == "ACME T2"
    assert task_list_items[2][1] == "ACME T3"
    assert task_list_items[3][1] == "ACME T4"

def test_tasklist_remove_task():
    # Test removing a task
    task_list = TaskList()
    task1 = Task("ACME T1", PRIORITY["LOW"])
    task2 = Task("ACME T2", PRIORITY["MEDIUM"])
    task3 = Task("ACME T3", PRIORITY["MEDIUM"])
    task4 = Task("ACME T4", PRIORITY["HIGH"])

    task_list.add(task1)
    task_list.add(task2)
    task_list.add(task3)
    task_list.add(task4)

    # Remove a task and verify
    assert task_list.remove("ACME T4") == True
    assert len(task_list.list()) == 3

    # Try to remove a non-existent task
    assert task_list.remove("ACME T5") == False

def test_tasklist_get_task_access_and_modification():
    # Test accessing and modifying a task
    task_list = TaskList()
    task1 = Task("ACME T1", PRIORITY["LOW"])
    task2 = Task("ACME T2", PRIORITY["MEDIUM"])

    task_list.add(task1)
    task_list.add(task2)

    # Access and modify a task
    assert task_list.get_task("ACME T2").priority == PRIORITY["MEDIUM"]
    task_list.get_task("ACME T2").priority = PRIORITY["URGENT"]
    assert task_list.get_task("ACME T2").priority == PRIORITY["URGENT"]

def test_tasklist_get_task_not_found():
    # Test accessing a non-existent task
    task_list = TaskList()
    task1 = Task("ACME T1", PRIORITY["LOW"])
    task_list.add(task1)

    # Verify that accessing a non-existent task raises an error
    with pytest.raises(ValueError, match="Task 'ACME T9' Not Found"):
        task_list.get_task("ACME T9")

def test_tasklist_priority_filtering():
    # Test priority filtering in list method
    task_list = TaskList()
    task1 = Task("ACME T1", PRIORITY["LOW"])
    task2 = Task("ACME T2", PRIORITY["MEDIUM"])
    task3 = Task("ACME T3", PRIORITY["MEDIUM"])
    task4 = Task("ACME T4", PRIORITY["HIGH"])

    task_list.add(task1)
    task_list.add(task2)
    task_list.add(task3)
    task_list.add(task4)

    # Test filtering by MEDIUM priority
    medium_tasks = task_list.list(PRIORITY["MEDIUM"])
    assert len(medium_tasks) == 2
    assert medium_tasks[0][1] == "ACME T2"
    assert medium_tasks[1][1] == "ACME T3"
    
    # Test filtering by HIGH priority
    high_tasks = task_list.list(PRIORITY["HIGH"])
    assert len(high_tasks) == 1
    assert high_tasks[0][1] == "ACME T4"
    
    # Test priority=0 returns all tasks
    all_tasks = task_list.list(0)
    assert len(all_tasks) == 4