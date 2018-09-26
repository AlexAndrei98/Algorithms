def create_input_data(hospitals_file, residents_file):
    """creates 3 dicts with the hospitals, residents and the availavility of the hospitals"""
    new_hospital_list = {}
    capacities = {}
    new_residents_list = {}
    with open(hospitals_file ,mode= 'r') as hospitals :
        for line in hospitals:
            linesplit  = line.split()
            new_hospital_list[linesplit[0]] = linesplit[2:]
            capacities[linesplit[0]]= int(linesplit[1])
    new_residents_list = {}
    with open(residents_file,mode= 'r') as residents :
        for line in residents:
            linesplit  = line.split()
            new_residents_list[linesplit[0]]= linesplit[1:]
    return new_residents_list, new_hospital_list, capacities

def print_pretty(matches):
    for k,v in matches.items():
        print(k,"\t:", " ".join(v))