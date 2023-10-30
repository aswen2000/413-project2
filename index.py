import output_parser 
import apply_changes

parser = output_parser
appChange = apply_changes
changes = parser.parse()

appChange.copy_file()
offset = 0
change1 = changes[0]
change2 = changes[1]
change3 = changes[2]
change4 = changes[3]
change5 = changes[4]
change6 = changes[5]

offset = appChange.apply_change(change1, offset)
print(offset)
offset = appChange.apply_change(change2, offset)
print(offset)
offset = appChange.apply_change(change3, offset)
print(offset)
offset = appChange.apply_change(change4, offset)
print(offset)
offset = appChange.apply_change(change5, offset)
print(offset)
offset = appChange.apply_change(change6, offset)
print(offset)