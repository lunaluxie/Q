# Q
> A quantum computing simulation library written in Python

With Q you can simulate quantum computing systems on a classical computer. 

## Usage
Basic example creating a qubit and applying a not-gate:
```Python
from Q import Qubit, gates

qb = Qubit(alpha=1, beta=0)

not_gate = gates.not_gate()

qb.apply_gate(not_gate)


print (qb.measure_state())
# out: 1
```
Because the initial state had the alpha coefficient equal to one 1, the measure state will with 100% certainty return 1 since now the beta coefficient is equal to 1.

Measure state simulates a physical measurement. It returns 0 with alpha squared probability, and 1 with beta squared probability.
```Python
from Q import Qubit

qb = Qubit(1,0)

print (qb.measure_state())
# out: 0
```

Alternatively, you can access the internal state directly. This is useful for debugging, however, would not be possible on a physical quantum computer. 
```Python
from Q import Qubit

qb = Qubit(1,0)

print (qb.get_state())
# out: (1,0)
```

You can also manually set the state of a qubit using the `set_state` method. This is useful for debugging, but is not possible on a physical quantum computer. 
```Python
from Q import Qubit

qb = Qubit()

qb.set_state(1,0)

# you can also let Q figure out the other coefficient
qb.set_state(beta=0.3)
```


## Todo: 
- Multi-qubit simulation. 
- Entanglement
- More gates
