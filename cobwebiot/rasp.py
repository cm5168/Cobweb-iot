import spidev
from cobwebiot import dev

class SPI:
    def __init__(self):
        self.spi = spidev.SpiDev()

    def add_dev(self,port,dev_id,dev_name):
        self.spi.open(port,dev_id)
        self.dev = dev_name

    def read_channel(self,channel):
        adc = self.spi.xfer2(self.dev.get_xfer2(channel))
        return self.dev.hex_to_data(adc[1],adc[2])
