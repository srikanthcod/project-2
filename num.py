import phonenumbers
from phonenumbers import geocoder
phone_number1=phonenumbers.parse("+916281939819")
phone_number2=phonenumbers.parse("+919121650393")
phone_number3=phonenumbers.parse("+919542251537")
phone_number4=phonenumbers.parse("+393661410998")

print("\nphone numbers location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));
print(geocoder.description_for_number(phone_number4,"en"));

#lets track the phone numbers 
