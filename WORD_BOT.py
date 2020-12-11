import PySimpleGUI as sg
from nltk.corpus import wordnet as wn

greeting = "Hi. I am word bot. I can help you with words.\n\n"

layout = [
    [sg.Multiline(greeting, font=("Arial", 14), size=(70, 15), key='output')],
    [sg.InputText("", font=("Arial", 14), size=(50, 1), key='input', enable_events=True)],
    [sg.Button("Meaning", font=("Arial", 14), bind_return_key=True, key="meaning"),
     sg.Button("Synonyms", font=("Arial", 14), key='synonyms'),
     sg.Button("Antonyms", font=("Arial", 14), key='antonyms'),
     sg.Button("Clear", font=("Arial", 14), key='clear')
    ]
]

def get_meaning(word):
    synset = wn.synsets(word)
    print(synset)
    if synset:
        return synset[0].definition()
    else:
        return None

def get_synonyms(word):
    synonyms = []
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            if lemma:
                synonyms.append(lemma.name())
    return set(synonyms)

def get_antonyms(word):
    antonyms = []
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return set(antonyms)

def display_meaning(word):
    meaning = get_meaning(word)
    window['output'].print("WORD : " + word)
    if meaning:
        window['output'].print("MEANING : ", meaning)
    else:
        display_error("Word is not found in corpus")

def display_synonyms(word):
    synonyms = get_synonyms(word)
    window['output'].print("WORD : " + word)
    if synonyms:
        window['output'].print("SYNONYMS : ", synonyms)
    else:
        display_error("Word is not found")

def display_antonyms(word):
    antonyms = get_antonyms(word)
    window['output'].print("WORD : " + word)
    if antonyms:
        window['output'].print("ANTONYMS : ", antonyms)
    else:
        display_error("Unable to find antonym of "+word)

def display_error(message):
    window['output'].print("Error : " +message, text_color='red')

if __name__ == '__main__':
    window = sg.Window('File Explorer', layout)

    while True:
        event, values = window.Read()
        if event == 'meaning':
            display_meaning(values['input'])
        elif event == 'synonyms':
            display_synonyms(values['input'])
        elif event == 'antonyms':
            display_antonyms(values['input'])
        elif event == 'clear':
            window.FindElement('output').Update(greeting)
        elif event == sg.WINDOW_CLOSED:
            break
    window.Close()
