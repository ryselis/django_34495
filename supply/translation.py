from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from supply.models import SupplyOrderGoodServiceBase, SupplyOrderGood


@register(SupplyOrderGoodServiceBase)
class SupplyOrderGoodServiceBaseTranslation(TranslationOptions):
    fields = ('title',)


@register(SupplyOrderGood)
class SupplyOrderGoodServiceBaseTranslation(TranslationOptions):
    fields = ()
