import re

def program(html_string):
    # Remove HTML tags using regular expressions
    clean_string = re.sub('<.*?>', '', html_string)
    
    # Find the content within the <body> tag
    body_start = html_string.find('<body>')
    body_end = html_string.find('</body>')
    
    if body_start != -1 and body_end != -1:
        body_content = clean_string[body_start:body_end]
        # Replace <br/> with newline characters
        body_content = body_content.replace('<br/>', '\n')
        return body_content.strip()
    else:
        return 'No content'

print(program('<body><h1>Toi la <b><i>Vu Nguyen Coder</i></b><h1></body>'))
print(program('<body>Vũ Nguyễn Coder<br/>youtube.com/VuNguyenCoder</body>'))
print(program('<htm><head title="Vu Nguyen Coder">'))
print(program('\
    <html>\
        <head></head>\
        <body>\
            <b>Bai hoc 11: Function</b><br/>\
            <i>1 - Dinh nghia</i><br/>\
            Function la mot kieu du lieu dac biet<br/>\
        </body>\
    </html>\
    '))