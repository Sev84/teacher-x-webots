from controller import Supervisor
from akis import Parkur

sim = Supervisor()
step = int(sim.getBasicTimeStep())
keys = sim.getKeyboard()
keys.enable(step)
field = sim.getFromDef("MARKER").getField("translation")
p = Parkur()
def label(i, text, y, color):
    sim.setLabel(i, text, 0.035, y, 0.052, color, 0, "Arial")
label(0, "TEACHER X   /   IKI KULE", 0.035, 0xffffff)
label(1, "H: yuksek sinyal   L: dusuk sinyal   G: geri don", 0.105, 0xd9e8ee)
label(2, "Sanal gaz girdisi | 3B konum gosterimi", 0.172, 0xc5deda)
while sim.step(step) != -1:
    cmd = keys.getKey()
    p.step(step/1000, chr(cmd).upper() if 0 <= cmd < 128 else "")
    field.setSFVec3f([-0.42 + 0.84*p.x, 0.04, 0.44])
    label(3, f"{p.state}   |   Sinyal: {p.gas} birim   |   Konum: %{round(100*p.x)}", 0.87, 0xffcb78)
