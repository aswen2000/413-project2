import shutil

def reset_file1v1():
    source_file = 'perm_copy.java'
    destination_file = 'file1v1.java'
    shutil.copy(source_file, destination_file)

def reset_diff_output():
    source_file = 'perm_diff.patch'
    destination_file = 'diff_output.patch'
    shutil.copy(source_file, destination_file)




