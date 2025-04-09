from django.http import JsonResponse

def api_root(request):
    return JsonResponse({"message": "Welcome to the Octofit API!", "url": "https://congenial-funicular-g54596v9g663wvwx.github.dev"})
