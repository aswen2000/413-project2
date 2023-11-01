@Authors: Michael Tretter Alex Swenson

How To Run:

    1. Once extracted to some folder, use git bash to open a git terminal for this location.
        You must cd into 413-project2(Where this README is located) and where index.py should be found
    
    2. ensure that all line endings for the testing java files are LF not CRLF
        This command should work
            git config --global core.autocrlf false
        This was an issue for us and we changed it in VSCode(bottom right)
        There is also a gitattribute file that could help

    3. in this program we will use the commands diff and patch to get the changes, make sure these are accessable in the git bash shell

    4. Make sure to have python(version 3+) installed, along with Java and be able to run at the current folder location
            (Add to PATH if needed).
    
    5. Then in the Git bash shell, run the following command:
            python index.py
    
    This should all work within the shell

