from urllib import parse

from django.urls.base import reverse
from edcs_dashboard.url_names import InvalidUrlName, url_names

from .keywords import Keywords


class NextUrlError(Exception):
    pass


class NextUrlParser:

    """A class to set `next_url`.

    `next_url` is  a qyerystring that follows the format of edcs_model model
        admin mixin for redirecting the model admin on save
        to a url other than the default changelist.
        * Note: This is not a url but parameters need to reverse
                to one in the template.

    User is responsible for making sure the url_name can be reversed
    with the given parameters.

    In your url &next=my_url_name,arg1,arg2&agr1=value1&arg2=
    value2&arg3=value3&arg4=value4...etc.

    * next_url_attrs:
        A list of querystring attrs to include in the next url.

        Format is:
            [param1, param2, ...]

    """

    keywords_cls = Keywords

    def __init__(self, url_name=None, url_args=None):
        try:
            # assume this is a key in global `url_names`
            self.url_name = url_names.get(url_name)
        except InvalidUrlName:
            if not url_name:
                raise NextUrlError(f"Invalid url_name. Got {url_name}.")
            # assume not a key but an explicitly declared `url_name`
            self.url_name = url_name
        self.url_args = url_args

    def querystring(self, objects=None, **kwargs):
        """Returns a querystring including "next_args" or ''.

        objects: a list of objects to from which to get attr values.
        """
        if self.url_args:
            next_args = "{}".format(",".join(self.url_args))
            url_kwargs = {k: v for k, v in kwargs.items() if k in (self.url_args or [])}
            keywords = self.keywords_cls(
                objects=objects,
                attrs=self.url_args,
                include_attrs=self.url_args,
                **url_kwargs,
            )
            querystring = parse.urlencode(keywords, encoding="utf-8")
            return f"{next_args}&{querystring}"
        return ""

    def reverse(self, model_wrapper=None, remove_namespace=None):
        keywords = self.keywords_cls(objects=[model_wrapper], attrs=self.url_args)
        url_name = self.url_name
        if remove_namespace:
            url_name = url_name.split(":")[1]
        return reverse(f"{url_name}", kwargs=keywords)
