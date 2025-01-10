# # from django.urls import path
# # from app_social.auth_view import GenerateTokenView, FileAccessView

# # urlpatterns = [
# #     path('token/', GenerateTokenView.as_view(), name='generate_token'),
# #     path('files/', FileAccessView.as_view(), name='file_access'),
# # ]
# from django.urls import path, include
# from app_social.auth_view import UserBooksView ,CustomAuthToken ,UserFilesView

# urlpatterns = [
#     path('', include('djoser.urls')),
#     path('', include('djoser.urls.authtoken')),
#     path('user-books/', UserBooksView.as_view(), name='user-books'),
#     path('token/login/', CustomAuthToken.as_view(), name='token_login'),
#     path('user-files/', UserFilesView.as_view(), name='user_files'),
# ]
# http://127.0.0.1:8000/api/user-files/
