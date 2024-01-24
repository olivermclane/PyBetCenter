import tkinter as tk

from api_interaction import APIClient

# Connection to apiclient via the API_interaction class
api_client = APIClient()

class BettingGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # Dictionary for storing odds
        self.odds_by_event_id = {}
        self.odds_buttons = []
        # Title tkinter window and instantiating the resolution
        self.title("Sports Odd Viewing")
        self.geometry("1060x800")

        # Create main sections
        self.sports_frame = tk.Frame(self)
        self.odds_frame = tk.Frame(self)
        self.events_frame = tk.Frame(self)

        # Initialize elements for each section
        self.sports_list = tk.Listbox(self.sports_frame, width=33, selectmode=tk.SINGLE)
        self.events_list = tk.Listbox(self.events_frame, width=50, selectmode=tk.SINGLE)
        self.odds_list = tk.Listbox(self.odds_frame, width=38, selectmode=tk.SINGLE)

        # Arranging within frames
        self.sports_list.pack(fill="both", expand=True)
        self.events_list.pack(fill="both", expand=True)
        self.odds_list.pack(fill="both", expand=True)

        # Layout the elements
        self.sports_frame.pack(side=tk.LEFT, fill="y")
        self.events_frame.pack(side=tk.LEFT, fill="y")
        self.odds_frame.pack(side=tk.LEFT, fill="y")
        self.display_sports(api_client.get_sports())

    def display_sports(self, sports_data):
        """ This method will display the sports avaliable to bet on"""
        # Populate the sports listbox with items
        for sport in sports_data:
            self.sports_list.insert("end", sport["title"])

    def display_games(self, event_data):
        """This method breaks down the event string to differ games/sports from odds and then seperates them into a
        dicitonary. """
        self.events_list.delete(0, tk.END)  # Clear the listbox
        self.odds_by_event_id = {}   # Clearing dictionary after selecting a different event.

        seen_event_ids = set()  # Track unique event IDs
        for event in event_data:
            event_name = ''
            if event["id"] not in seen_event_ids:  # Check for duplicates events
                seen_event_ids.add(event["id"])
                event_name = f"{event['home_team']} vs {event['away_team']}"
                self.events_list.insert(0, event_name)

            odds_data = []
            for bookmaker in event["bookmakers"]:
                for market in bookmaker["markets"]:
                    for outcome in market["outcomes"]:
                        odds_data.append({
                            "bookmaker": bookmaker["title"],  # Use "title" for bookmaker name
                            "market": market["key"],  # Use "key" for market type
                            "outcome": outcome["name"],  # Use "name" for team name
                            "price": outcome["price"]  # Use "price" for getting odds (in 1: price)
                        })
            self.odds_by_event_id[event_name] = odds_data

    def on_sport_selected(self, event):
        """This method handles sports selection"""
        # Get the index of the selected sport
        selected_index = self.sports_list.curselection()
        if selected_index:  # Check for selection
            self.odds_list.delete(0, tk.END)
            selected_index = selected_index[0]

            # Retrieve the sport title from the listbox
            selected_sport = self.sports_list.get(selected_index)
            sport_data = api_client.get_sports()  # Used to grab key

            # Pulling Event data from each sport
            for sport in sport_data:
                if sport["title"] == selected_sport:
                    event_data = api_client.get_odds(sport["key"])

            # Update the events display
            self.display_games(event_data)

    def on_event_selected(self, event):
        """This method handles event selection"""
        # Get the index of the selected event
        selected_index = self.events_list.curselection()
        if selected_index:  # Check for selection

            # Getting selected element
            selected_index = selected_index[0]
            selected_event_id = self.events_list.get(selected_index)

            self.odds_list.delete(0, tk.END)  # Clear the listbox

            # Getting the odds for the particular event for a particular team
            odds_data = self.odds_by_event_id.get(selected_event_id)

            # Adding list box entries for each element within the odds for that event
            for bookmaker_odds in odds_data:
                odds_text = f"{bookmaker_odds['bookmaker']} - {bookmaker_odds['market']} - {bookmaker_odds['outcome']}: {bookmaker_odds['price']}"
                self.odds_list.insert("end", odds_text)

            for odds_button in self.odds_buttons:
                odds_button.pack()  # Adjusting layout
