clouds=[]
def user_input():
    for i in range(2):
        platforms=input("Enter the cloud platforms you know: ")
        clouds.append(platforms)
def brief_out():
    for platform in clouds:
        if platform == "aws":
            print(platform,"This is the worlds leading cloud platform and ranks number 1")
        elif platform == "azure" or platform == "gcp" or platform == "alibaba":
            print("This are the second popular platforms ")
        else:
            print("This is an Indian Cloud Platform")

user_input()
print("The different cloud platforms are : ", clouds)
brief_out()