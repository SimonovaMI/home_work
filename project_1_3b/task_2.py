import names
import numpy as np
import re

count_names = 100

firstnames = np.array([''.join(names.get_first_name()) for i in range(count_names)])
firstnames_begin_A_M = [i for i in firstnames if re.match(r'[A-M]', i)]
firstnames_begin_N_Z = [i for i in firstnames if re.match(r'[N-Z]', i)]

print(firstnames_begin_A_M)
print(firstnames_begin_N_Z)