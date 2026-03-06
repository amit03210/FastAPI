# FILE: notification_engine.py

"""
SCENARIO: A system that sends alerts via different channels (Email, SMS).
INSTRUCTIONS:
1. Create an ABC 'Sender' that defines an @abstractmethod 'send(message)'.
2. Create 'EmailSender' and 'SMSSender' that implement the 'send' logic.
3. Create an 'AlertSystem' class. 
   - COMPOSITION: Instead of inheriting from Senders, give AlertSystem 
     a list of 'Sender' objects in its __init__.
4. Create a method 'notify_all(msg)' in AlertSystem that loops through 
   the senders and calls their .send() method.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class Sender(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
class SMSSender(Sender):
    def send(self, message):
        return f"{message}, sent via SMS"
    
class EmailSender(Sender):
    def send(self, message):
        return f"{message}, sent via Email"

@dataclass    
class AlertSystem:
   sender_list: list[Sender] = field(default_factory=list)

   def notify_all(self, message):
       return [obj.send(message) for obj in self.sender_list]

lis = [SMSSender(),EmailSender(),SMSSender(),EmailSender()]
alertObj = AlertSystem(sender_list = lis)

response = alertObj.notify_all("Hello david")
for message in response:
    print(message)

