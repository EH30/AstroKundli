# AstroKundli
AstroKundli uses flatlib_sidereal.   
flatlib was made by João Ventura and sidereal was added by joaoventura.    

AstroKundli Generates Lagna Chart.    

# Example   
<h3>Lagna Chart</h3>   

```
from AstroKundli import GKundli

# Largna Chart 
Lagna_Chart = GKundli.GKundli(2007, 6, 28, 0, 0,"2:00", 25.7479,  28.2293).lagnaChart()
print(Lagna_Chart)
# Output: 
# {
# '1': {'sign_num': 12, 'asc': '+11:21:18>', 'planets': {}}, 
# '2': {'sign_num': 1, 'planets': {'Ma': '+08:13:20'}}, 
# '3': {'sign_num': 2, 'planets': {}}, 
# '4': {'sign_num': 3, 'planets': {'Su': '+11:54:51', 'Me': '+13:14:45'}}, 
# '5': {'sign_num': 4, 'planets': {'Sa': '+28:02:18', 'Ve': '+25:42:01'}}, 
# '6': {'sign_num': 5, 'planets': {'Ke': '+16:17:07'}}, 
# '7': {'sign_num': 6, 'planets': {}}, 
# '8': {'sign_num': 7, 'planets': {}}, 
# '9': {'sign_num': 8, 'planets': {'Mo': '+10:56:37', 'Ju': '+18:17:44'}}, 
# '10': {'sign_num': 9, 'planets': {'Pl': '+03:27:17'}}, 
# '11': {'sign_num': 10, 'planets': {'Ne': '+27:46:35'}}, 
# '12': {'sign_num': 11, 'planets': {'Ra': '+16:17:07', 'Ur': '+24:43:19'}}
# }
# -------------------------------------------------------------------------
# 1 = First House
# 2 = Second House
# 3 = Third House
# ...
```   

<h3>Transit Chart</h3>   

```
from AstroKundli import GKundli

# Transit Chart 
Lagna_Chart = GKundli.GKundli(2007, 6, 28, 0, 0,"2:00", 25.7479,  28.2293).lagnaChart()
Transit_Chart = GKundli.GKundli(2007, 6, 28, 0, 0,"2:00", 25.7479,  28.2293).transitChart(Lagna_Chart)
print(Transit_Chart)

# Output: 
# {'1': {'sign_num': 12, 'asc': '+25:34:23>', 'planets': {'Ne': '+02:43:02'}}, 
# '2': {'sign_num': 1, 'asc': None, 'planets': {'Ju': '+21:16:05', 'Ra': '+03:25:39', 'Ur': '+28:53:15'}}, 
# '3': {'sign_num': 2, 'asc': None, 'planets': {}}, 
# '4': {'sign_num': 3, 'asc': None, 'planets': {}}, 
# '5': {'sign_num': 4, 'asc': None, 'planets': {'Ve': '+19:23:12'}}, 
# '6': {'sign_num': 5, 'asc': None, 'planets': {'Su': '+09:05:54', 'Me': '+27:14:48'}}, 
# '7': {'sign_num': 6, 'asc': None, 'planets': {'Ma': '+05:19:09'}}, 
# '8': {'sign_num': 7, 'asc': None, 'planets': {'Ke': '+03:25:39'}}, 
# '9': {'sign_num': 8, 'asc': None, 'planets': {}}, 
# '10': {'sign_num': 9, 'asc': None, 'planets': {'Mo': '+09:09:58'}}, 
# '11': {'sign_num': 10, 'asc': None, 'planets': {'Pl': '+04:09:25'}}, 
# '12': {'sign_num': 11, 'asc': None, 'planets': {'Sa': '+09:41:33'}}}
```



## Installation
download AstroKundli      
run powershell as an Administrator and cd to the AstroKundli folder.   
``` 
pip install .
```   



