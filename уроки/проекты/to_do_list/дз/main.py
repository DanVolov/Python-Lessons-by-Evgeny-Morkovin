from functions.frontend import *
from functions.backend import *


w = setup()
frame, task_entry, category_var, priority_entry, date_entry, time_entry = create_task_fame(w)
frame_button, button_add, button_change = create_buttons(w)
button_add.configure(command=lambda: click(w, task_entry, category_var, priority_entry, date_entry, time_entry))


w.mainloop()