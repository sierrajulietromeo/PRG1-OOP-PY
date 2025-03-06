# TaskList App

A minimum viable product (MVP) todo list application implementing an object-oriented design with two main classes.

## Overview

The application consists of two key classes that work together:

- `TaskList`: Manages a collection of todo items
- `Todo`: Represents individual todo items

The relationship between these classes is one-to-many: a single `TaskList` instance can manage multiple `Todo` instances.

## Class Diagram

![Todo_TaskList](./images/class_diagram.png)

## Helper Functions

The system requires three helper functions:

### 1. `valid_positive_integer(value)`
- **Accepts**: string or numeric value
- **Returns**: boolean
- **Purpose**: Validates if the input can be represented as a positive integer

```python
valid_positive_integer('10')  # returns True
valid_positive_integer(10)    # returns True
valid_positive_integer('-10') # returns False
valid_positive_integer(0.0)   # returns False
```

### 2. `validate_priority(value)`
- **Accepts**: string or numeric value
- **Returns**: integer (priority value)
- **Valid priorities**:
  - LOW (1)
  - MEDIUM (3)
  - HIGH (5)
  - URGENT (7)
- **Returns LOW (1)** for invalid inputs

```python
validate_priority(1)    # returns 1
validate_priority('7')  # returns 7
validate_priority('A')  # returns 1 (invalid input)
```

### 3. `todays_date()`
- **Returns**: string
- **Format**: 'DD/MM/YYYY HH:MM:SS'
- **Purpose**: Provides current system datetime

```python
todays_date()  # returns e.g., "23/10/2024 09:30:04"
```

## Class Specifications

### `Todo` Class

Represents a single todo item with three private attributes:
- `_title`
- `_priority`
- `_added` (automatically set on creation)

#### Example Usage:
```python
todo = Todo('Get Cappuccino', PRIORITY['MEDIUM'])
print(todo.added)    # '23/10/2024 12:26:26'
print(todo.title)    # 'Get Cappuccino'
print(todo.priority) # 3
todo.priority = PRIORITY['URGENT']
print(todo.priority) # 7
```

### `TaskList` Class

Manages a collection of `Todo` items with five main methods:

1. **`__init__()`**: Initialises an empty list to store todos.

2. **`add(todo)`**:
   - Adds a `Todo` instance to the list.
   - **Returns**: Number of todos in the list.

3. **`remove(title)`**:
   - Removes a todo by title (case insensitive).
   - **Returns**: boolean (`True` if removed, `False` if not found).

4. **`list(priority=0)`**:
   - Lists todos, optionally filtered by priority.
   - **Returns**: List of `[added, title, priority]` lists.
   - Priority `0` returns all todos.

5. **`task(title)`**:
   - Retrieves a specific todo by title.
   - **Returns**: `Todo` reference if found.
   - **Raises**: `ValueError` if not found (`Task 'title' Not Found`).

#### Example Usage:
```python
task_list = TaskList()
task_list.add(Todo('Get Cappuccino', PRIORITY['HIGH']))     # returns 1
task_list.add(Todo('Order Lunch', PRIORITY['MEDIUM']))      # returns 2
print(task_list.list(PRIORITY['MEDIUM']))                  # returns matching todos
task_list.task('Order Lunch').priority = PRIORITY['HIGH']   # updates priority
print(task_list.remove('Order Lunch'))                     # returns True
```

## Development Guidelines

1. Implement and test helper functions first.
2. Use private attributes (prefix with `_`) where possible.
3. Refactor for clarity and efficiency.
4. Follow standard Python coding conventions (PEP 8).

---

### Python-Specific Notes:
- Use `@property` decorators for getters and setters.
- Use `datetime` module for date formatting.
- Use `raise ValueError` for error handling.
- Use lists instead of arrays for storing todos.