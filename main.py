

from function import getData
import os
import re
from function import getData

institution = "Гуманитарный колледж"

getData(
    filename = "new data/0841 1842 0861 1862 0971 9851 0852.xls", 
    _course = "Курс 3",
    institution = institution)

# перебор всех скаченных файлов и нахождение встречающихся только один раз
for root, dirs, files in os.walk('new data/'):
    for filename in files:
        x = re.search(r'\(', filename)
        if not x:
            print(filename)
            
