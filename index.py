import reset_files
import diff
import apply_changes
import shutil

app_change = reset_files
diff_creator = diff
change_applier = apply_changes

app_change.reset_file1v1()
diff_creator.create_diff()

shutil.copy('diff_output.patch', 'perm_diff.patch') #creates permanent copy of diff file so don't have to regen every time it is changed

change_applier.apply_changes([0,1,2,3])