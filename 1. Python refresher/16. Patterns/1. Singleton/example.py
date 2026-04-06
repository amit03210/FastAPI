import threading


class SingletonMeta(type):
    """
    This is a 'metaclass' that controls how Singleton classes are created.
    It ensures only one instance of the class exists.
    """

    _instances = {}  # Dictionary to store the single instance
    _lock = threading.Lock()  # Lock for thread safety

    def __call__(cls, *args, **kwargs):
        """
        This method is called when you try to create an object.
        It checks if an instance already exists.
        """
        with cls._lock:  # Prevents multiple threads from creating multiple instances
            if cls not in cls._instances:
                # If no instance exists, create one and save it
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        # Always return the same instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    Example class that uses the SingletonMeta.
    No matter how many times you create it, you get the same object.
    """

    def __init__(self, value):
        self.value = value


# --- Usage Example ---

# First creation
singleton_a = Singleton("First")
print(singleton_a.value)  # Output: First

# Second creation with a different value
singleton_b = Singleton("Second")
print(singleton_b.value)  # Output: First (same instance reused!)

# Check if both are the same object
print(singleton_a is singleton_b)  # Output: True
