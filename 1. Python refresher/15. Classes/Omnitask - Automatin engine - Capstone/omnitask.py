"""
Project Requirements (The Architecture)
The Contract (ABCs): Create an Abstract Base Class BaseTask that forces every task to have an execute() method.
The Metadata (Dataclasses): Use a @dataclass to store TaskResult (status, execution_time, error_message).
The Security (Decorators): Create a @requires_auth decorator that checks a user's role before allowing a task to run.
The Validation (Descriptors): Create a Priority descriptor that ensures a task's priority is always between 1 and 10.
The Logic (Methods/Attributes): Use Class Variables to track how many tasks have been run across the whole system.
The Interface (Protocols): Use a Logger protocol so you can swap out different logging styles (File vs. Console).
The Modern Touch (Generators): Create a method that "yields" tasks one by one from a queue to save memory.
"""

import time
import functools
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol, List, Optional

# --- 1. THE DATA (Dataclasses) ---
@dataclass
class TaskResult:
    task_name: str
    success: bool
    duration: float
    message: str

# --- 2. THE INTERFACE (Protocols) ---
class Logger(Protocol):
    def log(self, message: str) -> None: ...

class ConsoleLogger:
    def log(self, message: str):
        print(f"[LOG]: {message}")

# --- 3. THE VALIDATION (Descriptors) ---
class PriorityValue:
    """Hint: Use __set_name__ and __set__ to keep priority 1-10."""
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, obj, value):
        # TODO: Implement logic to ensure 1 <= value <= 10
        if not (1 <= value <= 10):
            raise ValueError("Priority must be between 1 and 10")
        obj.__dict__[self.name] = value

# --- 4. THE SECURITY (Decorators) ---
def requires_auth(func):
    """Hint: Mock a user check. If not authorized, raise PermissionError."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Add a check for 'is_admin' or similar logic
        return func(*args, **kwargs)
    return wrapper

# --- 5. THE BLUEPRINT (ABCs) ---
class BaseTask(ABC):
    priority = PriorityValue()

    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority

    @abstractmethod
    def execute(self) -> str:
        """Subclasses must implement this."""
        pass

# --- 6. THE IMPLEMENTATION (Inheritance/Polymorphism) ---
class BackupTask(BaseTask):
    @requires_auth
    def execute(self) -> str:
        # TODO: Simulate a backup
        return "Database backup completed successfully."

class CleanupTask(BaseTask):
    def execute(self) -> str:
        # TODO: Simulate cleaning temp files
        return "Temporary files removed."

# --- 7. THE ENGINE (Composition & Generators) ---
class TaskEngine:
    # TODO: Use a class variable to track total tasks executed globally
    total_executed = 0

    def __init__(self, logger: Logger):
        self.logger = logger
        self.tasks: List[BaseTask] = []

    def add_task(self, task: BaseTask):
        self.tasks.append(task)

    def task_generator(self):
        """Hint: Use 'yield' to provide tasks one by one."""
        for task in self.tasks:
            yield task

    def run_all(self):
        """
        Hint: Iterate through the generator, time the execution,
        update the class variable, and log the result.
        """
        for task in self.task_generator():
            start = time.perf_counter()
            try:
                msg = task.execute()
                success = True
            except Exception as e:
                msg = str(e)
                success = False
            
            end = time.perf_counter()
            # TODO: Create a TaskResult object and log it
            TaskEngine.total_executed += 1
            self.logger.log(f"Ran {task.name} in {end-start:.4f}s. Result: {msg}")

# --- TEST YOUR ENGINE ---
if __name__ == "__main__":
    engine = TaskEngine(ConsoleLogger())
    
    # Create tasks
    t1 = BackupTask("DailyBackup", priority=10)
    t2 = CleanupTask("CacheClear", priority=2)
    
    engine.add_task(t1)
    engine.add_task(t2)
    
    engine.run_all()
    print(f"Grand Total Tasks Run: {TaskEngine.total_executed}")