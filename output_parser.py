# Read the diff output from the text file
with open("diff_output.txt", "r") as file:
    diff_output = file.read()

# Create a list of changes
changes = []

current_old_line = None
current_new_line = None
old_code = []
new_code = []

for line in diff_output.splitlines():
    if line.startswith('@@'):
        parts = line.split(' ')
        current_old_line = int(parts[1].split(',')[0][1:])
        current_new_line = int(parts[2].split(',')[0][1:])
        old_code = []
        new_code = []
    elif line.startswith('- '):
        old_code.append(line[2:])
    elif line.startswith('+ '):
        new_code.append(line[2:])
    else:
        if old_code or new_code:
            changes.append({
                "oldLine": current_old_line,
                "newLine": current_new_line,
                "change": {
                    "old": "\n".join(old_code),
                    "new": "\n".join(new_code)
                }
            })
            current_old_line += 1
            current_new_line += 1
            old_code = []
            new_code = []

# Print the results
for change in changes:
    print(f"Old Line: {change['oldLine']}, New Line: {change['newLine']}")
    print(f"Change (Old):\n{change['change']['old']}")
    print(f"Change (New):\n{change['change']['new']}")
    print()
