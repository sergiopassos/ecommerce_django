'''
# Shell session 1
# python manage.py shell
'''

from tags.models import Tag

qs = Tag.objects.all()
print(qs)
black = Tag.objects.last()
black.title
black.slug

black.products
"""
Returns:
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager at 0x6731b70>
"""
black.products.all()

black.products.all().first()

exit()


'''
# Shell session 2
# python manage.py shell
'''
from products.models import Product

qs = Product.objects.all()
print(qs)
tshirt = qs.first()
tshirt.title
tshirt.description

tshirt.tag
'''
AttributeError: 'Product' object has no attribute 'tag'
'''
tshirt.tags
'''
AttributeError: 'Product' object has no attribute 'tags'
'''
tshirt.tag_set
'''
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager at 0x7a27ef0>
'''
tshirt.tag_set.all()
'''
<QuerySet [<Tag: tshirt>, <Tag: Tshirt>, <Tag: t-shirt>]>
'''

tshirt.tag_set.all().filter(title__icontains='black')
