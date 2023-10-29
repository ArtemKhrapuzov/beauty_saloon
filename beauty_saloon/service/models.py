from django.db import models
from django.urls import reverse

FOR_WHAT = (
    ('default', ''),
    ('for hands', 'Для рук'),
    ('for legs', 'Для ног'),
    ('for nails', 'Для ногтей'),
)

FOR_WHAT_TOOLS = (
    ('default', ''),
    ('for a manicure', 'Для маникюра'),
    ('for pedicure', 'Для педикюра'),
)


class Product(models.Model):
    """Продукты"""
    name = models.CharField(max_length=255, verbose_name='Название')
    url = models.SlugField(max_length=160, unique=True, verbose_name='URL')
    trademark = models.CharField(max_length=255, verbose_name='Название торговой марки')
    compound = models.TextField(max_length=1000, verbose_name='Состав', blank=True, default='')
    volume = models.IntegerField(verbose_name='Объем (мл,гр)', blank=True, null=True)
    description = models.TextField(max_length=4000, blank=True, default='', verbose_name='Описание')
    color = models.CharField(max_length=50, verbose_name='Цвет', blank=True, default='')
    country = models.CharField(max_length=50, verbose_name='Страна производитель', blank=True, default='')
    for_what = models.CharField(max_length=30, verbose_name='Для чего', choices=FOR_WHAT, default='default',
                                blank=True)
    for_what_tools = models.CharField(max_length=30, verbose_name='Для чего инструменты', choices=FOR_WHAT_TOOLS,
                                      default='default', blank=True)
    best_before_date = models.CharField(max_length=50, verbose_name='Срок годность', blank=True, default='')
    where_buy = models.CharField(max_length=50, verbose_name='Где купить', blank=True, default='')
    link = models.TextField(max_length=2000, verbose_name='Ссылка на товар', blank=True, default='')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    cat = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    subtitle = models.ForeignKey('Subtitle', verbose_name='Подкатегория', on_delete=models.CASCADE, blank=True,
                                 default='')
    subsub = models.ForeignKey('Subsubtitle', verbose_name='Подподкатегория', on_delete=models.CASCADE, blank=True,
                               default='')

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.url})

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название категории')
    url = models.SlugField(max_length=160, verbose_name='URL')


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subtitle(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название подкатегории')
    url = models.SlugField(max_length=160, verbose_name='URL')
    cat = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cat} / {self.title}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Subsubtitle(models.Model):
    title = models.CharField(max_length=50, verbose_name='Подподкатегория')
    url = models.SlugField(max_length=160, verbose_name='URL')
    sub = models.ForeignKey('Subtitle', verbose_name='Подкатегория', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sub} / {self.title}'

    class Meta:
        verbose_name = 'Подподкатегория'
        verbose_name_plural = 'Подподкатегории'


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField(verbose_name='Mail')
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey("self", verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.product}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey('RatingStar', on_delete=models.CASCADE, verbose_name="звезда")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="фильм")

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ["value"]
