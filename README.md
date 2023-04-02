# hillel_pypro

mak admin

HW-5
django-admin startproject project
python manage.py runserver
python manage.py migrate -> Creates tabs to db
python manage.py createsuperuser
python manage.py startapp #FolderName -> go to settings.py and add to INSTALED_APPS #FolderName
python manage.py migrate --run-syncdb

HW-6
Create model
python manage.py makemigrations -> create model migrate db
python manage.py migrate -> init
python manage.py migrate products 0001/0002/0003 etc (zero for first)

python manage.py shell -> django ORM
EXAMPLE:
    - from products.models import Product
    - Product.objects.all()
    - Product.objects.create(name='Banan', description='banan desc', sku='123', is_active=False)

HW-7
python manage.py makemigrations products --empty -> Create empty migration

EXAMPLE:

def start(apps, schema_editor):
    Product = apps.get_model("products", "Product")
    for _ in range(1000):
       Product.objects.create(name='s', description='r')


def end():
    ....


class Migration(migrations.Migration):

    dependencies = [
    ]

    operation = [
        migration.RunPython(
            start,
            end
        )
    ]

