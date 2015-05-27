scripts = """
<script>
$('document').ready(fun1)
</script>
"""
#Sets graphic icon for page
icon = "list icon"

content = """
<div class="ui segment">

<p style="font-size:18px; text-align:center"> Our data is a Data Extract from the VicRoads Road Crash Information System. It provides information on Victorian crashes from 2010-2014 for educational purposes. Data included are time, location, conditions, crash type, road user type, etc. Note that our pivot table builder uses a restricted number of columns from the data for a more streamlined interface. Generally, the more interesting or relevant crash factors we chosen.
<br>
<br>
Our dataset is taken from data.vic.gov.au, and can be found <a href="https://www.data.vic.gov.au/data/dataset/road-crash-information-system-data-extract-may"> here </a>.
<br>
<br>
It was published on 01/05/2015, and last updated 06/05/2015. It is licensed under Creative Commons Attribution 3.0 Australia.
<br>
<br>
</p>

</div>
"""

from template import generate_html

page_title = "Our Data"

scripts = """
<script>
$('document').ready(fun1)
</script>
"""


generate_html(icon, content, page_title, scripts)