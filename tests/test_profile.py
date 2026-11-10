from pathlib import Path
import json
import re
root=Path(__file__).resolve().parents[1]
text=(root/'README.md').read_text()
links=set(re.findall(r"\[[^\]]*\]\(([^)]+)\)",text))
expected=set(json.loads((root/'tests/preserved-links.json').read_text()))
assert expected <= links, f"Removed original links: {expected-links}"
for link in links:
    if not link.startswith(('https://','http://','#','mailto:')):
        assert (root/link.split('#')[0]).exists(), link
assert text.count('| Public |') >= 11
assert text.count('| Private;') == 2
print(f"PASS: all {len(expected)} original destinations preserved; local links and 13-project catalog verified")
