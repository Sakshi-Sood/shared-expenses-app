from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Shared Expense API Running"
    })