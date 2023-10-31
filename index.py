import reset_files
import diff
import apply_changes
import run_test
import shutil

app_change = reset_files
diff_creator = diff
change_applier = apply_changes
tester = run_test

app_change.reset_temp_copy()
diff_creator.create_diff()
shutil.copy('diff_output.patch', 'perm_diff.patch') #creates permanent copy of diff file so don't have to regen every time it is changed

num_changes = diff_creator.get_num_chunks()
changes_index_arr = [item for item in range(0, num_changes)]

print(len(changes_index_arr))

def alg1(changes_index_arr):
    if len(changes_index_arr) == 1:
        return changes_index_arr

    app_change.reset_temp_copy()
    first_half, second_half = split_list(changes_index_arr)

    if tester.run_test(first_half) == 1: #first half has bug
        return alg1(first_half)
    elif tester.run_test(second_half) == 1: #second half has bug
        return alg1(second_half)
    else:
        print('interference') #not sure how to handle interference

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

print(alg1(changes_index_arr))