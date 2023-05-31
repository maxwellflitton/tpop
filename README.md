# tpop
Install package via pip:
```
pip install git+https://github.com/maxwellflitton/tpop.git     
```

# Usage
You should really use the adapters to interface with the components:

```python
from t_pop.collections.adapters.location_cache import LocationCacheAdapter
from t_pop.collections.adapters.location_guard import TwoDLocationGuardAdapter
```

Cars can be passed around and can interact with adapters:

```python
from t_pop.collections.components.car import Car
```

You can have 

