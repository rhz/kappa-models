from sys import argv, exit
from math import sqrt
from matplotlib import rcParams
rcParams.update( {'backend': 'Agg', 'axes.labelsize': 22} )
import pylab

filename = argv[1]
time, qties, coln2name = [], [], []
with open(filename, 'r') as infile:
  fileContents = infile.read().split('\n')
  header = fileContents.pop(0).split()
  for coln, name in enumerate(header[1:]):
    qties.append([])
    coln2name.append(name)
  numCols = len(qties)+1
  for lineNum, row in enumerate(fileContents):
    row = row.split()
    if len(row) == numCols:
      time.append( float(row[0]) )
      for coln, val in enumerate(row[1:]):
        qties[coln].append( float(val) )
    else:
      print 'Incomplete line:', lineNum

golden_mean = (sqrt(5) - 1.0) / 2.0

fig = pylab.figure( figsize=(10.0, golden_mean * 10.0) )
for coln, name in enumerate(coln2name):
  pylab.plot( time, qties[coln], label=name )
pylab.xlabel('Time')
pylab.ylabel('Number of molecules')
pylab.legend()
fig.savefig( filename[:-4] + '.png' )
