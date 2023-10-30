import re

def parse():
    # Define a regular expression pattern to match the line number information in the diff output
    pattern = r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@.*'

    # Initialize an empty list to store the changes
    changes = []
    current_change = {'old_line': None, 'new_line': None, 'content': []}

    # Open and read the diff_output.txt file
    with open('diff_output.txt', 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                if current_change['content']:
                    changes.append(current_change)
                    current_change = {'old_line': None, 'new_line': None, 'content': []}
                current_change['old_line'] = int(match.group(1))
                current_change['new_line'] = int(match.group(3))
            else:
                if line.startswith('-'):
                    current_change['content'].append({'flag': '-', 'line_content': line[1:]})
                elif line.startswith('+'):
                    current_change['content'].append({'flag': '+', 'line_content': line[1:]})
                else:
                    current_change['content'].append({'flag': ' ', 'line_content': line})

    # Append the last change
    if current_change['content']:
        changes.append(current_change)

    # Print the changes
    #for change in changes:
        #print(change)
    return changes

changes = parse()
