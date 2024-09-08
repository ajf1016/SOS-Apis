from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from auth_app.models import UserProfile
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.utils import IntegrityError


# api for creating a new user
@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    # Retrieve the data from the request
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    phone = request.data.get('phone')
    gender = request.data.get('gender')
    locality = request.data.get('locality')
    city = request.data.get('city')
    state = request.data.get('state')

    if not (username and email and password and phone and gender and locality and city and state):
        return Response({
            "status_code": 6001,
            "message": "All fields (username, email, password, phone, gender, locality, city, state) are required"
        }, status=400)

    try:
        # Check if user with email or username or phone already exists
        if not User.objects.filter(email=email).exists() and not User.objects.filter(username=username).exists() and not UserProfile.objects.filter(phone=phone).exists():
            # Create the User
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            # Create the user profile if needed (assuming you have a UserProfile model)
            # You can now save additional fields like phone, gender, etc., to UserProfile
            UserProfile.objects.create(
                user=user,
                phone=phone,
                gender=gender,
                locality=locality,
                city=city,
                state=state
            )

            response_data = {
                "status_code": 6000,
                "message": "User created successfully",
                "user_id": user.id,
            }
            return Response(response_data, status=201)
        else:
            if User.objects.filter(email=email).exists():
                return Response({"status_code": 6001, "message": "User with email already exists"}, status=400)
            elif User.objects.filter(username=username).exists():
                return Response({"status_code": 6001, "message": "User with username already exists"}, status=400)
            elif UserProfile.objects.filter(phone=phone).exists():
                return Response({"status_code": 6001, "message": "User with phone already exists"}, status=400)

    except IntegrityError:
        return Response({"status_code": 6001, "message": "An error occurred while creating user. Please try again later."}, status=500)


# api for logging in a user
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({
            "status_code": 6001,
            "message": "Please provide both username and password"
        }, status=400)

    print(username, password)

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)

        return Response({
            "status_code": 6000,
            "message": "Login successful",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=200)
    else:
        return Response({
            "status_code": 6001,
            "message": "Invalid username or password"
        }, status=400)
