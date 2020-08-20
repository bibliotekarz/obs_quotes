# obs_quotes 

## po polsku 

Skrypt pobiera losowo jedną linię tekstu ze wskazanego pliku tekstowego i wyświetla ją w widgecie tekstowym OBS. 
Linia jest losowana zgodnie z ustawioną częstotliwością w zakresie od 1 sekundy do 3600 sekund.

Skrypt powstał na bazie domyślnego skryptu dostępnego w OBS [url-text.py](https://github.com/obsproject/obs-studio/blob/master/UI/frontend-plugins/frontend-tools/data/scripts/url-text.py)

## Uruchomienie

1. W OBS wchodzimy w panel źródła obrazu i dodajemy do niego obiekt Text (GDI+). 
2. Z menu "Narzędzia" wybieramy "skrypty". Jak pojawi się okienko naciskamy w nim plus i wskazujemy lokalizację pobranego skryptu, następnie klikamy go i naciskamy guzik otwórz. Pojawi nam się w oknie obsługującym skrypty jego nazwa (obs_quotes.py). 
3. Klikamy w nazwę obs_quotes.py i wypełniamy formularz:
     - w pierwszej linii podajemy pełną ścieżkę do pliku tekstowego
     - w drugiej linii ustawiamy czas wyświetlania napisu
     - w trzeciej linii z menu rozwijalnego wybieramy nazwę którą nadaliśmy obiektowi Text (GDI+) mającemu wyświetlać napisy
     - klikamy guzik Refresh i :clap:.

## in English

The script takes one line of text randomly from the indicated text file and displays it in the OBS text widget. 
The line is randomized according to the set frequency ranging from 1 second to 3600 seconds.

The script is based on the default script available in OBS [url-text.py](https://github.com/obsproject/obs-studio/blob/master/UI/frontend-plugins/frontend-tools/data/scripts/url-text.py)

## Commissioning

1. In OBS, we enter the image source panel and add a Text (GDI +) object to it.
2. Select "scripts" from the "Tools" menu. When the window appears, press plus in it and select the location of the downloaded script, then click it and press the open button. His name (obs_quotes.py) will appear in the script window.
3. Click on the name obs_quotes.py and fill in the form:
     - in the first line we give the full path to the text file
     - in the second line we set the time of displaying the text
     - in the third line, from the pull-down menu, we select the name that we gave the Text (GDI +) object that was to display the strings
     - we click Refresh and :clap:.
