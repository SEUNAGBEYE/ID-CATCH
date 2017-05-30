import random
def gen_E_Id():

		e_id = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
		return e_id