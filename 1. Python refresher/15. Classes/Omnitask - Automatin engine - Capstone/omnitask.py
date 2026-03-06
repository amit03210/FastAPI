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

#Descriptor
class PriorityValue:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "__" + name
    
    def __set__(self, obj, value):
        print(f"Modifying the value of {self.public_name} to {self.private_name}")
        if not (1 <= value <= 10):
            raise ValueError("Priority must be between 1 and 10")
        obj.__dict__[self.private_name] = value

    def __get__(self, obj, type=None):
        value = obj.__dict__[self.private_name]
        print(f"Accessing the value of {self.public_name}...")
        print(f"{self.public_name} is {value}")

class BaseTask(ABC):
    priority = PriorityValue()

    def __init__(self, name: str, priority:int):
        self.name = name
        self.priority = priority

    @abstractmethod
    def execute(self) -> str:
        pass

@dataclass
class TaskResult:
    task_name: str
    status: bool
    executioin_time: float
    error_message: str




