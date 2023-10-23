main_menu = [
	"Menu:",
	"Load notes",
	"Show notes",
	"Save notes",
	"Add notes",
	"Find notes",
	"Refactor notes",
	"Remove notes",
	"Exit",
]
menu_error = f'Input Error! Enter number from 1 to {len(main_menu)-1}. Try one more time.'
empty_notes = f'List of notes is empty or not open'
empty_start = f'List of notes is empty. Start by filling out notes'
load_successfull= f'Notes loaded'
new_note = ["Enter header: ",
              "Enter message: "]
save_successfull = f"File successfully saved"
search_request = "Search keyword?"
search_notfind = "No results"
change_note = ["Enter new header. Press enter if you want stay without changes:",
                  "Enter new message. Press enter if you want stay without changes: "]
change_result = f"Note successfully changed"

delete_note = 'Enter header or key word for deleted: '
save_note = "You have changes. Do you want save it? (y/n): "
delete_result = f'Note successfully removed'
good_bay = "Good bye!"


def added_successfull(name: str) -> str:
    title = name.get("title")
    return f"Noote {str(title)} successfully created"


def find_result(res: str) -> str:
    return f'Notes with: {res} didn''t search'
