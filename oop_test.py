import pytest
from datetime import datetime
from oop import PRIORITY, valid_positive_integer, validate_priority, Todo, todays_date, TaskList

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

    assert valid_positive_integer(-100) == False
    assert valid_positive_integer(-25) == False
    assert valid_positive_integer(-0) == False
    assert valid_positive_integer(0.0) == False
    assert valid_positive_integer(1.0) == True

    # Test invalid cases
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
    # Test valid priorities using PRIORITY dictionary
    assert validate_priority(PRIORITY["LOW"]) == PRIORITY["LOW"]
    assert validate_priority(PRIORITY["MEDIUM"]) == PRIORITY["MEDIUM"]
    assert validate_priority(PRIORITY["HIGH"]) == PRIORITY["HIGH"]
    assert validate_priority(PRIORITY["URGENT"]) == PRIORITY["URGENT"]

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

def test_todo_private_attributes():
    # Test that private attributes exist
    todo = Todo("T1", PRIORITY["LOW"])
    assert hasattr(todo, "_added")
    assert hasattr(todo, "_title")
    assert hasattr(todo, "_priority")

def test_todo_added_property():
    # Test that added is a read-only property and has the correct format
    todo = Todo("T1", PRIORITY["LOW"])
    assert isinstance(todo.added, str)  # Should be a string in the correct format

    # Verify that added is read-only by attempting to set it
    with pytest.raises(AttributeError):
        todo.added = "02/01/2024 00:00:00"

def test_todo_title_property():
    # Test that title is a read-only property
    todo = Todo("T1", PRIORITY["LOW"])
    assert todo.title == "T1"  # Should return the correct title

    # Verify that title is read-only by attempting to set it
    with pytest.raises(AttributeError):
        todo.title = "NEW TITLE"

def test_todo_priority_property():
    # Test priority getter and setter using PRIORITY dictionary
    todo = Todo("T1", PRIORITY["LOW"])
    assert todo.priority == PRIORITY["LOW"]

    # Test setting priority to valid values
    todo.priority = PRIORITY["HIGH"]
    assert todo.priority == PRIORITY["HIGH"]

    # Test setting priority to invalid values (should default to LOW)
    todo.priority = 0
    assert todo.priority == PRIORITY["LOW"]

    todo.priority = 10
    assert todo.priority == PRIORITY["LOW"]

def test_tasklist_methods_exist():
    # Test that TaskList has the required methods
    task_list = TaskList()
    assert hasattr(task_list, "add")
    assert hasattr(task_list, "remove")
    assert hasattr(task_list, "list")
    assert hasattr(task_list, "task")

def test_tasklist_add_and_list_tasks():
    # Test adding tasks and listing them
    task_list = TaskList()
    todo1 = Todo("ACME T1", PRIORITY["LOW"])
    todo2 = Todo("ACME T2", PRIORITY["MEDIUM"])
    todo3 = Todo("ACME T3", PRIORITY["MEDIUM"])
    todo4 = Todo("ACME T4", PRIORITY["HIGH"])

    assert task_list.add(todo1) == 1
    assert task_list.add(todo2) == 2
    assert task_list.add(todo3) == 3
    assert task_list.add(todo4) == 4

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
    todo1 = Todo("ACME T1", PRIORITY["LOW"])
    todo2 = Todo("ACME T2", PRIORITY["MEDIUM"])
    todo3 = Todo("ACME T3", PRIORITY["MEDIUM"])
    todo4 = Todo("ACME T4", PRIORITY["HIGH"])

    task_list.add(todo1)
    task_list.add(todo2)
    task_list.add(todo3)
    task_list.add(todo4)

    # Remove a task and verify
    assert task_list.remove("ACME T4") == True
    assert len(task_list.list()) == 3

    # Try to remove a non-existent task
    assert task_list.remove("ACME T5") == False

def test_tasklist_task_access_and_modification():
    # Test accessing and modifying a task
    task_list = TaskList()
    todo1 = Todo("ACME T1", PRIORITY["LOW"])
    todo2 = Todo("ACME T2", PRIORITY["MEDIUM"])

    task_list.add(todo1)
    task_list.add(todo2)

    # Access and modify a task
    assert task_list.task("ACME T2").priority == PRIORITY["MEDIUM"]
    task_list.task("ACME T2").priority = PRIORITY["URGENT"]
    assert task_list.task("ACME T2").priority == PRIORITY["URGENT"]

def test_tasklist_task_not_found():
    # Test accessing a non-existent task
    task_list = TaskList()
    todo1 = Todo("ACME T1", PRIORITY["LOW"])
    task_list.add(todo1)

    # Verify that accessing a non-existent task raises an error
    with pytest.raises(ValueError, match="Task 'ACME T9' Not Found"):
        task_list.task("ACME T9")