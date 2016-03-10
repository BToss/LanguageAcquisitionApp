formants_wanted = 6
#TODO: Set buffer zone to the expected width of a formant/2
buffer_zone = 1
#TODO: Replace fft_result with the input from your fft function.
fft_result = [2,9,5,5,1,8,5,8,2,6,5,9,10,9,2]
print "fft_result = " + str(fft_result)
formants =[]
for i in range(formants_wanted):
    max_f   = -1
    max_val = -1
    for f in range(len(fft_result)):
        if max_val < fft_result[f]:
            max_f   = f
            max_val = fft_result[f]
    # Record max.
    formants.append(max_f)
    # Remove all points around the found point.
    removal_index = 0
    while removal_index <= 2*buffer_zone:
        fft_result[max_f-buffer_zone+removal_index] = 0
        removal_index += 1
print "all formants found = " + str(formants)
formants_we_care_about = sorted(formants)[1:4]
print "Formants we care about = " + str(formants_we_care_about)
