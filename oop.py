from datetime import datetime # use python's built-in datetime module and only import the datetime class from the datatime module ( the double name is confusing, otherwise we will need to use datetime.datetime.now() )

PRIORITY = { "LOW": 1, "MEDIUM": 3, "HIGH": 5, "URGENT": 7 }


def valid_positive_integer(value): # value can be a string or an integer
  try:
    if isinstance(value, float):
      return False
    num = int(value)
    return num > 0
  except:
    return False


def validate_priority(value):  # value can be a string or an integer
  try:
    num = int(value)
    if num in PRIORITY.values():
      return num
    else:
      return PRIORITY["LOW"]
  except:
    return PRIORITY["LOW"]


def todays_date(): 
  return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


class TaskList:
  def __init__(self):
    self._tasks = []
  
  def add(self, task):
    self._tasks.append(task)
    return len(self._tasks)
  
  def remove(self, title):
    for task in self._tasks:
      if task.title == title:
        self._tasks.remove(task)
        return True
    return False
  
  def list(self, priority=0):
    result = []
    for task in self._tasks:
      if priority == 0 or task.priority == priority:
        result.append([task.added, task.title, task.priority])
    return result
  
  def get_task(self, title):
    for task in self._tasks:
      if task.title == title:
        return task
    raise ValueError(f"Task '{title}' Not Found")
  

class Task:
  def __init__(self, title, priority):
    self._title = title
    self._priority = validate_priority(priority)
    self._added = todays_date()
  
  @property
  def added(self):
    return self._added
  
  @property
  def title(self):
    return self._title
  
  @property
  def priority(self):
    return self._priority
  
  @priority.setter
  def priority(self, value):
    self._priority = validate_priority(value)