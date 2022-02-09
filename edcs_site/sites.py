from django.core.management import color_style
from edcs_sites.single_site import SingleSite

style = color_style()

fqdn = "edcs.org"


# site_id, name, **kwargs
all_sites = {
    "tanzania": (
        SingleSite(
            10,
            "muhimbili",
            title="Muhimbili National hospital",
            country_code="tz",
            country="tanzania",
            domain=f"tz.{fqdn}",
        ),
    ),
    "uganda": (
        SingleSite(
            20,
            "mulago",
            title="Mulago Hospital",
            country_code="ug",
            country="uganda",
            domain=f"ug.{fqdn}",
        ),
    ),
}
