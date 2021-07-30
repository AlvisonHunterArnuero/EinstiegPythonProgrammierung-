import webbrowser as wb
url_lst = ['https://angular.io/','https://nodejs.org/en/','https://vuejs.org/']
for site in url_lst:
    print('Opening...',site)
    b = wb.open_new_tab(site)
print('All ready')
