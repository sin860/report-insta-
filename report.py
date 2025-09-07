import os 
try:
	import instaloader
	import requests 
	import webbrowser
	from typing import Any
except:
	os.system('pip inatall instaloader ')
	os.system('pip inatall typing ')
class sin:
	def __init__(self):
		self.g=0
	def exit_csr(self)->any:
		api=requests.get('https://www.instagram.com').cookies.get('csrftoken')
		return api
	def user_for_id(self,user_id :str,)->any:
		B = instaloader.Instaloader()
		username = user_id
		profile = instaloader.Profile.from_username(B.context, username)
		return profile.userid
	def Send_Report(self,Sessionid:str,crf_tt:str,USER_E:str,)->any:
				try:
					url = "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/"
					payload = {
	  'container_module': "profilePage",
	  'entry_point': "1",
	  'location': "2",
	  'object_id': f"{USER_E!r}",
	  'object_type': "5",
	  'context': "{\"tags\":[\"ig_report_account\",\"ig_its_inappropriate\",\"violence_hate_or_exploitation\"],\"ixt_context_from_www\":\"QVFZWlRaZldlWnlJVlRtRklPMmRrNEoyd1p5WWVVRG9jblN3Slhra2JXY210QmJPQXU2YnNEcG16SHpVaFJhZXVKcVN2eU9GS25ZR3Q0a3dfWDE0ODRjeXpLWlZrb1ZQaHd0dDYwQklWMjVUcTNua05FdldGY1A1Nk5SUE9YYXM2SXhiVnh1WlJROTdBS3ZWdzRDQzREdkt5R2dsOFNoamRpekphdmZfQUJKVlFhYktzbERuQmN3S2dxUkxBVHQ3MnhsVDZqZ19kY1poTHJjT1F2N0hFMkE0dl9lQ3hINkl0aGVrU0RuNEdDbGtIamR1SGhwRm93ZnpxOXNxTVZMYUpZTGFVR0FnNEk2VnFjUGRJZGVjSklfOHl6azRsb1ZfNUhxa2lGWVlMaE5SdG9ZQzYtVjFhS05Wd2JVMkNvem5QMmVuT0JnUjdzblFJTEY0OEl0dzhaXzdsaXFXWlJoTDBiNDdfNHRxYS1iOUtjd3BQTjByZjMzcDRqZ0VIZkdZV2hjVXJmYVlLc21RQXJJWmFKOWtoRE9WZ2Y2LWJpUEt3T1BrdTU2YUZoUjV5bFBLWnJPQXBSQTlvdVdEcUJ3UmtzVkd3ZHJNcVdWUHJ5bGx4WWtzMm82ZlJOWWlRcl9WeHZBREpDRUxVamZnTkhEdEFjN0lzOFFLZlkzTGVkOHpXN1dBTXB1UkZhd09LcFZaSjNMQUpKZi13RmNLNXU3ajFrNi1DdHg3ZUVqUi1VTzQ0YXUtcHFySGM4VGRkaEtFdXh5cjhsUC1pb0s3SVhaWFBUd3lleFBQajlLcC1FWUNfanMwTjdKMkc5VWxsV2dzZ2UxZ3VaT0VXaGc3UklVUjN0Y2tldGhSTUR2X0xvd2FJenNDMHFmbWhEZmhubGpRejFsLTVhYTAyREhVYnpvX2ltNUllRTJBVXJ0eWpGVHdtTWxwS2l3ek51VEFHV2tPbVdxME56WHBMajVwa1hDRldBeGpoTUVDUU5BZmszR2o2NmVKeVBwakp5Q1FsUzEwUkFsUjc0YmRSSEpLTzN6MHNFMFMwTFNxQUVHZU5nZ1ZNbDJKZVJWU2hpRjVlX3NYb2NLdDVVTVJ4RDdVU25nelBxTXF4XzZNa3c1cnlPMVk5MDBNYmU4dmEtdTBLU1NqR3dBMkl6YXp4MFdRaHdEN0pfMG5HOG1VTG1CMWhmT2RUbUJlRllYbWhfTUZhTlFWU0ZObHpBMEpSaDBVT29veEg5bVFBOWJPRXVickd4Nl8tYmZwem5EZWZLNUxFX1V2djlGdlF0aE5BSFZHTHJqbmFoUEpfMThwdndqUTRRV3BuQnBNdFJ3NDdTaEU1YktzVEl3THQ2eVVXMWpHWFBTQUo5LUxvcV9lVmVqU3FZdDdkY0owaVgyNlo3SVhjOExiOWh6VWQyNlJMQXZFZ3daZTNBd3NoN2lYRlRYclVIUV9iQ0E2NUZIZVZHV0RJNHNyRHZzVi1NTDBtWUkxSUxLNVpVNE4ySURXOV9HaHVlaDhhbDZBMnIzN3BRdU5TSEtYRkpQNnZoU0J3U0xuTUNhbDZQVmpEZVBRc1RjT2hfRGJubWZmWXhGeWRRLXB2VVRkdW5yOWxJelFzeHh3cldnd2hvNk5VTjRrc0Rpa0p1R0xvQkpmd0t6dHRJWnZIZkNsQmQ3ZjZrcmVyZk53VHRPSk9kR0RFcWUta1QydmRBOTlRUl9QNVhsdXptdzJSeW40bko3N1NVMm5aQ1dJa3BUNUoyNFhOU0x1TmRJTjlMSXdYSWNISDB2WHBNOWNId0Zqd1Fhc2pJbXY1RWwyQ08wYXhvV1BIMW9MNGlZdzlBenZCT2pZT29zR19oOUU2eDg2VXBlbWJJNXhTUjRjeDhEZU1kNGxaMXkzMkNnWXZHZmVCQzVIR1lwczJGRnJLOFJRUnJhV2k3UVZnMi1uUl9tTVo4V0ZlQkowdkZqaFlqSWN3cndUd20wTjhwd0IwUXkwd1RkbVVRZzZSbkdrWjFUdktBeFlaVFhwM0Nud0dENmdDZFpVdE9OOHJlWjE1WGhoYkp5NjQ4Mi1sbE1mcWloUU84UzE5VnBkekNrbFBuNWFkU1MyejducmFGRUhnOUdPcm9EYWNxSGU2WmdULWMxSmo2QXdFdlV1OGpTU2YtZ1U3YTF5VlpWZlhaRTFjVGRuYnI2WUEyX0xCckYzWFdZejNvWEx1SkpXRWZQTEpFVVBJNjBMUmtvdzZrMWdBRUNxd1RNa0liWHV6R3paZHZmbVlBelVobTI3ejJZQjE5ODFkNmI2ZWtPY3pZT200R1E1Z3pBZTFJcHBLQ3Z4X2NZSHBzUkVnUWFLSm9iQ2tpUG9SZWVvMzhtZ2pjdElycThkLW9hczdYeGZZQVc4MHhCcld1M3ZmQmNOQ01rWlZkT2ZfTzRCVEU3ck5hVG12c2QySWFRLUNwemlqWUc2LTk1WXJMWWd4bkliUmNObHJOOXF1bXZfWEkzSWpPenhpRVNnbFA2NEVxcVJiam5hdGlqbV8xSkpsNmVhSGFMTzVuLVZ3bDQxdURQY2lvTWJUbDNrUWhtMFlOMDZWNjNnVTJMUXhvME9BTVFCeUstSjVPWDkwQXR2dGhrN0Radlp2dFB5eVhDYmNoaGIxVUdDeU5rdW1PM1BlSVBtcHZmd2NPM0pMMDE1ZzZGNTgyTEJHamlJdndDWEJLaXh0Vi1xRkNpWndkRy1rRXpoX1Zwc1R6TmpIbHYxLXNJc2d3QmJhRmwxM2d3dlNqSExvVnBDeFRFM0Y4X2NqZHgtdS1WaGNGNlF2ZkYtMzBlTWtOdDI2TVkyWVpyV0tZb1RUOEhnZXZob2I2Yk95MFhEWU1FcTVSNWt4SE55em00ZXlsU1FHVkxEODhGbDd0WU0xN3c3TTRVbTM0YkRieHEtUmg5aFFDdDBHOWhBUVhnQnFyZXZzdXRoLU02eElHak5PQXRqSmhDOGJfY2U0V3ZQeVRrXzVWMWdyWmhZX1BtWk1TdFZDdHpUSmFlRVdHd1o3ZmZwS0doenlfcVFrVGVJcFVTdDdfcmhuRENUTEs0eDJMVlF3V25fN1BjZ0tzMFBnVnRydWN0RWFYQlRTMzM3ZFEyWmhuUGU3VlhxZHRIbGtKM1E3ZXBpOXZlaUdBemgtOHdjTTV1UGJ4eWt0aWJUWFZJR2U5aGI2TkZNUEdvWUlFcmNvbFpoV2Rpakp2ay1OQl9TUTBSMEY0VFY4am9WT1oxd2d3ckFUbmIzMkhVTW1JbHBTbUt4elE1TmJpVDRfNVp4d0VTbmNabVBlem5VVWRIUlYwUmhicDdXSDI2dTVVdGZjNUFweVpYVHJYVGcwcHBJVlNKMTRLSkZ0cG05NlVKaE10MzRkU0JZUXU3cURseUx1djVteFFvSHE1cmtlcURvMHhfbzkzcndlMk9OeFJLY2ZEVU14QTBqTjJQNzVUdk5UeTB6WkJKNGlMem12NmhHX3FheVl2TU1jZGJ4aENYcFlPMlRBS2VJSjE1aTVFaVVnZUU5Sk1qaEdUSmZjaUpTZ0hkLVlZWHB1NW9zcV9jTGw4UExaU0t5UDJKRTR4ZkVCZl8wZHBsT29ocE5FNVFhaGV4bWVsYWVYVnB6UGhXTDVFZkFmOUtTdHo3bGxCZEJIR0w2Y3RTdEFYOVRhLXdnM1Q3a1RmSXhpT2NWUnBRVWxKSDRobGpzdkNuQ2pyOGFQRFZVTjFTVjFYMF81SVY1Rl9zR1VtMnJGQlZvblpGWDdicEFJem91ZTlaczBURUxKZXlqSzlpX3ByQmdRb0t4c09Ld0ZXR215Qm4yeUpqd0xxeFdNSHQ4ZWM3SWY2V29Nb1Z4aWp0ODMxTW5LaDVfcjFEcjlXMnRrZXhOMnExbVFpalYzSDk2ZnVJREJGT2dhaW9DXzFBdUF2TGJQZlI3dWpSaGYxX09wQXJnaFNpU21xcGp5ZDc3UHgtZmswak9VdUhkMzhsdV93TG1ZSmtCZE5GZTQwMnF3REhJLW1pRWRjRC1SRHJCSm9TRFB3TTFnYnA4OGt5YndHdWZRUmQyN0ZyUjZpV0c5RDVzTUgybUYwcDZBd2pCejhsQ0JTMEtNY25SWWYwdGlWQ0QwUFhndXlsZ0RacWFaQUVqZUw3ZkI3UnVyYm8yakZfbURTellEd2M1VWc1OUdKbHl3OU1NUi1XaXJES1otaWk3S3ZWRm94RXZZbi01ZC1vVVdKb3RUZklzaGdJZzA4QmVJSG81OUZjRHJtYU0xYjRTSVl0U21zYWpuRGI4NDJiUEFHeHBDR1ZBVXRSVlpxWHlyWU1VUnZIVmhKN2twV0hBVER5UnJ6RDdTQVFnMkNnS2tJRU9xV1JIYkIxOFFGVk1KQm5uRFM2V3BhenY1dUtjTmFFOEwtSzNxc3VDdmhSYUNTbm9BdTN2Sm5JYk1vZmRoU1FNdjhycl9Sdkx0WjZMR1ZncVBHa1JialpyeTNzb1JobzhfMEZYbVhXVHREdFliZkdBTVZXZW9DSEs0M19tMzN0MzJIZ1VBWG9zZ3gw\",\"frx_context_from_www\":\"{\\\"location\\\":\\\"ig_profile\\\",\\\"entry_point\\\":\\\"chevron_button\\\",\\\"session_id\\\":\\\"b6f2fe68-e6c2-402d-ba61-fa32742586c3\\\",\\\"tags\\\":[\\\"ig_report_account\\\",\\\"ig_its_inappropriate\\\",\\\"violence_hate_or_exploitation\\\"],\\\"object\\\":\\\"{\\\\\\\"user_id\\\\\\\":\\\\\\\""+repr(USER_E)+"\\\\\\\"}\\\",\\\"reporter_id\\\":17841477249253541,\\\"responsible_id\\\":17841402263455874,\\\"locale\\\":\\\"ar_AR\\\",\\\"app_platform\\\":1,\\\"extra_data\\\":{\\\"container_module\\\":\\\"profilePage\\\",\\\"app_version\\\":\\\"None\\\",\\\"is_dark_mode\\\":null,\\\"app_id\\\":1217981644879628,\\\"sentry_feature_map\\\":\\\"Jv7di5q+BBgNMzcuMjM2LjEwLjEwMxhvTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2GAVhcl9BUhwYIGE1OTk3Yzc1ZGE0ZmExNWUyYjZkNzFiMGQ5MDY3MWRhGCBmYzE0NTBiNTg5MDViOTVmNWU1YTM2YWRiZTAxYzRjOBggYzFlYzY5ZDc5NmMzYzU4ZDQ4MmI5OTFlNWM2ZmViZjIYIDczZjk2ZThjZmZmNzZkNjEwZjA0Njg2MDFjNTk1MDM3IRggZDUzOTZjNjZhMjM0NDBkOWYxMDQ5MjJhN2U1NGNiODAYJHQxM2QzMTExaDJfZThmMWU3ZTc4ZjcwXzVhYzcxOTdkZjlkMgA8LBgcYUp5MHV3QUJBQUdoTXpnY2hadUNSQ1dCdEJmSxbw6Y\\\\\\/ClGYAHBUCKwGIEWRpc3BsYXlfc2l6ZV90eXBlH0RldmljZVR5cGVCeURpc3BsYXlTaXplLlVOS05PV04AIjw5FQAZFQA5FQAAGCAwOWFmZmNiNzFmNGM0Mzg2ODkzZThjNzMxNDVmNjBjZBUCERIYEDEyMTc5ODE2NDQ4Nzk2MjgcFpjbm4bCsLI\\\\\\/GEAzNzQ4YTZmMmQ5NmY0OTM2YTM0ZmViZjI1MWNjMmM1YWU0MjBjNGRlMGM3ZDk2NGVkY2JjZmJhNTkwYTUzNjMyGBk3NzA2ODMzNDk3NToyMDoxNzU3MjI3NTU0ABwVBAASKChodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL3NoZXJpbnNiZWF1dHkvGA5YTUxIdHRwUmVxdWVzdAAWyoKum9SusT8oIy9hcGkvdjEvd2ViL3JlcG9ydHMvZ2V0X2ZyeF9wcm9tcHQvFigWxKjpiw1YATQYBVZBTElEAA==\\\",\\\"shopping_session_id\\\":null,\\\"logging_extra\\\":null,\\\"is_in_holdout\\\":null,\\\"preloading_enabled\\\":null},\\\"frx_feedback_submitted\\\":false,\\\"ufo_key\\\":\\\"ufo-3f1f7ad1-e14d-4742-b7c5-0893703561c8\\\",\\\"additional_data\\\":{\\\"is_ixt_session\\\":true,\\\"frx_validation_ent\\\":\\\"IGEntUser\\\"},\\\"profile_search\\\":false,\\\"screen_type\\\":\\\"frx_tag_selection_screen\\\",\\\"ent_has_music\\\":false,\\\"evidence_selections\\\":[],\\\"is_full_screen\\\":false}\"}",
	  'selected_tag_types': "[\"violent_hateful_or_disturbing-credible_threat\"]",
	  'frx_prompt_request_type': "2",
	  'jazoest': "22668"
	}
					headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36",
	  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"140.0.7339.51\", \"Not=A?Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"140.0.7339.51\"",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-ch-ua': "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
	  'sec-ch-ua-model': "\"SM-A217F\"",
	  'sec-ch-ua-mobile': "?1",
	  'x-ig-app-id': "1217981644879628",
	  'x-requested-with': "XMLHttpRequest",
	  'x-instagram-ajax': "1026809190",
	  'x-csrftoken': crf_tt,
	  'x-web-session-id': "mriw1e:1s55q9:caluxw",
	  'x-asbd-id': "359341",
	  'sec-ch-prefers-color-scheme': "light",
	  'x-ig-www-claim': "hmac.AR0Dchf5POXAfONXZuR6v_xVPZEe6hWkp5biFfX9JWzI4lC7",
	  'sec-ch-ua-platform-version': "\"12.0.0\"",
	  'origin': "https://www.instagram.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.instagram.com/sherinsbeauty/",
	  'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'priority': "u=1, i",
	  'Cookie': f"csrftoken={crf_tt}; sessionid={Sessionid}"
	}
	
					response = requests.post(url, data=payload, headers=headers).text
					
					if '"status":"ok"' in response:
						self.g+=1
						return f" [{self.g}] Report successfully  "
					else:
						return response
				except Exception as e:
					return e
														
	def lite_re(self,Sessionid:str,crf_tt:str,USER_E:str,)->any:
					try:
						url = f"https://i.instagram.com/users/{USER_E!r}/flag/"
						headers = {
    "User-Agent": "Mozilla/5.0",
    "Host": "i.instagram.com",
    "cookie": f"sessionid={Sessionid}",
    "X-CSRFToken":crf_tt,
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
						data = f"source_name=&reason_id=5&frx_context="

						r3 = requests.post(url, headers=headers, data=data, allow_redirects=False).text
						return r3		
					except Exception as e:
						return e				
					
OO=sin()
if __name__=='__main__':
				def home():
					try:
						user_id=input('USER >> ')
						if not user_id or len(user_id)<=2:
							raise Exception('This option must not be empty Or less than the required number . ')
						Sessionid=input('sessionid >> ')
						if not Sessionid:
							raise Exception ('A session must be added. ')
						crf_tt=OO.exit_csr()
						USER_E=OO.user_for_id(user_id)
						os.system('clear')
						print('''
1- instagram report 
2- instagram lite report 
3- Developer Information  <S I N>				
						''')
						INPUT_SELKT=input('Choose :- ')
						if INPUT_SELKT=='1':
							while True:								
								REportt=OO.Send_Report(Sessionid,crf_tt,USER_E)
								print(REportt)														
						elif INPUT_SELKT=='2':
							while True:
								USER_lite=OO.lite_re(Sessionid,crf_tt,USER_E)
								print(USER_lite)
						
						elif INPUT_SELKT=='3':
							webbrowser.open('https://t.me/SIN_PHP')
							exit('تم نقلك الى صفحه المطور ')		
						else:
							home()
					except Exception as e:
						print(e)		
home()