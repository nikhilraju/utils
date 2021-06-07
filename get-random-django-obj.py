from django.db.models import Max
import random


# To get one object at a time
def get_random_obj():
    max_id = MyModelName.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        my_model_name = MyModelName.objects.filter(pk=pk).first()
        if my_model_name:
            return my_model_name
foo = get_random_obj()


## To extract a sample of size k from the entire population
max_id = MyModel.objects.all().aggregate(max_id=Max("id"))['max_id']
all_ids = list(range(1,max_id+1))
random_pks = random.sample( all_ids,  sample_size )
res = MyModel.objects.all().filter(pk__in=random_pks)



