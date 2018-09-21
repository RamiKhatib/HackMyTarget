import os

class Ctrl:
	def __init__(self,args):
		self.user=os.popen("whoami").read()[:-1]
		self.args=args

	def start(self):
		argLen=len(self.args)
		if argLen==1:
			self.usage()
		else:
			self.args.pop(0)
		self.checkArgs()

	def checkArgs(self):
		pass			# TODO

	def usage(self):
		print("Usage:")		# TODO
