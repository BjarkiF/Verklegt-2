from django.shortcuts import render
from config.models import Config

import logging

def index(request):
    # TODO: add data from the manage config here.

    config = Config.objects.last()
    data = {
        'config': config
    }

    logging.info(data['config'].lat)
    logging.info(data['config'].long)

    return render(request, 'about/index.html', data)
