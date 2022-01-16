import pandas as pd
import numpy as np
import requests

base = "https://www.balldontlie.io/api/v1"
#Test, joel embiid 2020 season. 
embiid = requests.request("GET", "https://www.balldontlie.io/api/v1/stats?seasons=2020&player_ids=29").json()
df = embiid