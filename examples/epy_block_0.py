"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, name = "triger"):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Eval_number_sample',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.m_name = name
        self.count = 0

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        self.count += len(input_items[0])
        print("%s len input samples = %s - count %s\n" % (self.m_name, len(input_items[0]), self.count))
        self.consume(0,len(input_items[0])) 
        return 0
