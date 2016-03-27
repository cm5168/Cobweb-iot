from setuptools import setup

'''
def readme():
	with open('README.rst') as f:
		return f.read()
'''
# long_description = readme()

setup(name = 'cobwebiot',
		version = '0.1.0',
		description = 'Cobweb Iot platform',
		long_description = 'Integrated raspberryPi platform that include SPI, I2C, and communication between server and client',
		url = 'https://github.com/cm5168/Cobweb-iot',
		author = 'Meng Cao, Cong Zhang, Haiyang Yun, Chang Zhao, Huashan Xiong',
		author_email = 'cm19920214@gmail.com',
		license = 'MIT',
		packages=['cobwebiot'],
		install_requires=['bottle'],
		zip_safe = False)