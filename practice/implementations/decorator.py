"""
simple decorator
"""
import time 

#a decorator that measures execution time
def costly(x):
	time.sleep(x)
	print('Slept for {}'.format(x))

def measure_time(f):
	def wrapper(x):
		timer = time.time()
		f(x)
		timer = time.time() - timer
		print('Executed in {}'.format(timer))
	return wrapper

costly(1)

wrapped = measure_time(costly)
wrapped(1)

"""
python syntax
"""

#decorator syntax
@measure_time
def costly(x):
	time.sleep(x)
	print('Slept for {}'.format(x))

costly(1)