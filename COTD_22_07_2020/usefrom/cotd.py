def challenge (thisset):
    set(thisset)
    bog = list(dict.fromkeys(thisset))
    answer = " ".join(sorted(bog))
    return answer
