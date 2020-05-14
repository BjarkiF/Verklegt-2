from django.shortcuts import render


def error_400(request, exception):
        data = {'status': 400}
        return render(request, 'status/status.html', data)


def error_403(request, exception):
        data = {'status': 403}
        return render(request, 'status/status.html', data)


def error_404(request, exception):
        data = {'status': 404}
        return render(request, 'status/status.html', data)


def error_500(request):
        data = {'status': 500}
        return render(request, 'status/status.html', data)


def error_503(request,  exception):
        data = {'status': 503}
        return render(request, 'status/status.html', data)
