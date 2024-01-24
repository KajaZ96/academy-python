isbn_number = "030640615"             #suma kontrolna, każda cyfra ma swoją wagę
isbn_number_calculation_sum = 0
for index, number in enumerate(isbn_number):            #indeks * wartość
    isbn_number_calculation_sum += (index + 1) * int(number)
print (f"Sum equeals {isbn_number_calculation_sum}")
checksum = isbn_number_calculation_sum % 11
print (f"Checksum for this ISBN number is {checksum}")    #https://pl.wikipedia.org/wiki/Mi%C4%99dzynarodowy_znormalizowany_numer_ksi%C4%85%C5%BCki#ISBN-10

