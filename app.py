import pandas as pd
from utils import is_primo
def f(event,context):
    print("Hola vv desde lambda con zappa")
    print(is_primo(6))
    return {}