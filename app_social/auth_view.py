# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from .models import Book
# from .serializers import BookSerializer
# from djoser.views import TokenCreateView
# from rest_framework.authentication import TokenAuthentication
# class CustomAuthToken(TokenCreateView):
#     """
#     This view allows users to authenticate and get the token.
#     You can use djoser’s built-in TokenCreateView for token generation.
#     """

#     # This view will automatically handle token generation using Djoser.
#     pass

# class UserBooksView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         # Get books uploaded by the logged-in user
#         books = Book.objects.filter(user=request.user)
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class UserFilesView(APIView):
#     """
#     This view fetches files uploaded by the authenticated user.
#     It uses token-based authentication.
#     """
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]

#     def get(self, request):
#         # Get all books uploaded by the authenticated user
#         user_books = Book.objects.filter(user=request.user)
#         if user_books.exists():
#             # Serialize the books and return them
#             serializer = BookSerializer(user_books, many=True)
#             return Response(serializer.data)
#         return Response({"message": "No books found."}, status=404)