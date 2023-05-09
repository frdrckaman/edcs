from django.conf import settings
from django.http import HttpResponse

from edcs_export.constants import PROSPECTIVE_DATA, PROSPECTIVE_DATA_DICT
from edcs_export.models import DataDownload


def download_data(request):
    data_file = settings.EDCS_DATA_DOWNLOAD
    download_data_rec(request, PROSPECTIVE_DATA)
    response = HttpResponse(open(data_file, "rb"), content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="{}"'.format(
        f"{settings.EDCS_DATA_NAME}.zip"
    )
    return response


def download_dict(request):
    data_file = settings.EDCS_DATA_DICTIONARY
    download_data_rec(request, PROSPECTIVE_DATA_DICT)
    response = HttpResponse(open(data_file, "rb"), content_type="application/vnd.ms-excel")
    response["Content-Disposition"] = 'attachment; filename="{}"'.format(
        f"{settings.EDCS_DICT_NAME}.xlsx"
    )
    return response


def download_data_rec(request, data_type):
    dt = {
        "data_type": data_type,
        "username": request.user,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
    }
    DataDownload.objects.create(**dt)
