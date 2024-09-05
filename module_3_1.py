calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()



print(string_info('Capybara'))
print(string_info('Armageddon'))

def is_contains(string, list_to_search):
    count_calls()
    isTrue = False
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            isTrue = True
            return isTrue
    if isTrue == False:
        return isTrue

        
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)