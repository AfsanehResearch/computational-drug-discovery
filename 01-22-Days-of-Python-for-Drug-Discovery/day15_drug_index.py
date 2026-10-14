drugs = ["Retinol", "Calamine", "Crotamiton", "Talc", "Methoxsalen" ]
molecular_weights = [286.5, 241.068, 203.2802,379.26, 216.19]
solubilities = [0.04 ,3.5,0,0.06,7.6]
for index, drug in (enumerate (drugs)):
    if molecular_weights[index] > 250 and solubilities[index] < 0.1:
        print(drug, molecular_weights[index], solubilities[index]) 