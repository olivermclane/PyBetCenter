import api_interaction
import gui

# Initialize API client
api_client = api_interaction.APIClient()

# Initialize GUI
betting_gui = gui.BettingGUI()

# Fetch initial sports data and populate the GUI
betting_gui.sports_list.bind("<<ListboxSelect>>", betting_gui.on_sport_selected)
betting_gui.events_list.bind("<<ListboxSelect>>", betting_gui.on_event_selected)

betting_gui.mainloop()
