from min_heap import MinHeap
import asyncio, concurrent
import msvcrt
import math
import time
class Building:
	def __init__(self, name=None, level=1):
		self.name = name
		self.level = level

	def output(self): 
		return 2**self.level

	def upgrade_time(self): #seconds
		return 2**self.level

class Game:
	def __init__(self):
		self.running = True
		self.tasks = []
		self.timers = MinHeap()
		self.farm = Building()
		self.message_queue = asyncio.Queue()

	async def handle_command(self, command):
		await self.message_queue.put('>>>'+command)
		if command == 'quit':
			self.running = False
		if command == 'upgrade':
			timer = time.time()+self.farm.upgrade_time()
			if not self.timers.find_min():
				self.timers.put(timer)
				await self.message_queue.put('Farm upgrade started!')
			else:
				await self.message_queue.put('Farm upgrade in progress!')

		return True

	async def timer_poll(self):
		while self.running:
			mintimer = self.timers.find_min()
			if mintimer:
				if time.time() - mintimer >= 0 :
					self.timers.del_min()
					self.farm.level += 1
					await self.message_queue.put('Farm upgrade complete!')
			await asyncio.sleep(1)

	async def status_report(self):
		while self.running:
			out = 'Your farm is level {} and outputs {} resources. It would take {} seconds to upgrade it.'.format(self.farm.level, self.farm.output(), self.farm.upgrade_time()) 
			mintimer = self.timers.find_min()
			if mintimer:
				out+='\nThere is an upgrade in progress, it will be done in {}'.format(time.time()-mintimer)
			await self.message_queue.put(out)
			await asyncio.sleep(3)

	async def handle_reading(self):
	    while self.running:
	        message = await self.message_queue.get()
	        print(message)

	async def handle_sending(self):
	    loop = asyncio.get_event_loop()

	    executor = concurrent.futures.ThreadPoolExecutor(
	        max_workers=1,
	    )

	    while self.running:
	        msg = await loop.run_in_executor(executor, input)
	        await self.handle_command(msg)


async def run_game():
    global game
    game = Game()
    asyncio.ensure_future(game.handle_reading())
    asyncio.ensure_future(game.handle_sending())
    asyncio.ensure_future(game.status_report())
    asyncio.ensure_future(game.timer_poll())

    while game.running:
    	await asyncio.sleep(0)

async def cleanup():
	print('Thanks for playing duh')

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(run_game())
finally:
    loop.run_until_complete(cleanup())
loop.close()
