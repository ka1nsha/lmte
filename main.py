# -*-coding:utf-8 -*-
import json
import sqlite3
from random import randint
import mtranslate
from datetime import datetime
import notify2


class bcolors:
    """
    Color Hex Codes for Terminal
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class JsonParser():

    def __init__(self):
        self.FILESPECS = {
            "filename": "quotes.json",
            "filemode": "rb"
        }
        self.File = json.loads(open(self.FILESPECS['filename'],
                                    self.FILESPECS['filemode']).read())

    def __repr__(self):
        """
        JSON Parser for Quotes file in Local

        Returns:
        [str] -- [Return Filename and Filemode]
        """
        FileName = self.FILESPECS['filename']
        FileMode = self.FILESPECS['filemode']
        return f"File name:{FileName}, File mode:{FileMode}"

    def getquotes(self, index: int):
        """
        Returned random quotes in Local JSON Quotes File

        Arguments:
            index {int} -- index of quotes

        Returns:
            [string] -- [Returning one quote in quotes used index number]
        """
        Quotes = self.File[index]
        Quote_Text = Quotes['quoteText']
        Quote_Author = Quotes['quoteAuthor']
        Repr_String = f"{Quote_Text} \n - {bcolors.BOLD} {Quote_Author} {bcolors.ENDC}"
        return Repr_String

    def quoteslength(self):
        """
        Returning length to json file.

        Returns:
            [int] -- [length of json file.]
        """
        return len(self.File)

    def getwordsinquotes(self, index: int):
        """Getting all words in quotes with serialized

        Arguments:
            index {int} -- index of Quotes

        Returns:
            [str] -- word
        """
        index -= 1
        Sentence = self.File[index]['quoteText'].split()
        Sentence_Length = len(Sentence)-1
        Word_Select = randint(0, Sentence_Length)
        Word = Sentence[Word_Select]
        return Word

    def translateword(self, word: str):
        """[Translate given word used Google Translate. Default used en-tr]

        Arguments:
            word {str} -- [English word]

        Returns:
            [str] -- [Turkish word]
        """
        Word = mtranslate.translate(word, "tr", "auto")
        return Word

        @property
        def onlyword(self):
            return Word

    def wordrender4human(self, EngWord: str, TrWord: str):

        #   return f"{bcolors.WARNING}{EngWord}{bcolors.ENDC} word is mean in Turkish {bcolors.OKGREEN}{TrWord}{bcolors.ENDC}"
        return f"{EngWord} word is mean in Turkish {TrWord}"


class DatabaseProcess():

    def __init__(self):
        """
        Setting up Database variables, Connector and Cursor
        """
        self.DbName = ".words.db"
        self.Con = sqlite3.connect(self.DbName)
        self.Cur = self.Con.cursor()

    def dbinitialize(self):
        """Create table if i don't have
        """
        TableQuery = "CREATE TABLE IF NOT EXISTS learnedwords(id integer PRIMARY KEY,eng_word text unique,tr_word text,learndate text)"
        self.Cur.execute(TableQuery)
        self.Con.commit()

    def appendword(self, EngWord: str, TrWord: str):
        """[Translate function.]

        Arguments:
            EngWord {str} -- [Word in English]
            TrWord {str} -- [Translated word from English - Turkish]
        """
        LearnDate = datetime.now()
        LearnDate = f"{LearnDate.day}.{LearnDate.month}.{LearnDate.year}"
        self.Cur.execute(
            "INSERT INTO learnedwords(eng_word,tr_word,learndate) VALUES(?,?,?)", (EngWord, TrWord, LearnDate),)
        self.Con.commit()

    def duplicatecontrol(self, EngWord: str):
        """[Function running each word for duplicates. ]

        Arguments:
            EngWord {str} -- [Word in English]

        Returns:
            [str] -- [Return None or Query Result]
        """
        self.Cur.execute(
            'SELECT eng_word FROM learnedwords WHERE eng_word=?', (EngWord,))
        result = self.Cur.fetchone()
        return result


def shownotify(Text: str):
    """[This function using of notifications on Desktop Environment]

    Arguments:
        Text {str} -- [Translated word with orginal word]
    """
    notify2.init('New Word')
    NotifyBody = f"You have new word \n {Text}"
    n = notify2.Notification("Let me teach English",
                             NotifyBody,
                             "notification-message-im"
                             )
    n.show()


db = DatabaseProcess()
db.dbinitialize()

js = JsonParser()
max_length = js.quoteslength()


rand = randint(0, max_length)
word = js.getwordsinquotes(rand)
translated_text = js.translateword(word)
if db.duplicatecontrol(word) == None:
    db.appendword(word, translated_text)

renderedtext = js.wordrender4human(word, translated_text)
shownotify(renderedtext)
