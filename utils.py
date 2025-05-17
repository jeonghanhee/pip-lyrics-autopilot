import os

PATH = os.path.dirname(os.path.abspath(__file__));
DEFAULT_FONT = "맑은 고딕"
FONT_SIZE = 13.5

def log(message):
    f = open(PATH + "/logs/debugger.log", "w")
    f.writelines('{}\n'.format(message))
    f.close()