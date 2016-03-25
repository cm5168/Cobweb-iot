from setuptools import setup

setup(name = 'cobwebiot',
		version = '0.1.0',
		description = 'Cobweb Iot platform',
		url = 'https://github.com/cm5168/Cobweb-iot',
		author = 'Meng Cao, Cong Zhang, Haiyang Yun, Chang Zhao, Huashan Xiong',
		author_email = 'cm19920214@gmail.com',
		license = 'MIT',
		packages=['cobwebiot'],
		install_requires=['bottle'],
		zip_safe = False)