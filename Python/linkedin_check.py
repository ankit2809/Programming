from linkedin import linkedin
API_KEY='xxxxxxx'
API_SECRET='xxxxxxxxx'
RETURN_URL='https://test.com'
auth = linkedin.LinkedInAuthentication(API_KEY,API_SECRET,RETURN_URL)
app = linkedin.LinkedInApplication(auth)
app.get_profile()
