from modeltranslation.translator import register, TranslationOptions
from rooms.models import RoomModel


@register(RoomModel)
class RoomModelTranslationOptions(TranslationOptions):
    fields = ('title',)

