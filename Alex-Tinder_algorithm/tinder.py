import numpy as np
def tinder(man_preferences, woman_preferences, capacities):
    """
    Parameters
    ----------
    man_preferences : dict
        A dictionary with mans as keys and their respective preference lists
        as values
    woman_preferences : dict
        A dictionary with womans as keys and their respective preference
        lists as values
    capacities : dict
        A dictionary with womans as keys and their capacities as values

    Returns
    -------
    sorted_woman_matching : dict
        A stable matching with womans as keys and lists of mans as values
    """
    #create list with the name of the men
    free_mans = list(man_preferences.keys())
    #create a dict for the matching of the men ex : { Alex : None }
    man_matching = {man: None for man in man_preferences.keys()}
    #create a dict for the matching of the women ex: {Emilia : [] }
    woman_matching = {woman: [] for woman in woman_preferences.keys()}
    #as long as there are free men 
    while free_mans:
        #remove the first men from the list
        man = free_mans.pop(0)
        #get hte preferences of this men
        man_prefs = man_preferences[man]
        #as long as the man does not have a match
        while (not man_matching[man]):
            #get the first preference
            if man not in woman_preferences[man_prefs[0]]:
                #remove the preference from the list 
                man_prefs.remove(man_prefs[0])
            # if the prefrence list is not empty
            if man_prefs != []:
                #get the first preferred woman
                woman = man_prefs[0]
                #get the preferences of the preferred woman
                woman_prefs = woman_preferences[woman]
                #assign the preferences 
                woman_matches = woman_matching[woman]
                #check if there is more space to add the women to the men 
                if len(woman_matches) < capacities[woman]:
                    #assign match to the men
                    man_matching[man] = woman
                    #assign match to the woman
                    woman_matching[woman] += [man]
                else:
                    #get the index of the current man 
                    man_idx = woman_prefs.index(man)
                    #get the index for the current man that is matched 
                    worst_idx = get_worst_idx(woman_prefs,woman_matches)
                    #get the name of the worst match
                    worst_match = woman_prefs[worst_idx]
                    #compare how the men rank
                    if man_idx < worst_idx:
                        #assign the worst man to be umatched
                        man_matching[worst_match] = None
                        #remove the worst man for the matches
                        woman_matches.remove(worst_match)
                        #remove the worst man as a prefernece 
                        man_preferences[worst_match].remove(woman)
                        #make the worst man available again 
                        free_mans.append(worst_match)
                        #assign match to the men
                        man_matching[man] = woman
                        #assign match to the woman
                        woman_matches += [man]
                    else:
                        #remove man from the preference
                        woman_prefs.remove(man)
                        #remove woman from the preference
                        man_prefs.remove(woman)
    #lets sort the preferences of the men s
        sorted_woman_matching= sort_matches(woman_matching,woman_preferences)

    return sorted_woman_matching

def get_worst_idx(preferences,matches):
    return np.max([woman_prefs.index(man_curr) for man_curr in preferences if man_curr in matches])
    
def sort_matches(woman_matching,woman_preferences):
    for woman, matches in woman_matching.items():
        #get the matches for the man
        woman_pref = woman_preferences[woman]
        #sort the matches based on the index of the prefrences of each man
        sorted_matches = sorted(matches, key=lambda x: woman_pref.index(x))
        #assign the sorted list back to the man
        woman_matching[woman] = sorted_matches
    return woman_matching