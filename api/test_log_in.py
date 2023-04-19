from utilities.setup import WebDriverSetup
import requests


class TestOH(WebDriverSetup):

    def test_01_valid_facebook_post(self):
        response = requests.post('https://www.facebook.com/login.php?skip_api_login=1&api_key=356713278727771&kid_directed_site=0&app_id=356713278727771&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D356713278727771%26auth_type%26cbt%3D1681899233865%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3d049df0736c88%2526domain%253Dqa.trado.co.il%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fqa.trado.co.il%25252Ff15102e4bbbac28%2526relation%253Dopener%26client_id%3D356713278727771%26display%3Dpopup%26domain%3Dqa.trado.co.il%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fqa.trado.co.il%252F%26locale%3Den_US%26logger_id%3Df358f2a5e01b2a8%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df371ff2c7d9e458%2526domain%253Dqa.trado.co.il%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fqa.trado.co.il%25252Ff15102e4bbbac28%2526relation%253Dopener%2526frame%253Df3bf3de85a1b68c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df371ff2c7d9e458%26domain%3Dqa.trado.co.il%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fqa.trado.co.il%252Ff15102e4bbbac28%26relation%3Dopener%26frame%3Df3bf3de85a1b68c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_US&pl_dbl=0', data={type: "facebook"})
        # Check if the response status code is 200 using an assertion
        assert response.status_code == 200, f"POST request failed. Status Code: {response.status_code}"
        # If the assertion passes, print a success message
        print("POST request was successful. Status Code: 200")

    def test_02_valid_google_post(self):
        response = requests.post('https://accounts.google.com/signin/oauth/error/v2?authError=ChVyZWRpcmVjdF91cmlfbWlzbWF0Y2gStQEKWW91IGNhbid0IHNpZ24gaW4gdG8gdGhpcyBhcHAgYmVjYXVzZSBpdCBkb2Vzbid0IGNvbXBseSB3aXRoIEdvb2dsZSdzIE9BdXRoIDIuMCBwb2xpY3kuCgpJZiB5b3UncmUgdGhlIGFwcCBkZXZlbG9wZXIsIHJlZ2lzdGVyIHRoZSBKYXZhU2NyaXB0IG9yaWdpbiBpbiB0aGUgR29vZ2xlIENsb3VkIENvbnNvbGUuCiAgGnVodHRwczovL2RldmVsb3BlcnMuZ29vZ2xlLmNvbS9pZGVudGl0eS9wcm90b2NvbHMvb2F1dGgyL2phdmFzY3JpcHQtaW1wbGljaXQtZmxvdyNhdXRob3JpemF0aW9uLWVycm9ycy1vcmlnaW4tbWlzbWF0Y2ggkAMqIAoGb3JpZ2luEhZodHRwczovL3FhLnRyYWRvLmNvLmlsMrECCAEStQEKWW91IGNhbid0IHNpZ24gaW4gdG8gdGhpcyBhcHAgYmVjYXVzZSBpdCBkb2Vzbid0IGNvbXBseSB3aXRoIEdvb2dsZSdzIE9BdXRoIDIuMCBwb2xpY3kuCgpJZiB5b3UncmUgdGhlIGFwcCBkZXZlbG9wZXIsIHJlZ2lzdGVyIHRoZSBKYXZhU2NyaXB0IG9yaWdpbiBpbiB0aGUgR29vZ2xlIENsb3VkIENvbnNvbGUuCiAgGnVodHRwczovL2RldmVsb3BlcnMuZ29vZ2xlLmNvbS9pZGVudGl0eS9wcm90b2NvbHMvb2F1dGgyL2phdmFzY3JpcHQtaW1wbGljaXQtZmxvdyNhdXRob3JpemF0aW9uLWVycm9ycy1vcmlnaW4tbWlzbWF0Y2g%3D&client_id=918041190286-ts0hq2o9fhq3adumgcj45a3vsp2fh8v9.apps.googleusercontent.com', data={type: "gmail"})
        # Check if the response status code is 200 using an assertion
        assert response.status_code == 200, f"POST request failed. Status Code: {response.status_code}"
        # If the assertion passes, print a success message
        print("POST request was successful. Status Code: 200")

    def test_03_valid_twitter_post(self):
        response = requests.post('https://cors.bridged.cc/https://api.twitter.com/oauth/request_token', data={type: "twitter"})
        # Check if the response status code is 200 using an assertion
        assert response.status_code == 200, f"POST request failed. Status Code: {response.status_code}"
        # If the assertion passes, print a success message
        print("POST request was successful. Status Code: 200")
