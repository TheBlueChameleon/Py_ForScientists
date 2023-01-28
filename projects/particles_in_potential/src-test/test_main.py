import unittest

from test_Particle import Particle_Test
from test_Potential import Potential_Test
# ... and all other classes/modules

if __name__ == '__main__':
    print('ABOUT TO RUN UNIT TESTS')
    print('#' * 80)

    unittest.main()

    print('#' * 80)
    print('DONE')

else:
    print('INITIALIZED UNIT TEST RUN EXTERNALLY. READY TO GO')