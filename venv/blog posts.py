
#cronbach alpha #cronbach alpha
import pandas as pd
import pingouin as pg

#used a different example jim links was being blocked
df = pd.DataFrame({'P1': [1, 2, 2, 3, 1, 2, 3, 3, 2, 3, 1],
                   'P2': [1, 1, 1, 2, 1, 3, 2, 3, 3, 3, 1],
                   'P3': [1, 1, 2, 3, 1, 3, 3, 3, 2, 3, 1],
                   'P4': [2, 1, 4, 1, 3, 2, 1, 3, 1, 3, 2]})

a = pg.cronbach_alpha(df)
print(a)


#used a different example jim links was being blocked
df = pd.DataFrame({'P1': [1, 2, 2, 3, 1, 2, 3, 3, 2, 3, 1, 3, 4, 1, 5, 6, 1, 5, 2, 5],
                   'P2': [1, 1, 1, 2, 1, 3, 2, 3, 3, 3, 1, 3, 4, 1, 5, 6, 1, 5, 2, 5],
                   'P3': [1, 1, 2, 3, 1, 3, 3, 3, 2, 3, 1, 3, 4, 1, 5, 6, 1, 5, 2, 5],
                   'P4': [2, 1, 4, 1, 3, 2, 1, 3, 1, 3, 2, 3, 4, 1, 5, 6, 1, 5, 2, 5]})
a = pg.cronbach_alpha(df)
print(a)

