from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def hello_world(request):
    """
    Sample API endpoint that returns a greeting message
    """
    return Response({
        'message': 'Hello from Django!',
        'status': 'success',
        'data': {
            'framework': 'Django REST Framework',
            'frontend': 'React + TypeScript + Vite',
            'styling': 'TailwindCSS'
        }
    })

@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint
    """
    return Response({
        'status': 'healthy',
        'message': 'Backend is running'
    })

