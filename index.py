import reset_files
import diff
import apply_changes
import run_test
import shutil

app_change = reset_files
diff_creator = diff
#change_applier = apply_changes
tester = run_test

app_change.reset_file1v1()
diff_creator.create_diff()
#creates permanent copy of diff file so don't have to regen every time it is changed
shutil.copy('diff_output.patch', 'perm_diff.patch') 

num_changes = diff_creator.get_num_chunks()
changes_index_arr = [item for item in range(0, num_changes)]
current_step = 0


def get_diff_headers():
    app_change.reset_diff_output()
    lines = []

    with open('perm_diff.patch', 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('@@'):
            print(str(line))



def alg1(changes_index_arr, current_step):
    if len(changes_index_arr) == 1:
        return changes_index_arr

    app_change.reset_file1v1()
    first_half, second_half = split_list(changes_index_arr)

    #print(str(changes_index_arr))
    print("===")
    print("Divide: "+str(first_half) + " " + str(second_half))
    #print(str(second_half))

    if tester.run_test(first_half) == 1: #first half has bug
        current_step = current_step + 1
        print("Step: " + str(current_step)+": Fail")

        return alg1(first_half, current_step)
    else:
        current_step = current_step + 1
        print("Step: " + str(current_step)+": Pass")
    if tester.run_test(second_half) == 1: #second half has bug
        current_step = current_step + 1
        print("Step: " + str(current_step)+": Fail")

        return alg1(second_half, current_step)
    else:
        current_step = current_step + 1
        print("Step: " + str(current_step)+": Pass")

    print('interference') #not sure how to handle interference

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]




get_diff_headers()
print("Total Number of Changes: " + str(num_changes))
error_num = alg1(changes_index_arr, current_step)
#print(error_num) 