# The program file_reader.py in this section uses a temporary variable, lines,
# to show how splitlines() works. You can skip the temporary variable and loop
# directly over the list that splitlines() returns:
#   for line in content.splitlines()
# Remove the temporary variable from each of the program in this section, to
# make them more concise.

from pathlib import Path
file = Path('learning_python.txt')
content = file.read_text()
for line in content.splitlines():
    print(line)