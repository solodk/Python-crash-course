# Start with a copy of user_profile.py
# Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value
# pairs that describe you

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('Mykola', 'Solodkyi',
    occupation='unempoyed', location='Ukraine')
print(my_profile)