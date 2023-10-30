import shutil

def copy_file():
    # Define the source and destination file paths
    source_file = 'file1v1.java'  # Replace with the path to your original Java file
    destination_file = 'temp_file.java'  # Replace with the desired destination path for the copy

    # Copy the file
    shutil.copy(source_file, destination_file)

def apply_change(change):
    file_name = "temp_file.java"
    #{'old_line': 6, 'new_line': 5, 'flag': '-', 'content': '    int x = 0;\n'}
    
    old_line = change['old_line']
    content = change['content']
    #print(content)
    for row in content:
        line_content = row['line_content']
        flag = row['flag']
        print(flag, line_content)
            # Read the Java file
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Check if the line number is valid
        if 1 <= old_line <= len(lines):
            # Update the line
            if(flag == '-'):
                lines[old_line - 1] = ""
            elif(flag == '+'):
                lines.insert(old_line - 1, line_content)
            with open(file_name, 'w') as file:
                file.writelines(lines)
                print("file changed")




