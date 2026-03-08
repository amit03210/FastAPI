"""
Project Requirements (The Architecture)
The Contract (ABCs): Create an Abstract Base Class BaseTask that forces every task to have an execute() method.
The Metadata (Dataclasses): Use a @dataclass to store TaskResult (status, execution_time, error_message).
The Security (Decorators): Create a @requires_auth decorator that checks a user's role before allowing a task to run.
The Validation (Descriptors): Create a Priority descriptor that ensures a task's priority is always between 1 and 10.
The Modern Touch (Generators): Create a method that "yields" tasks one by one from a queue to save memory.
The Logic (Methods/Attributes): Use Class Variables to track how many tasks have been run across the whole system.
The Interface (Protocols): Use a Logger protocol so you can swap out different logging styles (File vs. Console).
"""
"""
Diagram
[ 1. CONTRACT LAYER ]
           BaseTask (ABC) <--------- [ PriorityValue (Descriptor) ]
           /        \                  (Validates 1-10 priority)
          /          \
 [ BackupTask ]  [ CleanupTask ] <--- [ @requires_auth (Decorator) ]
    (Child)         (Child)            (Checks permissions)
          \          /
           \        /
    [ 2. MANAGEMENT LAYER ]
          TaskEngine <--------------- [ ConsoleLogger (Protocol) ]
    (Stores List[BaseTask])             (Handles all output)
               |
               | (task_generator: yield)
               v
    [ 3. EXECUTION LAYER ]
       For task in engine:
          Start Timer
          task.execute()
          End Timer
          Update Global Counter (Class Variable)
          Create TaskResult (Dataclass)

"""
from dataclasses import dataclass
from abc import ABC, abstractmethod
import functools #for metadata of functions
from typing import Protocol, List
import time


@dataclass
class TaskResult:
    task_name: str
    status: bool
    executioin_time: float
    error_message: str

#Descriptor
class PriorityValue:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "__" + name
    
    def __set__(self, obj, value):
        # print(f"Modifying the value of {self.public_name} to {value}")
        if not (1 <= value <= 10):
            raise ValueError("Priority must be between 1 and 10")
        obj.__dict__[self.private_name] = value

    def __get__(self, obj, type=None):
        value = obj.__dict__[self.private_name]
        print(f"Accessing the value of {self.public_name}...")
        print(f"{self.public_name} is {value}")

def require_auth(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Initializing {self.__class__.__name__}....")
        print(f"Security Check:", end=" ")
        if (self.role == 'admin'):
            print(f"Access Granted for {self.__class__.__name__}")
            return func(self, *args, **kwargs)
        else:
            print("Access denied")
    return wrapper
    
class BaseTask(ABC):
    priority = PriorityValue()

    def __init__(self, name: str, priority:int, role: str):
        self.name = name
        self.priority = priority
        self.role = role

    @abstractmethod
    def execute(self, role) -> str:
        pass

class BackupTask(BaseTask):
    @require_auth
    def execute(self):
        print("Executing DailyBackup....")
        return "Database backup completed successfully.\n"

class CleanupTask(BaseTask):
    @require_auth
    def execute(self):
        print("Executing CacheCleaner...")
        return "Temporary Files removed.\n"

#------------Log Protocol--------------
class Logger(Protocol): 
    def log(self, message: str) -> str:
        return message

class ConsoleLogger:
    def log(self, message: str) -> int:
        return message

def print_log_message(logger: Logger, message):
    print(logger.log(message))

#------------------------------------

class TaskEngine:

    total_tasks_executed = 0

    def __init__(self):
        self.tasks = []

    def gen_Task(self):
        for task in self.tasks:
            yield task

    def add_task(self, task: BaseTask):
        self.tasks.append(task)


    def run_Engine(self):
        welcome_message = "--- Starting OmniTask Pipeline ---"
        print_log_message(ConsoleLogger(), welcome_message)
        for task in self.gen_Task():
            start_time = time.perf_counter()
            try:
                msg = task.execute()
                success = True
            except Exception as e:
                msg = str(e)
                success = False
            end_time = time.perf_counter()

            TaskEngine.total_tasks_executed += 1 
            print_log_message(ConsoleLogger(), f"Ran {task.name} in {end_time-start_time:.4f}s. Result: {msg}")

        
if __name__ == "__main__":

    x = BackupTask("Backup Task", 1, 'admin')
    y = CleanupTask("Cleanup Task", 2, 'admin')
    test = TaskEngine()
    test.add_task(x)
    test.add_task(y)
    test.run_Engine()
    print(f"Grand Total Tasks Run: {TaskEngine.total_tasks_executed}")



