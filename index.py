import output_parser 
import apply_changes

parser = output_parser
appChange = apply_changes
changes = parser.parse()

change = changes[3]
appChange.apply_change(change)