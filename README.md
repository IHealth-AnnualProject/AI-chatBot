# ChatBot using Chatterbot

## SetUp

```
virtualenv -p python3 venv
source venv/bin/activate
pip3 list
pip3 install -r requirements.txt
```

> Using Python 3.5+

## Training

```
python3 train.py
```

### Notes

* You can train this on custom data as well, just pass the folder location in `ChatBot.train(datafolder="./custom", train_corpus=True)` in `train.py`

* Since we are using `trainer='chatterbot.trainers.ChatterBotCorpusTrainer'` check `ChatBot.py`, you need to pass your custom data in the given format. Check `custom/basic.yml` for info

## Running

```
python3 run.py
```

### Notes
* You can turn of logging if you want by commenting `logging.basicConfig(level=logging.INFO)` in `ChatBot.py`

* Threshold is set in `ChatBot.py` at `'threshold': 0.65,`, you can change it.

* In case of response is not found the bot will reply `'default_response': 'I am sorry, but I do not understand.'` set in `ChatBot.py`

* Can create a help response as well in `ChatBot.py`

* The reply is chosen randomly if multiple responsies available: `response_selection_method=get_random_response,` in `ChatBot.py`
