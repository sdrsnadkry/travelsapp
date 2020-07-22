from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView, TemplateView, View, ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import SigninForm, ContactForm, SectionAddForm, CategoryAddForm, PackageAddForm, PackageBookForm, BlogAddForm
from django.urls import reverse_lazy
from .models import Section, Category, Packages, Bookings, Blogs
from django.db.models import Case, Value, When


# Create your views here.

class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['allBlogss'] = Blogs.objects.all()
        context['allSectionsMenu'] = Section.objects.all()
        context['allPackagesFooter'] = Packages.objects.all()
        # context['rootCatmenu'] = Category.objects.all()

        return context


class HomeView(BaseMixin, TemplateView):
    template_name = 'ClientTemplate/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popularPlaces'] = Category.objects.filter(
            popular=True).filter(active=True)
        context['valuePackages'] = Packages.objects.filter(
            best_value=True).filter(active=True)
        context['recommendedTrips'] = Packages.objects.filter(
            recommended=True).filter(active=True)

        context['allBlogs'] = Blogs.objects.filter(active=True)
        return context


class PackageView(BaseMixin, DetailView):
    template_name = "ClientTemplate/Package.html"
    model = Category
    context_object_name = "categoryObject"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoryId = self.kwargs['pk']
        context['allPackages'] = Packages.objects.filter(category=categoryId)

        return context


class PackageDetailsview(BaseMixin, DetailView):
    template_name = "ClientTemplate/PackageDetail.html"
    model = Packages
    context_object_name = "packageobject"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PackageBookForm

        return context


class PackageBookView(SuccessMessageMixin, CreateView):
    template_name = "ClientTemplate/PackageDetail.html"
    form_class = PackageBookForm
    success_url = reverse_lazy('travelsapp:homepage')

    def get_success_message(self, cleaned_data):
        return "We will contact You Soon !!"


class BlogDetailsview(BaseMixin, DetailView):
    template_name = "ClientTemplate/BlogDetail.html"
    model = Blogs
    context_object_name = "blogObject"


class BlogView(BaseMixin, TemplateView):
    template_name = 'ClientTemplate/Blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listBLogs'] = Blogs.objects.filter(active=True)
        return context


def Search(request):
    query = request.GET['search_country']
    query2 = request.GET['min_budget']
    query3 = request.GET['max_budget']
    countryPackage = Packages.objects.filter(section=query).filter(package_discount__gte=query2).filter(package_discount__lte=query3)

    # allpackages = countryPackage.union(allprodscat, allprodsdesc)
    params = {'allpackages': countryPackage}
    return render(request, 'ClientTemplate/Search.html', params)


class handleLoginView(FormView):
    template_name = 'AdminTemplate/Adminlogin.html'
    form_class = SigninForm
    success_url = reverse_lazy('travelsapp:adminHome')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(self.request, 'Welcome To Dashboard')
            login(self.request, user)
        else:
            messages.error(self.request, 'Invalid Username Or Password')
            return render(self.request, "AdminTemplate/adminLogin.html", {"form": form})
        return super().form_valid(form)

   
class signout(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged Out Successfully')
        return redirect('/admin-login')


class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect("/admin-login")
        return super().dispatch(request, *args, **kwargs)


class AdminHomeView(AdminRequiredMixin, TemplateView):
    template_name = 'AdminTemplate/AdminDashboard.html'


class AdminSectionsView(AdminRequiredMixin, ListView):
    # objects = models.Manager()
    template_name = 'AdminTemplate/SectionsTemplate/ListSection.html'
    queryset = Section.objects.all()
    context_object_name = 'sectionsList'


class AdminSectionAdd(AdminRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'AdminTemplate/SectionsTemplate/AddSection.html'
    form_class = SectionAddForm
    success_url = reverse_lazy('travelsapp:adminSectionView')
    success_message = "Section Was Created successfully"


class AdminSectionUpdateView(AdminRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'AdminTemplate/SectionsTemplate/AddSection.html'
    form_class = SectionAddForm
    model = Section
    success_url = reverse_lazy('travelsapp:adminSectionView')
    success_message = "Section Was Updated successfully"


def AdminSectionDelete(request, id):
    section = Section.objects.filter(id=id)
    section.delete()
    messages.success(request, "Section Was Deleted Successfully")
    return redirect('/med-admin/sections')


def AdminSectionStatusUpdate(request, id):
    section = Section.objects.filter(id=id).update(active=Case(
        When(active=True, then=Value(False)), default=Value(True)))
    active_status = Section.objects.filter(
        id=id).values_list('active', flat=True)
    return HttpResponse(active_status)


class AdminCategoryView(AdminRequiredMixin, ListView):
    template_name = 'AdminTemplate/CategoriesTemplate/ListCategories.html'
    queryset = Category.objects.all()
    context_object_name = 'categoriesList'


class AdminCategoryAdd(AdminRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'AdminTemplate/CategoriesTemplate/AddCategory.html'
    form_class = CategoryAddForm
    success_url = reverse_lazy('travelsapp:adminCategoryView')
    success_message = "Category Was Created successfully"


class AjaxGetCategoryView(TemplateView):
    template_name = 'AdminTemplate/PackagesTemplate/AjaxGetCategories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section_id = self.request.GET['section_id']
        section_object = Section.objects.get(id=section_id)
        category = Category.objects.filter(section=section_object)
        context['relatedCategory'] = category

        return context


class AdminCategoryUpdateView(AdminRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'AdminTemplate/CategoriesTemplate/AddCategory.html'
    form_class = CategoryAddForm
    model = Category
    success_url = reverse_lazy('travelsapp:adminCategoryView')
    success_message = "Category Was Updated successfully"


def AdminCategoryStatusUpdate(request, id):
    category = Category.objects.filter(id=id).update(active=Case(
        When(active=True, then=Value(False)), default=Value(True)))
    active_status = Category.objects.filter(
        id=id).values_list('active', flat=True)
    return HttpResponse(active_status)


def AdminCategoryDelete(request, id):
    category = Category.objects.filter(id=id)
    category.delete()
    messages.success(request, "Category Was Deleted Successfully")
    return redirect('/med-admin/categories')


class AdminPackageView(AdminRequiredMixin, ListView):
    template_name = 'AdminTemplate/PackagesTemplate/ListPackages.html'
    queryset = Packages.objects.all()
    context_object_name = 'packagesList'


class AdminPackageAdd(AdminRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'AdminTemplate/PackagesTemplate/AddPackage.html'
    form_class = PackageAddForm
    success_url = reverse_lazy('travelsapp:adminPackageView')
    success_message = "Package Was Created successfully"


def AdminPackageStatusUpdate(request, id):
    package = Packages.objects.filter(id=id).update(active=Case(
        When(active=True, then=Value(False)), default=Value(True)))
    active_status = Packages.objects.filter(
        id=id).values_list('active', flat=True)
    return HttpResponse(active_status)


class AdminPackageUpdateView(AdminRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'AdminTemplate/PackagesTemplate/AddPackage.html'
    form_class = PackageAddForm
    model = Packages
    success_url = reverse_lazy('travelsapp:adminPackageView')
    success_message = "Packages Was Updated successfully"


def AdminPackageDelete(request, id):
    package = Packages.objects.filter(id=id)
    package.delete()
    messages.success(request, "Package Was Deleted Successfully")
    return redirect('/med-admin/packages')


class AdminBookingView(AdminRequiredMixin, ListView):
    template_name = 'AdminTemplate/BookingsTemplate/ListBookings.html'
    queryset = Bookings.objects.all()
    context_object_name = 'bookingsList'


def AdminBookingDelete(request, id):
    booking = Bookings.objects.filter(id=id)
    booking.delete()
    messages.success(request, "Booking Was Deleted Successfully")
    return redirect('/med-admin/bookings')


class AdminBlogView(AdminRequiredMixin, ListView):
    template_name = 'AdminTemplate/BlogsTemplate/ListBlogs.html'
    queryset = Blogs.objects.all()
    context_object_name = 'blogsList'


class AdminBlogAdd(AdminRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'AdminTemplate/BlogsTemplate/AddBlog.html'
    form_class = BlogAddForm
    success_url = reverse_lazy('travelsapp:adminBlogView')
    success_message = "Blog Was Created successfully"


class AdminBlogUpdateView(AdminRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'AdminTemplate/BlogsTemplate/AddBlog.html'
    form_class = BlogAddForm
    model = Blogs
    success_url = reverse_lazy('travelsapp:adminBlogView')
    success_message = "Blogs Was Updated successfully"


def AdminBlogStatusUpdate(request, id):
    blog = Blogs.objects.filter(id=id).update(active=Case(
        When(active=True, then=Value(False)), default=Value(True)))
    active_status = Blogs.objects.filter(
        id=id).values_list('active', flat=True)
    return HttpResponse(active_status)


def AdminBlogDelete(request, id):
    blog = Blogs.objects.filter(id=id)
    blog.delete()
    messages.success(request, "Blog Was Deleted Successfully")
    return redirect('/med-admin/blogs')
