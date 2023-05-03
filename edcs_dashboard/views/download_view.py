from django.conf import settings
from django.http import HttpResponse


def download_data(request):
    data_file = settings.EDCS_DATA_DOWNLOAD
    response = HttpResponse(open(data_file, "rb"), content_type="application/zip")
    response["Content-Disposition"] = 'attachment; filename="{}"'.format(
        f"{settings.EDCS_DATA_NAME}.zip"
    )
    return response


def download_dict(request):
    data_file = settings.EDCS_DATA_DICTIONARY
    response = HttpResponse(open(data_file, "rb"), content_type="application/vnd.ms-excel")
    response["Content-Disposition"] = 'attachment; filename="{}"'.format(
        f"{settings.EDCS_DICT_NAME}.xlsx"
    )
    return response
