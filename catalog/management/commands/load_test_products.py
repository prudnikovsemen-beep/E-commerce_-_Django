from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.utils import timezone

class Command(BaseCommand):
    help = "Очищает тестовые продукты и категории, затем добавляет тестовые продукты"

    def handle(self, *args, **options):
        # Удаляем только тестовые данные — помечаем их тегом/префиксом в названии
        # Так не удалим реальные данные, если они появятся позже
        Category.objects.filter(name__startswith='[TEST]').delete()
        Product.objects.filter(name__startswith='[TEST]').delete()

        self.stdout.write("Тестовые категории и продукты удалены.")

        # Создаём тестовые категории
        categories_data = [
            {"name": "[TEST] Электроника", "slug": "test-electronics"},
            {"name": "[TEST] Инструменты", "slug": "test-tools"},
            {"name": "[TEST] Камни и минералы", "slug": "test-stones"},
        ]

        categories = []
        for data in categories_data:
            cat, created = Category.objects.get_or_create(
                name=data["name"],
                defaults={"slug": data["slug"], "description": "Тестовая категория"}
            )
            categories.append(cat)

        self.stdout.write(f"Создано категорий: {len(categories)}")

        # Создаём тестовые продукты
        products_data = [
            {
                "name": "[TEST] Умная розетка",
                "description": "Wi‑Fi розетка с таймером и мониторингом энергопотребления.",
                "price": 1990,
                "category": categories[0],
            },
            {
                "name": "[TEST] Мультиметр цифровой",
                "description": "Профессиональный мультиметр для электрика с подсветкой и автоопределением диапазона.",
                "price": 3490,
                "category": categories[1],
            },
            {
                "name": "[TEST] Набор камней (аметист, кварц)",
                "description": "Коллекционный набор натуральных камней для декора и хобби.",
                "price": 890,
                "category": categories[2],
            },
            {
                "name": "[TEST] Паяльная станция",
                "description": "Паяльная станция с регулировкой температуры и антистатическим комплектом.",
                "price": 5990,
                "category": categories[1],
            },
        ]

        created_count = 0
        for data in products_data:
            product, created = Product.objects.get_or_create(
                name=data["name"],
                defaults={
                    "description": data["description"],
                    "price": data["price"],
                    "category": data["category"],
                    "created_at": timezone.now(),
                    "updated_at": timezone.now(),
                }
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f"Добавлено тестовых продуктов: {created_count}"))
