import output_parser 
import apply_changes

parser = output_parser
appChange = apply_changes
changes = parser.parse()

appChange.copy_file()
