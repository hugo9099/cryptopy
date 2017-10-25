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
sudo chmod +x workers_perf.py
``` 


### Rig Temps
Shows the temprature for rigs under panels. Info provided by ethOS API
Panels needed. See PANELS variable in config.py

```python
./rig_temps.py 
```

### What to mine
Shows the profits for different coins. Info provided by Coinwarz
URL needed in order to scrape data. See URL in config.py

```python
./what_to_mine.py 
```

### Workers Performance
Shows the general and per-worker performance based on the stats given
by Ethermine API (mining pool). See ETH_WALLET in config.py.

The purpose of this script is to give information whether a rig (worker) is currently 
sending the amount of shares is supposed to send to the network.
As shown in the ethermine graphs, some rigs perform better than others. This could be
due to multiple factors such as overclocking, free space, RAM, etc.   


```python
./workers_perf.py
```

