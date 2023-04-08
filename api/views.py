from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

# import models
from .models import Task

# import seralizers
from .serializers import TaskSerializer


@api_view(['GET'])
def get_tasks(request: Request) -> Response:
    '''get all tasks'''
    # all tasks
    tasks = Task.objects.all()
    # task_list
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def completed_tasks(request: Request) -> Response:
    """get completed data"""
    tasks = Task.objects.filter(completed=True)
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def in_completed_tasks(request: Request) -> Response:
    """get incompletet data"""
    tasks = Task.objects.filter(completed=False)
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def create_task(request: Request) -> Response:
    data = request.data
    serializer = TaskSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update(request: Request, pk: int) -> Response:
    data = request.data
    task = Task.objects.get(id=pk)

    serializer = TaskSerializer(instance=task, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

