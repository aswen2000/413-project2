import reset_files
import diff
import shutil

app_change = reset_files
diff_creator = diff

app_change.reset_file1v1()
diff_creator.create_diff()

shutil.copy('diff_output.patch', 'perm_diff.patch') #creates permanent copy of diff file so don't have to regen every time it is changed