from django.contrib import admin
from django.utils.html import format_html
from .models import (Hero,InnerHero,Service,ServiceCategory,ServiceFeature,Portfolio,PortfolioCategory,
                     PortfolioImage,Blog,BlogCategory,BlogImage,BlogTag,FAQ,Testimonial,SiteSetting,
                     ContactMessage,Comment)



@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):

    list_display = (
        "thumbnail",
        "title",
        "button_text",
        "is_active",
        "updated_at",
    )

    list_filter = (
    "is_active",
    "created_at",
    )

    search_fields = (
        "title",
        "subtitle",
    )

    readonly_fields = (
        "thumbnail",
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("محتوای هرو", {
            "fields": (
                "title",
                "subtitle",
                "description",
            )
        }),

        ("دکمه", {
            "fields": (
                "button_text",
                "button_link",
            )
        }),

        ("تصویر", {
            "fields": (
                "image",
                "thumbnail",
            )
        }),

        ("تنظیمات", {
            "fields": (
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    save_on_top = True

    list_per_page = 20

    ordering = (
        "title",
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:150px; height:90px; object-fit:cover; border-radius:8px;">',
                obj.image.url
            )
        return "-"

    thumbnail.short_description = "پیش‌نمایش"
# ==============================================================================================

@admin.register(InnerHero)
class InnerHeroAdmin(admin.ModelAdmin):

    list_display = (
        "page_name",
        "title",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "page_name",
        "title",
        "subtitle",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("محتوای هرو صفحات داخلی", {
            "fields": (
                "page_name",
                "title",
                "subtitle",
            )
        }),

        ("تنظیمات", {
            "fields": (
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    save_on_top = True

    list_per_page = 20

    ordering = (
        "page_name",
    )

# ==============================================================================================
class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 0
    ordering = ("order",)

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "order",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("اطلاعات", {
            "fields": (
                "name",
                "order",
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    ordering = ("order",)

    save_on_top = True


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "thumbnail",
        "title",
        "category",
        "order",
        "show_on_home",
        "is_active",
    )

    list_editable = (
        "order",
        "show_on_home",
        "is_active",
    )

    list_filter = (
        "category",
        "show_on_home",
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
        "thumbnail",
    )


    ordering = ("order",)

    fieldsets = (
        ("اطلاعات اصلی", {
            "fields": (
                "category",
                "title",
                "slug",
                "short_description",
                "description",
            )
        }),

        ("تصویر", {
            "fields": (
                "cover_image",
                "thumbnail",
            )
        }),

        ("تنظیمات", {
            "fields": (
                "order",
                "show_on_home",
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    save_on_top = True

    list_per_page = 20

    def thumbnail(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="width:150px; height:90px; object-fit:cover; border-radius:8px;">',
                obj.cover_image.url
            )
        return "-"

    thumbnail.short_description = "پیش‌نمایش"

    inlines = [
        ServiceFeatureInline,
    ]

# ==============================================================================================
class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 0
    ordering = ("order",)

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "order",
        "is_active",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    list_filter = (
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "order",
    )
    fieldsets = (
        ("اطلاعات دسته", {
            "fields": (
                "name",
                "slug",
                "order",
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    save_on_top = True

    list_per_page = 20


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):

    list_display = (
        "thumbnail",
        "title",
        "category",
        "card_type",
        "show_on_home",
        "order",
        "is_active",
    )

    list_editable = (
        "show_on_home",
        "card_type",
        "order",
        "is_active",
    )

    list_filter = (
        "category",
        "show_on_home",
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
        "thumbnail",
    )

    ordering = (
        "order",
    )

    list_per_page = 20

    save_on_top = True

    inlines = [
        PortfolioImageInline,
    ]

    fieldsets = (
        ("اطلاعات اصلی", {
            "fields": (
                "category",
                "title",
                "slug",
                "short_description",
                "description",
            )
        }),

        ("تصویر", {
            "fields": (
                "cover_image",
                "thumbnail",
            )
        }),

        ("تنظیمات", {
            "fields": (
                "card_type",
                "show_on_home",
                "order",
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    def thumbnail(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="width:150px; height:90px; object-fit:cover; border-radius:8px;">',
                obj.cover_image.url
            )
        return "-"

    thumbnail.short_description = "تصویر"

# ==============================================================================================
class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 0
    ordering = ("order",)

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "order",
        "is_active",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("اطلاعات دسته", {
            "fields": (
                "name",
                "slug",
                "order",
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    save_on_top = True

    list_per_page = 20

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "order",
        "is_active",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("اطلاعات تگ", {
            "fields": (
                "name",
                "slug",
                "order",
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    save_on_top = True

    list_per_page = 20

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = (
        "thumbnail",
        "title",
        "category",
        "author",
        "featured",
        "show_on_home",
        "views",
        "is_active",
        "is_published",
    )

    list_editable = (
        "featured",
        "show_on_home",
        "is_active",
    )

    list_filter = (
        "category",
        "featured",
        "show_on_home",
        "is_active",
        "published_at",
    )

    search_fields = (
        "title",
        "short_description",
        "content",
        "author",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "tags",
    )

    readonly_fields = (
        "thumbnail",
        "views",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20

    save_on_top = True

    inlines = [
        BlogImageInline,
    ]

    fieldsets = (
        ("اطلاعات اصلی", {
            "fields": (
                "category",
                "tags",
                "title",
                "slug",
                "short_description",
                "content",
            )
        }),

        ("تصویر", {
            "fields": (
                "cover_image",
                "thumbnail",
            )
        }),

        ("انتشار", {
            "fields": (
                "author",
                "published_at",
                "reading_time",
            )
        }),

        ("تنظیمات", {
            "fields": (
                "featured",
                "show_on_home",
                "order",
                "is_active",
                "is_published",
            )
        }),

        ("آمار", {
            "fields": (
                "views",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    def thumbnail(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="width:150px; height:90px; object-fit:cover; border-radius:8px;">',
                obj.cover_image.url
            )
        return "-"

    thumbnail.short_description = "پیش‌نمایش"

# ==============================================================================================
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):

    list_display = (
        "question",
        "show_on_home",
        "order",
        "is_active",
    )

    list_editable = (
        "show_on_home",
        "order",
        "is_active",
    )

    search_fields = (
        "question",
        "answer",
    )

    list_filter = (
        "show_on_home",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "order",
    )

    save_on_top = True

    list_per_page = 20

    fieldsets = (
        ("سؤال", {
            "fields": (
                "question",
                "answer",
            )
        }),

        ("تنظیمات", {
            "fields": (
                "show_on_home",
                "order",
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

# ==============================================================================================
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "thumbnail",
        "full_name",
        "job_title",
        "rating",
        "show_on_home",
        "order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "show_on_home",
        "order",
        "is_active",
    )

    search_fields = (
        "full_name",
        "job_title",
        "comment",
    )

    list_filter = (
        "rating",
        "show_on_home",
        "is_active",
    )

    readonly_fields = (
        "thumbnail",
        "created_at",
        "updated_at",
    )

    ordering = (
        "order",
    )

    save_on_top = True

    list_per_page = 20

    fieldsets = (
        ("اطلاعات مشتری", {
            "fields": (
                "full_name",
                "job_title",
                "image",
                "thumbnail",
            )
        }),

        ("نظر", {
            "fields": (
                "comment",
                "rating",
            )
        }),

        ("تنظیمات", {
            "fields": (
                "show_on_home",
                "order",
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="70" height="70" style="border-radius:50%; object-fit:cover;">',
                obj.image.url
            )
        return "-"

    thumbnail.short_description = "تصویر"

# ==============================================================================================
@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):

    list_display = (
        "logo_preview",
        "site_name",
        "phone",
        "mobile",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "is_active",
    )

    readonly_fields = (
        "logo_preview",
        "favicon_preview",
        "created_at",
        "updated_at",
    )

    save_on_top = True

    fieldsets = (

        ("اطلاعات اصلی", {
            "fields": (
                "site_name",
                "site_description",
            )
        }),

        ("لوگو", {
            "fields": (
                "logo",
                "logo_preview",
                "favicon",
                "favicon_preview",
            )
        }),

        ("اطلاعات تماس", {
            "fields": (
                "phone",
                "mobile",
                "whatsapp",
                "email",
                "address",
            )
        }),

        ("ساعات کاری", {
            "fields": (
                "working_days",
                "working_hours",
            )
        }),

        ("شبکه‌های اجتماعی", {
            "fields": (
                "instagram",
                "telegram",
                "youtube",
                "aparat",
                "linkedin",
                "pinterest",
            )
        }),

        ("نقشه", {
            "fields": (
                "map_iframe",
            )
        }),

        ("SEO", {
            "classes": ("collapse",),
            "fields": (
                "meta_title",
                "meta_description",
                "meta_keywords",
            )
        }),

        ("تنظیمات", {
            "fields": (
                "copyright",
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="width:150px; height:90px; object-fit:contain; border-radius:8px;">',
                obj.logo.url
            )
        return "-"

    logo_preview.short_description = "لوگو"

    def favicon_preview(self, obj):
        if obj.favicon:
            return format_html(
                '<img src="{}" style="width:40px; height:40px; object-fit:contain;">',
                obj.favicon.url
            )
        return "-"

    favicon_preview.short_description = "فاوآیکون"

    def has_add_permission(self, request):
        return not SiteSetting.objects.exists()

# ==============================================================================================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "phone",
        "email",
        "subject",
        "is_read",
        "is_replied",
        "created_at",
        "updated_at",
    )

    list_editable = (
        "is_read",
        "is_replied",
    )

    list_filter = (
        "is_read",
        "is_replied",
        "created_at",
    )

    search_fields = (
        "full_name",
        "phone",
        "email",
        "subject",
        "message",
    )

    readonly_fields = (
        "full_name",
        "phone",
        "email",
        "subject",
        "message",
        "ip_address",
        "user_agent",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25

    save_on_top = True

    fieldsets = (
        ("اطلاعات فرستنده", {
            "fields": (
                "full_name",
                "phone",
                "email",
                "subject",
            )
        }),

        ("متن پیام", {
            "fields": (
                "message",
            )
        }),

        ("وضعیت", {
            "fields": (
                "is_read",
                "is_replied",
            )
        }),

        ("اطلاعات فنی", {
            "classes": ("collapse",),
            "fields": (
                "ip_address",
                "user_agent",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    def has_add_permission(self, request):
        return False

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "mobile",
        "blog",
        "short_text",
        "created_at",
        "is_active",
    )

    list_editable = (
        "is_active",
    )

    search_fields = (
        "name",
        "mobile",
        "text",
        "blog__title",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    readonly_fields = (
        "blog",
        "name",
        "mobile",
        "text",
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25

    save_on_top = True

    fieldsets = (
        ("اطلاعات کاربر", {
            "fields": (
                "name",
                "mobile",
            )
        }),

        ("نظر و مقاله", {
            "fields": (
                "blog",
                "text",
            )
        }),

        ("وضعیت", {
            "fields": (
                "is_active",
            )
        }),

        ("اطلاعات سیستم", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
            )
        }),
    )

    def short_text(self, obj):
        if len(obj.text) > 50:
            return obj.text[:50] + "..."
        return obj.text

    short_text.short_description = "متن نظر"