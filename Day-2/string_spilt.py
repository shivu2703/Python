arn = "arn:aws:iam::123456789012:user/johndoe"

# Split the array by "/" , will create a list of two elements 
ans = arn.split("/")[1]

# We are printing the second element
print(ans)