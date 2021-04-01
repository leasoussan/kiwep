from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer 
from .models import Task 









# to get functionality fro rest 
@api_view(['GET'])
def todoOverview(request):
    todo_urls = {
        'List': '/task_list/',
        'Detail View': '/task_detail/<str:pk>/',
        'Create': '/task_create/',
        'Update': '/task_update/<str:pk>/',
        'List': '/task_delete/<str:pk>/',
    }
    return Response(todo_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):

    serializer = TaskSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)



@api_view(['POST'])
def task_update(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)   


@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response("Item was deleted")    



def frontend_list_view(request):
    return render(request, 'todo/frontend/my_tasks_list.html')

def show_jokes(request):
    return render(request, 'todo/frontend/task.html')