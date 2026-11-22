import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'controllers'/'parkur'))
from akis import Parkur
p=Parkur()
p.gas=600
p.step(.032,'G')
assert (p.state,p.x)==('HAZIR',0)
p.step(.032,'H')
p.step(.032,'G')
assert p.state=='ILERI'
for i in range(70): p.step(.032)
assert (p.state,p.x)==('UCTA',1)
for i in range(70): p.step(.032)
assert (p.state,p.x)==('UCTA',1)
p.step(.032,'G')
for i in range(100): p.step(.032)
assert (p.state,p.x)==('BEKLE',0)
p.step(.032,'L')
assert p.state=='HAZIR'
p.step(.032,'H')
assert p.state=='ILERI'
print('OK: esik, erken komut, iki uc, bekleme, donus ve yeniden kurma')
