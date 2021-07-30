# --------------------------------------------------------------------------------
# A simple Breadcrumb Generator made in python 3 for a Codewars challenge
# Made with ❤️ in Python 3 by Alvison Hunter - March 8th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
def generate_bc(url, separator):
    home_url = '<a href="/">HOME</a>'
    resulting_url = middle_url = end_url = ""
    url_elem_list = url.split("/")
    last_element = url_elem_list[-1]
    item_before_last = len(url_elem_list) - 1

    if "index" in url_elem_list[-1]:
        url_elem_list.pop()

    if "." in url_elem_list[-1]:
        tmp_str = last_element.split(".")
        url_elem_list[-1] = tmp_str[0]

    for elem in range(1, item_before_last):
        middle_url += f'{separator}<a href="/{url_elem_list[elem]}/">{url_elem_list[elem].upper()}</a>'
        end_url = f'<span class="active">{url_elem_list[-1].upper()}</span>'

    if len(url_elem_list) <= 2:
        resulting_url = f"{home_url}{separator}{end_url}"
    else:
        resulting_url = f"{home_url}{middle_url}{separator}{end_url}"

    print("-"*65)
    print(resulting_url)



generate_bc("mysite.com/pictures/holidays.html", " : ")
# '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
generate_bc("www.codewars.com/users/GiacomoSorbi", " / ")
# '<a href="/">HOME</a> / <a href="/users/">USERS</a> /
# <span class="active">GIACOMOSORBI</span>'
generate_bc("www.microsoft.com/docs/index.htm", " * ")
# '<a href="/">HOME</a> * <span class="active">DOCS</span>'

generate_bc("mysite.com/pictures/holidays.html", " : ")
# <a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> :
# <span class="active">HOLIDAYS</span>')
generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / ")
# <a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">
# GIACOMOSORBI</span>')
generate_bc("www.microsoft.com/important/confidential/docs/index.htm#top", " * ")
# <a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> *
# <a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>')
generate_bc(
    "mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > ")
# <a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">
# VLUMSYME</a> > <span class="active">EXAMPLE</span>')
generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi",
            " + ")
# '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">
# GIACOMO SORBI</span>')
