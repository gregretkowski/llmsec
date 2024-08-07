import csv
import os

class LLMSec:
    def __init__(self):
        self.harmful_behaviors = []
        csv_path = os.path.join(os.path.dirname(__file__), 'data', 'harmful_behaviors.csv')
        with open(csv_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.harmful_behaviors.append(row['goal'])

    def check_user_prompt(self, message):
        """
        Check if the user prompt is malicious and return a probability.

        Args:
            message (str): The user's message to check.

        Returns:
            float: A probability (between 0 and 1) that the message is malicious.
        """
        return self.harmful_behaviors.get(message, 0.0)
