from lib.report_length import *

def test_report_length1():
    result = report_length("ians_report.txt")
    assert result == "This string was 15 characters long."

def test_report_length2():
    result = report_length("Top_Secret.rtf")
    assert result == "This string was 14 characters long."

def test_report_length3():
    result = report_length("My_report.csv")
    assert result == "This string was 13 characters long."


def test_report_length4():
    result = report_length("hello world")
    assert result == "This string was 11 characters long."


