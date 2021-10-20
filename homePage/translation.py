from modeltranslation.translator import register, TranslationOptions

from homePage.models import ContactModel
from rooms.models import RoomModel, BookInfoModel


# @register(BannerModel)
# class BannerModelTranslationOptions(TranslationOptions):
#     fields = ('title', 'description')

# @register(BookInfoModel)
# class BookInfoModelTranslationOptions(TranslationOptions):
#     fields = ('first_name', 'last_name', 'email',
#               'phone', 'country', 'district',
#               'city', 'postcode',
#               )
