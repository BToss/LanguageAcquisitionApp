#TODO: translate from python to java

#Step 1 Person produces vowel as input and is passed into Kiss FFT

#Step 2 is utilizing the c library Kiss FFT
#go here to get it: https://github.com/itdaniher/kissfft
#FT takes input and produces values
# AudioAnalyzer/app/src/main/jni/AudioAnalyzerHelperJNI.cpp 
# The path above is to the windowing functions present in the AudioAnalyzer app. There isn't a Gaussian, but we can use their model
# to write one.

#output of 2 is passed into 3, file it as FFT result(see TODO below)

#Step 3 (The only written code currently): Extract important formants from spectra recived as output from step 2

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
print "Formants we care about = " + str(formants_we_care_about)GH

#TODO: step 4(Bark Difference Metric): Normalizes the vowel formants so different speakers register the same vowels
#zi = (26.81/((1+1960)/Fi))-0.53 aaaaaannnnnd then the output of that, the x axis is z3-z2  and y axis is z3-z1
#Step 5 is plotting matrix on graph utilizing above
#Step 6 is synthesizing exemplar vowel measurements into "target areas" on graph (See Archetype Calculations)
