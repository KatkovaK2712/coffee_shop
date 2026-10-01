from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CatTeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя котика")
    position = models.CharField(max_length=100, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='cat_team/', verbose_name="Фото котика")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Член команды котиков"
        verbose_name_plural = "Команда котиков"
        ordering = ['order']

    def __str__(self):
        return self.name


class MenuPageContent(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок меню", default="Наше меню")
    subtitle = models.TextField(verbose_name="Подзаголовок меню", default="Выберите свой любимый напиток")
    main_image = models.ImageField(upload_to='menu_page/', verbose_name="Главное фото меню", blank=True, null=True)

    class Meta:
        verbose_name = "Контент страницы меню"
        verbose_name_plural = "Контент страницы меню"

    def __str__(self):
        return "Контент страницы меню"


class HomePageContent(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок", default="Кофейня Уютный Котик")
    subtitle = models.TextField(verbose_name="Подзаголовок", default="Где кофе встречается с мурлыканием")
    main_image = models.ImageField(upload_to='homepage/', verbose_name="Главное изображение", blank=True, null=True)
    philosophy_title = models.CharField(max_length=200, verbose_name="Заголовок философии", default="Наша философия")
    philosophy_text = models.TextField(verbose_name="Текст философии", default="Мы создали место, где можно насладиться кофе в компании котиков")
    philosophy_image = models.ImageField(upload_to='homepage/', verbose_name="Изображение философии", blank=True, null=True)

    class Meta:
        verbose_name = "Контент главной страницы"
        verbose_name_plural = "Контент главной страницы"

    def __str__(self):
        return "Контент главной страницы"


class AboutPageContent(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок", default="О нашей кофейне")
    history_title = models.CharField(max_length=200, verbose_name="Заголовок истории", default="Наша история")
    history_text = models.TextField(verbose_name="Текст истории", default="История нашей кофейни...")
    mission_title = models.CharField(max_length=200, verbose_name="Заголовок миссии", default="Наша миссия")
    mission_text = models.TextField(verbose_name="Текст миссии", default="Наша миссия...")
    main_image = models.ImageField(upload_to='about/', verbose_name="Основное изображение", blank=True, null=True)

    class Meta:
        verbose_name = "Контент страницы 'О нас'"
        verbose_name_plural = "Контент страницы 'О нас'"

    def __str__(self):
        return "Контент страницы 'О нас'"


class ContactsPageContent(models.Model):
    address = models.TextField(verbose_name="Адрес", default="г. Москва, ул. Котикова, 15")
    phone = models.CharField(max_length=20, verbose_name="Телефон", default="+7 (999) 123-45-67")
    email = models.EmailField(verbose_name="Email", default="hello@cozycat.ru")
    work_hours = models.TextField(verbose_name="Часы работы", default="Пн-Пт: 8:00-22:00, Сб-Вс: 9:00-23:00")
    map_image = models.ImageField(upload_to='contacts/', verbose_name="Изображение карты", blank=True, null=True)

    class Meta:
        verbose_name = "Контент страницы контактов"
        verbose_name_plural = "Контент страницы контактов"

    def __str__(self):
        return "Контент страницы контактов"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    ingredients = models.TextField(verbose_name="Состав", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True, verbose_name="Изображение")
    is_available = models.BooleanField(default=True, verbose_name="Доступно")
    is_special = models.BooleanField(default=False, verbose_name="Акционное предложение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Позиция меню"
        verbose_name_plural = "Позиции меню"


class Review(models.Model):
    author_name = models.CharField(max_length=100, verbose_name="Имя автора")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Рейтинг"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    image = models.ImageField(upload_to='reviews/', blank=True, null=True, verbose_name="Фото котика")

    def __str__(self):
        return f"Отзыв от {self.author_name} ({self.rating}/5)"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class PreOrder(models.Model):
    TIME_CHOICES = [
        ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'),
        ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'),
        ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'),
        ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'),
    ]

    customer_name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    items = models.TextField(verbose_name="Состав заказа")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    pickup_time = models.CharField(max_length=5, choices=TIME_CHOICES, verbose_name="Время самовывоза")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнен")

    def __str__(self):
        return f"Заказ от {self.customer_name}"

    class Meta:
        verbose_name = "Предзаказ"
        verbose_name_plural = "Предзаказы"