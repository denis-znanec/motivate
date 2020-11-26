import motivate.motivate.motivate as mt
import motivate.motivate.find_dupes as fd
import pytest



def test_getlink():
    assert mt.getlink(__file__) == "C:\\Users\denis\Documents\GitHub\motivate"

def test_motivate(capsys):
    mt.quote("test")
    out, err = capsys.readouterr()
    assert out == "\"test\"\n" "\t\t--testington\n"

def test_motivate2(capsys):
    mt.quote("test3")
    out, err = capsys.readouterr()
    assert out == '---------------Debug info begins:--------------\n' 'Oops, we met a ValueError.\n' 'Please check this file ' 'C:\\Users\\denis\\Documents\\GitHub\\motivate\\motivate\\test3\\001.json\n' '1. A Possible reason is that there is a redundant comma behind last group of ' 'author/quote in this json file.\n' '   If so, delete that redundant comma, then it will run smoothly.\n' '2. Another possible reason is that there is hard line-break or tab in that ' 'file.\n' "   However JSON don't support that. Please use '\\n' or '\\t'.\n" 'For later actions, I help you wrote this filename to JSON_ERROR_LIST.txt.\n' 'I suggest you to test those json file in this website: jsonlint.com\n' '---------------Debug info ends:--------------\n'

def test_find_dupes(capsys):
    fd.findDupes("test")
    out, err = capsys.readouterr()
    assert out == "Unique quotes: 1, authors: 1\n\n"

def test_find_dupes2(capsys):
    fd.findDupes("test2")
    out, err = capsys.readouterr()
    assert out == "Unique quotes: 1, authors: 1\n""{'quote': 'test', 'author': 'testington'}\n"