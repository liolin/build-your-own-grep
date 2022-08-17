import sys

from dataclasses import dataclass

# import pyparsing - available if you need it!
# import lark - available if you need it!

if sys.argv[1] != "-E":
    print("Expected first argument to be '-E'")
    exit(1)

pattern = sys.argv[2]
input = sys.stdin.read()

if len(pattern) == 1:
    if input.count(pattern) > 0:
        exit(0)
    else:
        exit(1)
else:
    print(f"Unhandled pattern: {pattern}")