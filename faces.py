#implement function called "convert" that accepts a str
#converts :) and :( to an emoji
# implement main to ask user for input for string
def main():
    response = input("Are you :) or :(?")
    result = convert(response)
    print(result)

def convert(response):
     response = response.replace(':)', '🙂')
     response = response.replace(':(', '🙁')
     return response


main()
