it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# I. Find the length of the set it_companies
length_it_companies = len(it_companies)
print("Length of it_companies:", length_it_companies)
# II. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("Set after adding 'Twitter':", it_companies)
# III. Insert multiple IT companies at once to the set it_companies
new_companies = {'LinkedIn', 'Snapchat', 'TikTok'}
it_companies.update(new_companies)
print("Set after adding multiple companies:", it_companies)
# IV. Remove one of the companies from the set it_companies
it_companies.remove('Oracle')  # Let's remove 'Oracle' as an example
print("Set after removing 'Oracle':", it_companies)



