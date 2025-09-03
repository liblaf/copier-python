# >>> tangerine-start: lazy-loader.py >>>
import lazy_loader as lazy

__getattr__, __dir__, __all__ = lazy.attach_stub(__name__, __file__)
# <<< tangerine-end <<<
