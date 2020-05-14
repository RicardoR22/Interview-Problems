"""
You need to calculate a similarity score between a pair of handles by looking at the letters each contains,
scoring +1 for each letter in the alphabet that occurs in both handles but scoring –1 for each letter that occurs in only one handle.
Your function should return k handles from the array that have the highest similarity score to the new user’s handle.

"""

def suggest(user, handles, k):
    user_chars = {}
    results = {}

    for char in user:
        user_chars[char] = True

    for handle in handles:
        score = 0
        for char in handle:
            if char in user_chars:
                score += 1
            else:
                score -= 1
        results[handle] = score

    suggestions = []

    for _ in range(k):
        suggestion = max(results, key=results.get)
        suggestions.append(suggestion)
        results.pop(suggestion)

    return suggestions



handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
print(suggest('iLoveDogs', handles, k=2))
