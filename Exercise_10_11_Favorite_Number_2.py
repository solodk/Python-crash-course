from pathlib import Path
import json

file = Path("favorite_number.json")
content = file.read_text()
content = json.loads(content)

print(f"I know your favorite number! It's {content}")