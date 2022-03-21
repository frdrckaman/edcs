"""Default sites module.

Define ``sites.py`` in your own module and set EDCS_SITES_MODULE_NAME
to the name of that module.

"""
from django.conf import settings

from edcs_sites.single_site import SingleSite

default_country = getattr(settings, "EDCS_SITES_DEFAULT_COUNTRY", "tanzania")
default_country_code = getattr(settings, "EDCS_SITES_DEFAULT_COUNTRY_CODE", "tz")
default_domain = getattr(settings, "EDCS_SITES_DEFAULT_DOMAIN", "localhost")

# all_sites = {
#     default_country
#     or "site": [
#         SingleSite(
#             1,
#             settings.APP_NAME,
#             country=default_country,
#             country_code=default_country_code,
#             domain=default_domain,
#         ),
#     ],
# }

# fqdn = "edcs.org"
fqdn = settings.EDCS_DOMAIN

# site_id, name, **kwargs
all_sites = {
    "tanzania": (
        SingleSite(
            10,
            "Muhimbili",
            title="Muhimbili National hospital",
            country_code="tz",
            country="tanzania",
            domain=f"mnh.tz.{fqdn}",
        ),
        SingleSite(
            11,
            "OceanRoadCancerInstitute",
            title="Ocean Road Cancer Institute",
            country_code="tz",
            country="tanzania",
            domain=f"orci.tz.{fqdn}",
        ),
    ),
    "uganda": (
        SingleSite(
            20,
            "UgandaCancerInstitute",
            title="Uganda Cancer Institute",
            country_code="ug",
            country="uganda",
            domain=f"uci.ug.{fqdn}",
        ),
        SingleSite(
            21,
            "Mulago",
            title="Mulago National Referral Hospital",
            country_code="ug",
            country="uganda",
            domain=f"mnrh.ug.{fqdn}",
        ),
    ),
}
