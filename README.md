This basic tkinter application is a viewing application for all the odds in sports betting. 
This spans across several different sports books, so you can view odds for any game.

# Step 1
For this to work you do need to get a API-key.

Navigate to https://the-odds-api.com

Once there, scroll down and register for a free API KEY.

# Step 2
After registration is complete, the API KEY will be sent to your email. Copy that key into a .env file with the env variable called API-KEY.

Create a .env file and follow the below format.
```{python}
API_KEY="{your_api_key}"
```

# Run
Once this is complete, run main.py and enjoy the UI to explore different head-to-head odds and outright odds.

To do this navigate to the root directory.
```
python main.py
```

# Notes
It is worth noting, the games that have head-to-head odds will populate with None Vs None, click on that and you can still retrieve odds for outright.
