from django.db.models import Max
import random
def get_random_obj():
    max_id = MyModelName.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        my_model_name = MyModelName.objects.filter(pk=pk).first()
        if my_model_name:
            return my_model_name
foo = get_random_obj()


