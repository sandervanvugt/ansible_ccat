# plugins/filter/phone_format.py
def phone_format(number):
    return f"({number[:3]}) {number[3:6]}-{number[6:]}"

class FilterModule(object):
    def filters(self):
        return {
            'phone_format': phone_format
        }

