import pdfplumber
import pandas as pd
from IPython.display import display

# open pdf
pdf = pdfplumber.open("./ca-warn-report.pdf")
# choose pages
p0 = pdf.pages[0]
#extrac table
table = p0.extract_table()
#make it a dataframe
df = pd.DataFrame(table[1:],columns=table[0])
# delete extra space
for column in ["Effective", "Received"]:
  df[column] = df[column].str.replace(" ","")
display(df)
# filter 
data = df[df['Notice Date'] == "07/17/2015"]
display(data)

