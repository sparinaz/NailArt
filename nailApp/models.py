from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django_ckeditor_5.fields import CKEditor5Field


# ====Hero model=====

class Hero(models.Model):
    title = models.CharField(max_length=200,verbose_name="عنوان")
    subtitle = models.CharField(max_length=200, blank=True,verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="توضیحات")

    primary_button_text = models.CharField(
    max_length=50,
    verbose_name="متن دکمه اصلی"
    )

    primary_button_link = models.CharField(
        max_length=200,
        verbose_name="لینک دکمه اصلی",
        blank=True
    )

    secondary_button_text = models.CharField(
        max_length=50,
        verbose_name="متن دکمه دوم"
    )

    secondary_button_link = models.CharField(
        max_length=200,
        verbose_name="لینک دکمه دوم",
        blank=True
    )

    image = models.ImageField(upload_to="hero/",verbose_name="تصویر")

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "هرو صفحه اصلی"
        verbose_name_plural = "هرو صفحه اصلی"

    def __str__(self):
        return self.title
    
# ====InnerHero model=====    
class InnerHeroQuerySet(models.QuerySet):

    def active_for(self, page_name):
        return self.filter(
            page_name=page_name,
            is_active=True
        ).first()
       
class InnerHero(models.Model):

    objects = InnerHeroQuerySet.as_manager()

    page_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="نام صفحه"
    )

    title = models.CharField(
        max_length=200,
        verbose_name="عنوان"
    )

    subtitle = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="زیرعنوان"
    )

    is_active = models.BooleanField(
    default=True,
    verbose_name="فعال"
)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )


    class Meta:
        ordering = ["page_name"]
        verbose_name = "هدر صفحات داخلی"
        verbose_name_plural = "هدر صفحات داخلی"

    def __str__(self):
        return self.page_name

# ====ServiceCategory model=====

class ServiceCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="دسته‌بندی"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name="تاریخ ایجاد"
)

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "دسته خدمات"
        verbose_name_plural = "دسته‌های خدمات"

    def __str__(self):
        return self.name        

# ====Service model=====

class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="services",
        verbose_name="دسته خدمات"
    )

    title = models.CharField(
        max_length=150,
        verbose_name="عنوان خدمت"
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        verbose_name="اسلاگ"
    )

    short_description = models.CharField(
        max_length=250,
        verbose_name="توضیح کوتاه"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات کامل"
    )

    cover_image = models.ImageField(
        upload_to="services/covers/",
        verbose_name="عکس"
    )

    base_price = models.PositiveIntegerField(
    verbose_name="قیمت پایه"
    )

    show_on_pricing = models.BooleanField(
    default=False,
    verbose_name="نمایش در تعرفه‌ها"
    )

    is_featured = models.BooleanField(
    default=False,
    verbose_name="پرطرفدار"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    show_on_home = models.BooleanField(
        default=True,
        verbose_name="نمایش در صفحه اصلی"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )
    updated_at = models.DateTimeField(
    auto_now=True,
    verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات"

    def __str__(self):
        return self.title
        
# ====ServiceFeature model=====

class ServiceFeature(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="features",
        verbose_name="خدمت"
    )

    title = models.CharField(
        max_length=200,
        verbose_name="ویژگی"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب"
    )
    is_active = models.BooleanField(
    default=True,
    verbose_name="فعال"
)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "ویژگی خدمت"
        verbose_name_plural = "ویژگی‌های خدمت"

    def __str__(self):
        return self.title
    
# ====PortfolioCategory model=====    

class PortfolioCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="نام دسته"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="اسلاگ"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )
    created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name="تاریخ ایجاد"
)

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "دسته‌بندی نمونه کار"
        verbose_name_plural = "دسته‌بندی نمونه کارها"
    

    def __str__(self):
        return self.name  
  

# ====Portfolio model=====

class Portfolio(models.Model):
    category = models.ForeignKey(
        PortfolioCategory,
        on_delete=models.CASCADE,
        related_name="portfolios",
        verbose_name="دسته‌بندی"
    )

    title = models.CharField(
        max_length=200,
        verbose_name="عنوان"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="اسلاگ"
    )

    short_description = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="توضیح کوتاه"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    cover_image = models.ImageField(
        upload_to="portfolio/covers/",
        verbose_name="عکس کاور"
    )

    CARD_TYPES = [
    ("normal", "نرمال"),
    ("small", "کوچک"),
    ("tall", "بلند"),
    ("wide", "عریض"),
    ]

    card_type = models.CharField(max_length=10,choices=CARD_TYPES)

    show_on_home = models.BooleanField(
        default=False,
        verbose_name="نمایش در صفحه اصلی"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "نمونه کار"
        verbose_name_plural = "نمونه کارها"

    def __str__(self):
        return self.title 
 

# ====PortfolioImage model=====

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="نمونه کار"
    )

    image = models.ImageField(
        upload_to="portfolio/gallery/",
        verbose_name="تصویر"
    )
    

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
    default=True,
    verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "تصویر نمونه کار"
        verbose_name_plural = "تصاویر نمونه کار"

    def __str__(self):
        return f"{self.portfolio.title} - {self.order}"

# ====BlogCategory model=====

class BlogCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="نام دسته"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="اسلاگ"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "دسته‌بندی مقاله"
        verbose_name_plural = "دسته‌بندی مقالات"

    def __str__(self):
        return self.name

# ====BlogTag model=====

class BlogTag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="نام تگ"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="اسلاگ"
    )

    order = models.PositiveIntegerField(
    default=1,
    verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "تگ"
        verbose_name_plural = "تگ‌ها"

    def __str__(self):
        return self.name

# ====Blog model=====
class BlogQuerySet(models.QuerySet):

    def published(self):
        return self.filter(
            is_active=True,
            is_published=True
        )
    
class Blog(models.Model):
    objects = BlogQuerySet.as_manager()

    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blogs",
        verbose_name="دسته‌بندی"
    )

    tags = models.ManyToManyField(
        BlogTag,
        related_name="blogs",
        blank=True,
        verbose_name="تگ‌ها"
    )

    title = models.CharField(
        max_length=250,
        verbose_name="عنوان"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="اسلاگ"
    )

    short_description = models.CharField(
        max_length=350,
        verbose_name="خلاصه مقاله"
    )

    content = CKEditor5Field(
        verbose_name="متن مقاله"
    )

    cover_image = models.ImageField(
        upload_to="blog/covers/",
        verbose_name="عکس کاور"
    )

    author = models.CharField(
        max_length=100,
        default="Sanaz Nail Art",
        verbose_name="نویسنده"
    )

    reading_time = models.PositiveIntegerField(
        default=5,
        verbose_name="زمان مطالعه (دقیقه)"
    )

    views = models.PositiveIntegerField(
        default=0,
        verbose_name="تعداد بازدید"
    )

    featured = models.BooleanField(
        default=False,
        verbose_name="مقاله ویژه"
    )

    show_on_home = models.BooleanField(
        default=False,
        verbose_name="نمایش در صفحه اصلی"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="تاریخ انتشار"
    )

    is_published = models.BooleanField(
        default=False ,
        verbose_name=" منتشر شده")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

# ====BlogImage model=====

class BlogImage(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="مقاله"
    )

    image = models.ImageField(
        upload_to="blog/gallery/",
        verbose_name="تصویر"
    )

    caption = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان تصویر"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "تصویر مقاله"
        verbose_name_plural = "تصاویر مقاله"

    def __str__(self):
        return f"{self.blog.title} - {self.order}"
    
# ====FAQ model=====

class FAQ(models.Model):
    question = models.CharField(
        max_length=300,
        verbose_name="سؤال"
    )

    answer = models.TextField(
        verbose_name="پاسخ"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    show_on_home = models.BooleanField(
        default=True,
        verbose_name="نمایش در صفحه اصلی"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "سوال متداول"
        verbose_name_plural = "سوالات متداول"

    def __str__(self):
        return self.question    
    

# ====Testimonial model=====

class Testimonial(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name="نام مشتری"
    )

    job_title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="عنوان یا شغل"
    )

    comment = models.TextField(
        verbose_name="متن نظر"
    )

    image = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True,
        verbose_name="عکس مشتری"
    )

    RATING_CHOICES = [
    (1, "⭐"),
    (2, "⭐⭐"),
    (3, "⭐⭐⭐"),
    (4, "⭐⭐⭐⭐"),
    (5, "⭐⭐⭐⭐⭐"),
    ]

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        default=5,
        verbose_name="امتیاز",
    )

    show_on_home = models.BooleanField(
        default=True,
        verbose_name="نمایش در صفحه اصلی"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "نظر مشتری"
        verbose_name_plural = "نظرات مشتریان"

    def __str__(self):
        return self.full_name


# ====SiteSetting model=====

class SiteSetting(models.Model):
    site_name = models.CharField(
        max_length=100,
        verbose_name="نام سایت"
    )

    site_description = models.TextField(
        blank=True,
        verbose_name="توضیحات سایت"
    )

    logo = models.ImageField(
        upload_to="site/",
        verbose_name="لوگو"
    )

    favicon = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True,
        verbose_name="فاوآیکون"
    )

    phone = models.CharField(
        max_length=20,
        verbose_name="شماره تماس"
    )

    mobile = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="شماره موبایل"
    )

    whatsapp = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="شماره واتساپ"
    )

    email = models.EmailField(
        blank=True,
        verbose_name="ایمیل"
    )

    address = models.TextField(
        verbose_name="آدرس"
    )

    working_days = models.CharField(
        max_length=100,
        verbose_name="روزهای کاری"
    )

    working_hours = models.TextField(
    verbose_name="ساعات کاری"
)

    instagram = models.URLField(
        blank=True,
        verbose_name="اینستاگرام"
    )

    telegram = models.URLField(
        blank=True,
        verbose_name="تلگرام"
    )

    youtube = models.URLField(
        blank=True,
        verbose_name="یوتیوب"
    )

    aparat = models.URLField(
        blank=True,
        verbose_name="آپارات"
    )

    linkedin = models.URLField(
        blank=True,
        verbose_name="لینکدین"
    )

    pinterest = models.URLField(
        blank=True,
        verbose_name="پینترست"
    )

    map_iframe = models.TextField(
        blank=True,
        verbose_name="کد iframe نقشه"
    )

    copyright = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن کپی‌رایت"
    )

    meta_title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Meta Title"
    )

    meta_description = models.TextField(
        blank=True,
        verbose_name="Meta Description"
    )

    meta_keywords = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Meta Keywords"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return self.site_name


# ====ContactMessage model=====

class ContactMessage(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name="نام و نام خانوادگی"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="شماره تماس"
    )

    email = models.EmailField(
        blank=True,
        verbose_name="ایمیل"
    )

    subject = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="موضوع"
    )

    message = models.TextField(
        verbose_name="متن پیام"
    )

    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True,
        verbose_name="آدرس IP"
    )

    user_agent = models.TextField(
        blank=True,
        verbose_name="User Agent"
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name="خوانده شده"
    )

    is_replied = models.BooleanField(
        default=False,
        verbose_name="پاسخ داده شده"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ارسال"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"

    def __str__(self):
        return f"{self.full_name} | {self.subject or 'بدون موضوع'}"

class Comment(models.Model):

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="مقاله"
    )

    name = models.CharField(
        max_length=40,
        verbose_name="نام"
    )

    mobile = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name="شماره موبایل"
    )

    text = models.TextField(
        verbose_name="متن نظر"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ارسال"
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name="تایید شده"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return f"{self.name} - {self.blog.title}"