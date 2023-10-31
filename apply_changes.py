def apply_changes(chunks):
    chunk_counter = -1

    with open('diff_output.patch', 'r') as file:
        lines = file.readlines()

        for index, line in enumerate(lines):
            print(line)

            if line.startswith('@@'):
                chunk_counter = chunk_counter + 1
            if not chunk_counter < 0 and not chunk_counter in chunks:
                lines[index] = ""
    print(lines)