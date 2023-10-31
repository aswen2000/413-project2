import apply_changes
import run_java

change_applier = apply_changes
java_runner = run_java

def run_test(changes):
    change_applier.apply_changes(changes)
    return java_runner.run_java('file1v1.java', str(5), str(0), 'division')

        