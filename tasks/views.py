from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, TaskSerializer
from .models import User, Task

# Create your views here.
@api_view(['POST'])
def add_user(request):
    """Adding a new user
    """
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def add_task(request, userid):
    """Adding a new task for user with userid=userid
    """

    if request.method == 'POST':
        try:
            user = User.objects.get(id=userid)
        except User.DoesNotExist:
            return Response(
                {"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        

    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_tasks(request, userid):
    """Returning tasks for userid=userid
    """
    
    tasks = Task.objects.filter(userid=int(userid))
    serializer = TaskSerializer(tasks, many=True)

    if request.method == 'GET':
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_users(request):
    """Get list of available users
    """

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_task(request, taskid):
    """Deleting task with task_id=task_id
    """

    try:
        task = Task.objects.get(id=int(taskid))
    except Task.DoesNotExist:
        return Response(
            {"error": "Task does not exist"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'DELETE':  
        task.delete() # delete
        return Response(status=status.HTTP_200_OK)
    return 

@api_view(['DELETE'])
def delete_user(request, userid):
    """Deleting the user
    """
    try:
        user = User.objects.get(id=int(userid))
    except User.DoesNotExist:
        return Response(
            {"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'DELETE':
        tasks = Task.objects.filter(userid=int(userid))
        tasks.delete()
        user.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["PUT"])
def update_task(request, taskid):
    try:
        task = Task.objects.get(id=int(taskid))
    except Task.DoesNotExist:
        return Response(
            {"error": "Task does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_user(request, userid):
    try:
        user = User.objects.get(id=userid)
    except User.DoesNotExist:
        return Response(
            {"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
