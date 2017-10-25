# cryptopy

##### To run you need first to install in your environment:
```python
pip install requests
pip install beautifulsoup4
``` 
##### Make files executable:
```python
sudo chmod +x rig_temps.py
sudo chmod +x what_to_mine.py
``` 


#### Rig Temps
Shows the temprature for rigs under panels. Info provided by ethOS API
Panels needed. See PANELS variable in config.py

```python
./rig_temps.py 
```

#### What to mine
Shows the profits for different coins. Info provided by Coinwarz
URL needed in order to scrape data. See URL in config.py

```python
./what_to_mine.py 
```



