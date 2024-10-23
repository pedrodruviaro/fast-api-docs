# Environment Variables

import os

dog_name = os.getenv("DOG_NAME", "No value for this")
print(dog_name)