from django.urls import path
from . import views
from django.urls import include
from .views import (
    handleLoginView,
    AdminHomeView,
    signout,
    AdminSectionsView,
    AdminSectionAdd,
    AdminSectionUpdateView,
    AdminSectionDelete,
    AdminSectionStatusUpdate,
    AdminCategoryView,
    AdminCategoryAdd,
    AdminCategoryUpdateView,
    AdminCategoryDelete,
    AdminCategoryStatusUpdate,
    AdminPackageView,
    AdminPackageAdd,
    AjaxGetCategoryView,
    AdminPackageStatusUpdate,
    AdminPackageUpdateView,
    AdminPackageDelete,
    HomeView,
    PackageView,
    PackageDetailsview,
    PackageBookView,
    AdminBookingView,
    AdminBookingDelete,
    AdminBlogView,
    AdminBlogAdd,
    AdminBlogDelete,
    AdminBlogUpdateView,
    AdminBlogStatusUpdate,
    BlogDetailsview,
    BlogView,
    Search

)
# from views import *

app_name = "travelsapp"

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('package/<int:pk>/', PackageView.as_view(), name='packages'),
    path('package/packageDetails/<int:pk>',PackageDetailsview.as_view(), name='packageDetails' ),
    path('packages/bookPackage/', PackageBookView.as_view(), name='bookPackage'),
    path('blog', BlogView.as_view(), name='blogPage'),
    path('blog/blogDetails/<int:pk>',BlogDetailsview.as_view(), name='blogDetails' ),
    path('search/', views.Search, name='Search'),




    # admin urls
    path('admin-login/', handleLoginView.as_view(), name='adminLogin'),
    path('med-admin/home', AdminHomeView.as_view(), name='adminHome'),
    path('logout', signout.as_view(), name='logout'),

    # sections urls
    path('med-admin/sections',AdminSectionsView.as_view(), name='adminSectionView' ),
    path('med-admin/sections/add/',AdminSectionAdd.as_view(), name='adminSectionAdd' ),
    path('med-admin/sections/sectionedit/<int:pk>/' ,AdminSectionUpdateView.as_view(), name='adminSectionUpdate' ),
    path('med-admin/delete-section/<int:id>/', views.AdminSectionDelete, name="deleteSection"),
    path('med-admin/update-section-status/<int:id>/', views.AdminSectionStatusUpdate, name="updateSectionStatus"),

    # category urls
    path('med-admin/categories', AdminCategoryView.as_view(), name='adminCategoryView'),
    path('med-admin/category/add/',AdminCategoryAdd.as_view(), name='adminCategoryAdd' ),
    path('med-admin/categories/categoryedit/<int:pk>/' ,AdminCategoryUpdateView.as_view(), name='adminCategoryUpdate' ),
    path('med-admin/update-category-status/<int:id>/', views.AdminCategoryStatusUpdate, name="updateCategoryStatus"),
    path('med-admin/delete-category/<int:id>/', views.AdminCategoryDelete, name="deleteCategory"),

    # packages urls
    path('med-admin/packages', AdminPackageView.as_view(), name='adminPackageView'),
    path('med-admin/package/add/',AdminPackageAdd.as_view(), name='adminPackageAdd' ),
    path('ajax/section-category/', AjaxGetCategoryView.as_view(), name='ajaxGetCategory'),
    path('med-admin/update-package-status/<int:id>/', views.AdminPackageStatusUpdate, name="updateCategoryStatus"),
    path('med-admin/packages/packageedit/<int:pk>/' ,AdminPackageUpdateView.as_view(), name='adminPackageUpdate' ),
    path('med-admin/delete-package/<int:id>/', views.AdminPackageDelete, name="deletePackage"),

    # booking url
    path('med-admin/bookings/', AdminBookingView.as_view(), name='adminBookingView'),
    path('med-admin/bookings/delete-booking/<int:id>/', views.AdminBookingDelete, name="deleteBooking"),


    # blogs urls

    path('med-admin/blogs/', AdminBlogView.as_view(), name='adminBlogView'),
    path('med-admin/blog/add/',AdminBlogAdd.as_view(), name='adminBlogAdd' ),
    path('med-admin/blogs/update-blog-status/<int:id>/', views.AdminBlogStatusUpdate, name="updateBlogStatus"),
    path('med-admin/blogs/blogedit/<int:pk>/' ,AdminBlogUpdateView.as_view(), name='adminBlogUpdate' ),
    path('med-admin/blogs/delete-blog/<int:id>/', views.AdminBlogDelete, name="deleteBlog"),





    


    



    
]
