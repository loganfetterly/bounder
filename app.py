import sys
from classes.Bounder import Bounder as bd 

print()
print("Running your script.. ", sys.argv[0])

if (len(sys.argv) != 2):
    print("Usage: python app.py <your_test_text_file>")
else:
    x = bd(sys.argv[1])
    x.printOutput()