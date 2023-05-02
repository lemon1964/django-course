from datetime import datetime


class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value


class My_Float_Converter:
    regex = '[+-]?(\d*\.)?\d+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)


class MyDateConverter:
    regex = '(((0[1-9])|([12][0-9])|(3[01]))-((0[0-9])|(1[012]))-((20[012]\d|19\d\d)|(1\d|2[0123])))'

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value):
        return value.strftime('%d-%m-%Y')

