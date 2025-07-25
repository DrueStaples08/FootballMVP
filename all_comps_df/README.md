# 📊 AllCompetitions – FotMob League Tracker

A utility class for extracting, managing, and tracking football competitions from [FotMob](https://www.fotmob.com). This tool allows you to retrieve competition IDs, format competition names, and maintain a local watchlist of leagues to monitor.

---

## 🧠 Overview

The `AllCompetitions` class performs three core tasks:

1. **Scrapes competition IDs** from FotMob.
2. **Formats league names** into clean, hyphenated strings.
3. **Adds competitions** to a local watchlist using Spark DataFrames.

---

## 📦 Requirements

- Python 3.12+
- `pyspark`
- `beautifulsoup4`
- `requests`

Install via pip:

```bash
pip install -r requirements.txt
🔧 Class Overview
python
Copy
Edit
from mvp_comp_dir.all_competitions import AllCompetitions

comp = AllCompetitions()
🧾 Methods
gather_all_competition_ids(url: str) -> Dict
Scrapes competition IDs from FotMob’s leagues page and returns a dictionary of ID → formatted name.

python
Copy
Edit
all_ids = comp.gather_all_competition_ids("https://www.fotmob.com/")
format_competition_names(tournament_prefixes_dict: Dict) -> Dict
Cleans up competition names (e.g. "Serie A" → "serie-a").

python
Copy
Edit
formatted = comp.format_competition_names({"55": "Serie A"})
add_competition_to_my_watchlist(competition_name: str, gather_all_competition_ids: Dict, defined_url: str = "") -> str
Adds a league to the local Spark-based all_comps_df watchlist, either by:

Lookup via formatted name

OR by parsing the full FotMob URL

python
Copy
Edit
# By name (preferred)
comp.add_competition_to_my_watchlist("mls", all_ids)

# Or directly by URL (if missing from the dictionary)
comp.add_competition_to_my_watchlist("", {}, defined_url="https://www.fotmob.com/leagues/55/matches/serie-a")
📁 Output
Competitions are saved in a local CSV folder (all_comps_df) with the following schema:

competition_url	competition_id	competition_name
https://...	55	serie-a

Duplicates are automatically checked and skipped.

🚨 Error Handling
If the competition name doesn't exist in the dictionary and no defined_url is provided, an error message will guide the user on how to correctly call the method.

🛠 Example
python
Copy
Edit
comp = AllCompetitions()
all_comp_info = comp.gather_all_competition_ids("https://www.fotmob.com/")
comp.add_competition_to_my_watchlist("fifa-intercontinental-cup", all_comp_info)
Or:

python
Copy
Edit
comp.add_competition_to_my_watchlist(
    competition_name="",
    gather_all_competition_ids={},
    defined_url="https://www.fotmob.com/leagues/47/matches/premier-league"
)