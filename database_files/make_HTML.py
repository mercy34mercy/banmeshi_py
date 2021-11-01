from jinja2 import Template
def make_html(datas):
  html = '''
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <title>data sheet</title>
  </head>
  <body>
      <ul id="navigation">
      <table>
      <tr>
      {% for data in datas %}
          <th>{{data}}</th>
      {% endfor %}
      </tr>
      </table>
      </ul>

      <h1>data sheet</h1>
      {{ a_variable }}

  </body>
  </html>
  '''
  template = Template(html)
  return (template.render(datas))