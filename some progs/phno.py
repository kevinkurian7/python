import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
ph=input('enter phone number with country coden')
phone_number=phonenumbers.parse(ph)
print(geocoder.description_for_number(phone_number,'en'))

print(carrier.name_for_number(phone_number,'en'))