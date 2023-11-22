# import random
# from faker import Faker
# from myapp.models import Product, Category
#
# fake = Faker()
#
# def generate_dummy_data():
#     categories = Category.objects.all()
#
#     for _ in range(50):
#         category = random.choice(categories)
#         name = fake.word()
#         vendor = fake.name()
#         quantity = random.randint(1, 100)
#         original_price = round(random.uniform(1.0, 100.0), 2)
#         selling_price = round(random.uniform(1.0, 100.0), 2)
#         description = fake.sentence()
#         status = fake.boolean()
#         trending = fake.boolean()
#
#         product = Product.objects.create(
#             category=category,
#             name=name,
#             vendor=vendor,
#             quantity=quantity,
#             original_price=original_price,
#             selling_price=selling_price,
#             description=description,
#             status=status,
#             trending=trending
#         )
#         print(f"Created product: {product}")
#
# generate_dummy_data()
