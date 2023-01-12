

# from function import getData

institution = "Гуманитарный колледж"


import os
import re
from function import getData

# for root, dirs, files in os.walk('new data/'):
#     for filename in files:
#         x = re.search(r'\(', filename)
#         if not x:
#             print(filename)


getData(
    filename = "new data/0841 1842 0861 1862 0971 9851 0852.xls", 
    _course = "Курс 3",
    institution = institution)




# 0811 1812 0821 1822 2822 2812.xls
# 0841 1842 0861 1862 0971 9851 0852.xls
# 1811 1851 2852 1821.xls
# 1841 1852 1861 2863 1971.xls
# 2811 2821 2841 2851 2861 2862 2971.xls
# 9841 9861 0862.xls