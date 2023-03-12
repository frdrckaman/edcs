"""Default sites module.

Define ``sites.py`` in your own module and set EDCS_SITES_MODULE_NAME
to the name of that module.

"""
from django.conf import settings

from edcs_sites.single_site import SingleSite

default_country = getattr(settings, "EDCS_SITES_DEFAULT_COUNTRY", "tanzania")
default_country_code = getattr(settings, "EDCS_SITES_DEFAULT_COUNTRY_CODE", "tz")
default_domain = getattr(settings, "EDCS_SITES_DEFAULT_DOMAIN", "localhost")

fqdn = settings.EDCS_DOMAIN
edcs = ""

if settings.EDCS_SITES_LIVE_DOMAIN:
    edcs = "edcs."


# site_id, name, **kwargs
all_sites = {
    "tanzania": (
        SingleSite(
            10,
            "Muhimbili National Hospital (MNH)",
            title="Muhimbili National hospital",
            country_code="tz",
            country="tanzania",
            domain=f"mnh.tz.{edcs}{fqdn}",
        ),
        SingleSite(
            11,
            "Ocean Road Cancer Institute (ORCI)",
            title="Ocean Road Cancer Institute",
            country_code="tz",
            country="tanzania",
            domain=f"orci.tz.{edcs}{fqdn}",
        ),
        SingleSite(
            12,
            "Bugando Medical Center",
            title="Bugando Medical Center",
            country_code="tz",
            country="tanzania",
            domain=f"bugando.tz.{edcs}{fqdn}",
        ),
        SingleSite(
            13,
            "Mbeya Referral Zonal Hospital",
            title="Mbeya Referral Zonal Hospital",
            country_code="tz",
            country="tanzania",
            domain=f"mbeya.tz.{edcs}{fqdn}",
        ),
        SingleSite(
            14,
            "Mwananyamala Regional Referral Hospital",
            title="Mwananyamala Regional Referral Hospital",
            country_code="tz",
            country="tanzania",
            domain=f"mwananyamala.tz.{edcs}{fqdn}",
        ),
    ),
    "uganda": (
        SingleSite(
            20,
            "Mulago National Referral Hospital (MNRH)",
            title="Mulago National Referral Hospital",
            country_code="ug",
            country="uganda",
            domain=f"mnrh.ug.{edcs}{fqdn}",
        ),
        SingleSite(
            21,
            "Uganda Cancer Institute (UCI)",
            title="Uganda Cancer Institute",
            country_code="ug",
            country="uganda",
            domain=f"uci.ug.{edcs}{fqdn}",
        ),
        SingleSite(
            22,
            "Makerere Lung Institute (MLI)",
            title="Makerere Lung Institute",
            country_code="ug",
            country="uganda",
            domain=f"mli.ug.{edcs}{fqdn}",
        ),
    ),
}
