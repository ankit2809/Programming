from linkedin import linkedin
API_KEY='77g9m61okx6drd'
API_SECRET='bjcw05JLqyW0TJnM'
RETURN_URL='https://test.com'
auth = linkedin.LinkedInAuthentication(API_KEY,API_SECRET,RETURN_URL)
app = linkedin.LinkedInApplication(auth)
app.get_profile()
