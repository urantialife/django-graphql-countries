from countries import models


class QueryResolveMixin(object):

    def resolve_countries(self, info, **kwargs):
        return models.Country.objects.all()

    def resolve_languages(self, info, **kwargs):
        return models.Language.objects.all()

    def resolve_locales(self, info, **kwargs):
        return models.Locale.objects.all()

    def resolve_timezones(self, info, **kwargs):
        return models.Timezone.objects.all()
