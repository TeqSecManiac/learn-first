email=input()

start=email.index('@')
end=email.index('.')
print(email[start+1:end],end='')