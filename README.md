This basic tkinter application is a viewing application for all of the odds in sports betting. 
This spans across several 


For this to work you do need to get a API-key.

Navigate to https://the-odds-api.com

Once there, scroll down and register for a free API KEY.

After registration is complete, the API KEY will be sent to your email. Copy that key into a .env file with the env variable called API-KEY.

```{python}
API_KEY="{your_api_key}"
```
Once this is complete, run main.py and enjoy the a UI to explore different head-to-head odds and outright odds.


It is worth noting, the games that have head to head odds will populate with None Vs None, click on that and you can still retrieve odds for outright.
