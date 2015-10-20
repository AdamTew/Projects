import mechanize
import cookielib 

br = mechanize.Browser()

cookiejar = cookielib.LWPCookieJar() 
br.set_cookiejar( cookiejar ) 

br.set_handle_robots(False)

br.open('')

br.select_form("")        
br['username'] = ''
br['password'] = ''
br.submit()

