from django.shortcuts import render,redirect
from django.views.generic import TemplateView , ListView , DetailView
from django.db.models import Q,Count
from .forms import CommentForm
from .models import(Hero,
    InnerHero,
    Service,
    Portfolio,
    Blog,
    BlogCategory,
    BlogImage,
    BlogTag,
    Testimonial,
    FAQ,
    Comment
)

class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['hero'] = Hero.objects.filter(
            is_active=True
        ).first()

        services = Service.objects.filter(
            is_active=True,
            show_on_home=True
        ).order_by('order')[:8]

        pricing_services = Service.objects.filter(
            is_active=True ,
            show_on_pricing=True
        ).order_by('order')[:4]

        icon_map = {
            'nail-extension': 'images/icon/nail.png',
            'gel-polish': 'images/icon/gel.png',
            'nail-repair': 'images/icon/repair.png',
            'nail-art': 'images/icon/design.png',
        }

        for service in services:
            service.icon = icon_map.get(service.slug)

        context['services'] = services

        context['pricing_services'] = pricing_services

        context['portfolios'] = Portfolio.objects.filter(
            is_active=True,
            show_on_home=True
        ).order_by('order')[:5]

        context['blogs'] = (
            Blog.objects
            .published()
            .filter(show_on_home=True)
            .order_by('-published_at')[:3]
        )

        context['testimonials'] = Testimonial.objects.filter(
            is_active=True,
            show_on_home=True
        ).order_by('order')[:3]

        context['faqs'] = FAQ.objects.filter(
            is_active=True,
            show_on_home=True
        ).order_by('order')[:4]

        return context

class ServiceListView(TemplateView):
   template_name = 'service/list.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['services'] = Service.objects.filter(
         is_active=True).order_by('order')
      context['innerhero'] = InnerHero.objects.active_for('service')
      return context
   
class PortfolioListView(TemplateView):
   template_name = 'portfolio/list.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['portfolios'] = Portfolio.objects.filter(
         is_active=True).order_by('order')
      context['innerhero'] = InnerHero.objects.active_for('portfolio')
      return context

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        queryset = (Blog.objects.published()
                    .select_related('category')
                    .order_by('-published_at')
                    .prefetch_related('tags'))
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
               Q(title__icontains=keyword)
               |Q(short_description__icontains=keyword)
               |Q(content__icontains=keyword)
               |Q(tags__name__icontains=keyword),
            ).distinct().order_by('-published_at')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = (BlogCategory.objects
        .filter(is_active=True)
        .annotate(blog_count=Count('blogs'))
        .order_by('order'))
        context['featured_post'] = Blog.objects.published().filter(
           featured=True).order_by('order').first()
        context['innerhero'] = InnerHero.objects.active_for('blog')
        context['popular_posts'] = Blog.objects.filter(
            is_active=True,
            is_published=True
         ).order_by('-views')[:3]
        return context    
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get_queryset(self):
         return Blog.objects.published()

    def get_object(self,queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = (BlogCategory.objects
        .filter(is_active=True)
        .annotate(blog_count=Count('blogs'))
        .order_by('order'))
        context['popular_posts'] = Blog.objects.published().order_by('-views')[:3]

        current_article = self.object
        

        context["related_posts"] = (
        Blog.objects.published().filter(
            category=current_article.category
        )
        .exclude(id=current_article.id)
        .order_by("-published_at")[:3]
    )
        context['approved_comments'] = Comment.objects.filter(is_active=True,
                    blog=current_article).order_by('-created_at')[:5]
        if 'comment_form' not in context:
         context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
      article = self.get_object()
      self.object = article
      form = CommentForm(request.POST)
      print(form.is_valid())
      print(form.errors)
      if form.is_valid():
          comment = form.save(commit=False)
          comment.blog = article
          comment.save()

          return redirect("blog_detail", article.slug)
    
      else:
          return self.render_to_response(
        self.get_context_data(comment_form=form)
    )
      

       

class CategoryBlogListView(ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
         slug = self.kwargs['slug']
         queryset = (Blog.objects.published()
                     .select_related('category')
                     .prefetch_related('tags')
                     .filter(category__slug=slug)
                     .order_by('-published_at'))

         return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['innerhero'] = InnerHero.objects.active_for('blog')
        context['categories'] = (BlogCategory.objects
        .filter(is_active=True)
        .annotate(blog_count=Count('blogs'))
        .order_by('order'))

        return context

class TagBlogListView(ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
         slug = self.kwargs['slug']
         queryset = (Blog.objects.published()
                     .select_related('category')
                     .prefetch_related('tags')
                     .filter(tags__slug=slug)
                     .order_by('-published_at'))

         return queryset
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)

      context['innerhero'] = InnerHero.objects.active_for('blog')
      context['categories'] = (BlogCategory.objects
        .filter(is_active=True)
        .annotate(blog_count=Count('blogs'))
        .order_by('order'))

      return context

