import shutil
import time

def copy_file():
    # Define the source and destination file paths
    source_file = 'file1v1.java'  # Replace with the path to your original Java file
    destination_file = 'temp_file.java'  # Replace with the desired destination path for the copy

    # Copy the file
    shutil.copy(source_file, destination_file)

def apply_change(change, offset):
    file_name = "temp_file.java"
    #{'old_line': 6, 'new_line': 5, 'flag': '-', 'content': '    int x = 0;\n'}
    
    old_line = change['old_line']
    content = change['content']
    new_line = change['new_line']
    diff = new_line - old_line
    #print(content)
    for row in content:
        time.sleep(2)
        line_content = row['line_content']
        flag = row['flag']
        print(flag, line_content)
            # Read the Java file
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Update the line
        if(flag == '-'):
            lines[old_line + offset + diff] = ""
            offset = offset-1
        elif(flag == '+'):
            lines.insert(old_line + offset + diff, line_content)
            offset = offset+1
        with open(file_name, 'w') as file:
            file.writelines(lines)
    return offset





