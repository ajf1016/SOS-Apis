from django.http import HttpResponse


def index(request):
    return HttpResponse('''
        <h1>Welcome to the SOS App</h1>
        <a href="/admin/">Go to Admin Page</a>
        <a href="https://github.com/ajf1016/SOS-Apis/blob/main/README.md" target="_blank">Api Docs</a>
    ''')
