from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.


class ProfileList(APIView):
    """
    Returns a list of all profiles.

    Fetches all Profile objects from the database, serializes them, 
    and returns the data in a JSON response.
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    Handles retrieving and updating a profile by its ID.

    Methods:
    --------
    - get_object(pk): 
        Retrieves a profile by ID or raises a 404 error.

    - get(request, pk): 
        Returns the profile data for the given ID.

    - put(request, pk): 
        Updates the profile with the given ID. Returns updated data or a 400 error.
    """
    serializer_class = ProfileSerializer

    def get_object(self,pk):
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
        
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)