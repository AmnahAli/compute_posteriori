from sys import argv

if len(argv) > 1:
	observations = argv[1]
else:
	observations = ""
#endif

outputFile = open("result.txt", 'w+')
outputFile.write("\nObservation Sequence of Q: %s\n" % observations)
outputFile.write("Length of the Q: %i\n" % len(observations))

observations = observations.upper()
# Assuming Q + 1 will be "C"
observations = " " + observations + "C"

probabilityHypo = [{ 'h1':0.1, 'h2':0.2, 'h3':0.4, 'h4':0.2, 'h5':0.1 }]
probabilityPrior = { 'C|h1':1, 'L|h1':0, 'C|h2':0.75, 'L|h2':0.25, 'C|h3':0.5, 'L|h3':0.5, 'C|h4':0.25, 'L|h4':0.75, 'C|h5':0, 'L|h5':1 
}
probabilityQueries = []

p = 0

for i in range(1, 6):
	temp = (probabilityPrior[observations[1] + '|h' + str(i)] * probabilityHypo[0]['h' + str(i)])
	p = p + temp
#endfor

probabilityQueries.append({ observations[1]:p })
obsLength = len(observations)

for i in range(1, obsLength - 1):
	outputFile.write("\nAfter Observation %i = %s:\n" % (i, observations[i]))
	
	if len(probabilityHypo) - 1 < i:
		probabilityHypo.append({})
	#endif
	if len(probabilityQueries) - 1 < i:
		probabilityQueries.append({})
	#endif
	
	temp = 0

	for j in range(1, 6):
		probabilityHypo[i]['h' + str(j)] = probabilityPrior[observations[i] + '|h' + str(j)] * probabilityHypo[i - 1]['h' + str(j)] / probabilityQueries[i - 1][observations[i]]		
		temp = temp + probabilityPrior[observations[i + 1] + '|h' + str(j)] * probabilityHypo[i]['h' + str(j)]		
		probabilityQueries[i][observations[i + 1]] = temp
	#endfor

        for k in range(1, 6):
	        outputFile.write("P(h%d|Q) = %.5f\n" % (k, probabilityHypo[-1]["h" + str(k)]))
        #endfor

        if observations[i] == "C" and observations[i + 1] == "L":
            probabilityNextObs = probabilityQueries[i][observations[i + 1]]
            outputFile.write("\nProbability that the next candy we pick will be C, given Q: %.5f\n" % (1.000 - probabilityNextObs))
            outputFile.write("Probability that the next candy we pick will be L, given Q: %.5f\n" % (probabilityNextObs))
        #endif

        elif observations[i] == "L" and observations[i + 1] == "C":
            probabilityNextObs = probabilityQueries[i][observations[i + 1]]
            outputFile.write("\nProbability that the next candy we pick will be C, given Q: %.5f\n" % probabilityNextObs)
            outputFile.write("Probability that the next candy we pick will be L, given Q: %.5f\n" % (1.000 - probabilityNextObs))
        #endif

        elif observations[i] == observations[i + 1] == "C":
            if probabilityQueries[i][observations[i]] > probabilityQueries[i][observations[i + 1]]:
                probabilityNextObs = probabilityQueries[i][observations[i]]
            else:
                probabilityNextObs = probabilityQueries[i][observations[i + 1]]
            #endif
            outputFile.write("\nProbability that the next candy we pick will be C, given Q: %.5f\n" % probabilityNextObs)
            outputFile.write("Probability that the next candy we pick will be L, given Q: %.5f\n" % (1.000 - probabilityNextObs))
        #endif

        elif observations[i] == observations[i + 1] == "L":
            if probabilityQueries[i][observations[i]] > probabilityQueries[i][observations[i + 1]]:
                probabilityNextObs = probabilityQueries[i][observations[i]]
            else:
                probabilityNextObs = probabilityQueries[i][observations[i + 1]]
            #endif
            outputFile.write("\nProbability that the next candy we pick will be C, given Q: %.5f\n" % (1.000 - probabilityNextObs))
            outputFile.write("Probability that the next candy we pick will be L, given Q: %.5f\n" % probabilityNextObs)
        #endif

#endfor

outputFile = open("result.txt", "r")
outputFileContents = outputFile.read()
print(outputFileContents)
outputFile.close()

#endoffile