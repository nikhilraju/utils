# Randomly sample a few objects from a database
import random
max_id = SomeObjectModelHere.objects.order_by('-id')[0].id
sample_size = 50
random_ids = random.sample(list(range(max_id + 1)), sample_size)
