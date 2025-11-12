import re

def reverse_str(s: str) -> str:
    return s[::-1]

def to_upper(s: str) -> str:
    return s.upper()

def remove_vowels(s: str) -> str:
     return (re.sub("[aeiouAEIOU]","",s)) 

def remove_every_third(s: str) -> tuple[str, list[str]]:
    s_str = ""
    s_list = list(s) 
    del s_list[::3]      
    s_str.join(s_list)  
    return s_str, s_list      

def letter_counts_map(s: str) -> dict[str, int]:
    l= len(s)
    return {s: l}





